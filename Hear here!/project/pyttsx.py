import pyttsx3
import os

def tts(fname,male):
    engine = pyttsx3.init()
    mytext=""
    try:
        fp=open('stories/'+fname+'.txt','r')
        for line in fp:
            mytext+=line
        fp.close()
    except:print('File handling error (stories/{}.txt)'.format(fname))

    voices = engine.getProperty('voices')
    if male==False: engine.setProperty('voice',voices[1].id)
    engine.save_to_file(mytext,'audio.mp3')
    engine.runAndWait()
    os.system('audio.mp3')
    os.remove('audio.mp3')
