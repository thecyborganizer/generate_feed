import sys
import os
import datetime
from mutagen.mp3 import MP3
audio_filename = sys.argv[1]
audio = MP3(audio_filename)
outfile = open(sys.argv[2], "a")

outfile.write("<item>\n")
text = input("Title?")
outfile.write("<title>" + text + "</title>\n")
url = "http://www.pizzamymindcast.com/episodes/" + audio_filename
outfile.write("<link>" + url + "</link>\n")
outfile.write("<guid>" + url + "</guid>\n")
description = input("Description?")
outfile.write("<description>" + description + '\n\nIntro and outro from "Day At The Beach" by Atlantic Thrills, licensed under CC-BY-NC-ND.\n</description>\n')
outfile.write('<enclosure url="' + url + '" length="' + str(os.path.getsize(os.path.join(os.path.dirname(os.path.realpath(__file__)),audio_filename))) +'" ' + 'type="audio/mpeg"/>\n')
outfile.write('<category>Podcasts</category>\n')
dt = datetime.datetime.now()
outfile.write('<pubDate>' + dt.strftime("%a, %d %b %Y %X") + ' EST</pubDate>\n')
outfile.write('<itunes:author>Kaileigh Ahlquist and Joshua Keller</itunes:author>\n')
outfile.write('<itunes:explicit>No</itunes:explicit>\n')
outfile.write('<itunes:subtitle>' + description + '</itunes:subtitle>\n')
outfile.write('<itunes:summary>' + description + '</itunes:summary>\n')
duration_in_seconds = int(audio.info.length)
outfile.write('<itunes:duration>' + str(int(duration_in_seconds/3600)).zfill(2) + ":" + str(int(duration_in_seconds/60)) + ":" + str(duration_in_seconds % 60) + '</itunes:duration>\n')
outfile.write('<itunes:keywords>Food</itunes:keywords>\n')
outfile.write("</item>\n")