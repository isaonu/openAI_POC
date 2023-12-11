# Find a topic in an audio file
This is a tool created to find some keyword - topic in an Audio file without having to 
listen to all the topics and waste time listening audios which won't give us the information
we are looking for.

This is a POC of bigger implementations, for example if we have a lot of voice notes in our phone
but we are not sure which one contains the information we are looking for, if there are some podcast which we listened
and we don't remember exactly which was the one that contained the information and many mores applications.

## Technologies
We are using the power of the OpenAI API to transcript some audio files and to get the bullet point of those
transcription so later on the user can search a given topic and be pointed to the respective audio file.

## Configuration - Setup
The needed libraries are in requirements.txt file, so you can just type:

`pip install -r requirements.txt`

Also, since this is using the OpenAI API, we need to configure a key to be able to use it. So for this you need to set 
an environment variable that is needed by this tool. So please get the value of your key for the openAI API and assign its
value to the environment variable "OPENAI_API_KEY"

## How to run it
Execute the file main.py.

When running the main.py file, the user will be requested to input the path of the audio files and also the keyword which
relates to the topic the user is interested to find in the audio files.

Here in the project we have a folder called "speeches" which contains some audio files. These audios are small, if you plan to process
longer audios, you may have to split them,

After the corresponding processing is done, the user may get a response with the audio file name which contains
information related to the topic, if there is no audio file found with the given keyword, the system will ask the user if he/she wants to
continue checking with another keyword and try again or if he/she wants to stop the search.

If the folder contains the same audios as the transcripts there won't be any new processing, it will use the existing 
information so it won't call openAI API.



