from gtts import gTTS
import os
from playsound  import playsound



mytext = 'hallo denu , this is new, welcome to the new world '
save = 'voicetry.mp3'
language = 'en'

myobj = gTTS(text=mytext, lang=language, slow=False)
myobj.save(save)


playsound(save)

# os.remove('voicetry.mp3')
