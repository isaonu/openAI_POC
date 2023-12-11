import os
import pathlib
import time

from summary import SummaryGPT
from textHandlers import TextHandler
from transcriptor import TranscriptorGPT
from userSearch import UserSearches


def get_audio_name_path(audios_file_path, file_name, audio_paths="./speeches"):
    """
    Get the full path and name of the audio files

    Args:
    - audios_file_path (str[]): Array that will contain all the path.
    - file_name (str[]): The file name of the audio file without extension
    """
    speeches_path = audio_paths
    for item in os.listdir(speeches_path):
        if os.path.isfile(os.path.join(speeches_path, item)) and pathlib.Path(item).suffix == ".mp3":
            audios_file_path.append(os.path.join(speeches_path, item))
            file_name.append(item[0:-4])
    return

def get_transcripts_file_names(file_name, transcript_paths="./transcript"):
    """
    Get the full path and name of the audio files

    Args:
    - audios_file_path (str[]): Array that will contain all the path.
    - file_name (str[]): The file name of the audio file without extension
    """
    for item in os.listdir(transcript_paths):
        if os.path.isfile(os.path.join(transcript_paths, item)) and pathlib.Path(item).suffix == ".txt":
            file_name.append(item[0:-4])
    return

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    audios_file_path = []
    file_name = []
    file_name_transcript = []
    data = []
    text = ""
    bullet_points = ""
    already_processed = False
    #Creating my objects
    summary_gpt = SummaryGPT()
    transcriptor_gpt = TranscriptorGPT()
    textHandlers = TextHandler()
    user_search = UserSearches()
    audio_found = False
    check_again = True
    # User interactions
    print(
        "##############################\n"
        "Welcome!! Now you will be able to find out which audio contains the info you need, and listen only that one, without having to listing all the audios you have and losing many time")
    user_path_audios = input("Please add the path of the folder which contains your audios: ")
    while(not audio_found and check_again):
        # Lets use ./speeches
        keyword_to_search = input("Please add the keyword you need to find in the audios: ")

        get_audio_name_path(audios_file_path, file_name, user_path_audios)
        get_transcripts_file_names(file_name_transcript)
        if(len(file_name) == len(file_name_transcript)):
            for i, item in enumerate(file_name):
                if(item in file_name_transcript):
                    already_processed = True
                else:
                    already_processed = False
                    break
        # Creating transcript files for each audio
        if(not already_processed):
            print("Processing audios")
            for i in range(len(audios_file_path)):
                #Adding this to overcome rate limit for whisper-1 and GPT turbo
                time.sleep(30)
                audio_transcript_text = transcriptor_gpt.sound_to_text_openai(audios_file_path[i])
                textHandlers.create_file_with_text(audio_transcript_text, f"./transcript/{file_name[i]}")
                text = textHandlers.get_text_from_transcript(f"./transcript/{file_name[i]}.txt")
                bullet_points = summary_gpt.summary_openai(text)
                data.append([file_name[i], audios_file_path[i], bullet_points])

            textHandlers.create_csv_data(["Audio Name", "Audio Path", "Bullet points"], data)
        summaries = textHandlers.read_csv_data("./csvData/audio_bullets.csv")
        audio_found = user_search.audio_with_topic(summaries, keyword_to_search)
        check_again = False
        if(not audio_found):
            continue_checking = input("Do you want to try with another keyword y/n: ")
            if(continue_checking.lower() == 'y'):
                check_again = True
            else:
                check_again = False




