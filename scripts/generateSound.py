from google_speech import Speech
import os

# say "Hello World"
text1 = "Выключен ближний свет"
text = "Включен ближний свет"
lang = "ru"
speech = Speech(text, lang)

# you can also apply audio effects while playing (using SoX)
# see http://sox.sourceforge.net/sox.html#EFFECTS for full effect documentation
sox_effects = ("speed", "1.05")
speech.play(sox_effects)

# save the speech to an MP3 file (no effect is applied)
speech.save("../files/sound/off_low_light.mp3")

os.system("mpg321 ../files/sound/off_low_light.mp3 -quiet")