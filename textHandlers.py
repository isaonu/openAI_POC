
import csv
class TextHandler:
    """A class to handle the text we are going to create and inspect"""

    def create_file_with_text(self, text, name):
        """
        Save some text in a file

        Args:
            - text (str): The text to be saved in the file
            - name (str): Path and Name for the file (without extension)
        """
        with open(f'{name}.txt', 'w') as f:
            f.write(text)

    def get_text_from_transcript(self, file_path_name):
        """
        Save some text in a file

        Args:
            - text (str): The text to be saved in the file
            - name (str): Path and Name for the file (without extension)

        Returns:
            It will retrieve the text from a .txt file
        """
        text = ""
        with open(file_path_name) as f:
            lines = f.readlines()
            for line in lines:
                text += line + " "
        return text

    def create_csv_data(self, headers, data):
        """
        Creates a csv with three columns and its respective data. One column has the audio name, second one has the
        path of the audio and the third one has the bullet points of that audio.

        Args:
        - header (str): Header of the csv file
        - data (array of arrays): data fulfilling the headers, each run will be an array
        """
        with open(f"./csvData/audio_bullets.csv", 'w', newline="") as file:
            csvwriter = csv.writer(file)
            csvwriter.writerow(headers)
            for row in data:
                csvwriter.writerow(row)

    def read_csv_data(self, file_name_path):
        """
        It will read the csv file created in create_csv_data and created an array with this info, since we wont always
        have this array if we don't run the OpenAI's ChatGPT model

        Args:
        - path (str): Path to the file including file extension

        Returns:
        - str[]: An array with the data from the csv, one array per row
        """
        rows = []
        with open(file_name_path, 'r') as file:
            csvreader = csv.reader(file)
            header = next(csvreader)
            for row in csvreader:
                rows.append(row)
        return rows