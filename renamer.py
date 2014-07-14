# Renumber mp3 files based on the file name
from mutagen.easyid3 import EasyID3

import os

for root, dirs, files in os.walk("tracks"):
	for file in files:
		mp3 = EasyID3(os.path.join("tracks", file))

		mp3["tracknumber"] = str(int(file[0:3]))

		mp3.save()