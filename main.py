import os
import sys
from ui import *

playlist = []
current_song =""
is_pause = False

class player():

    def __init__(self, play, pause, stop, next, prev, repeat, shuffle):
        self.play = play
        self.pause = pause
        self.stop = stop
        self.next = next
        self.prev = prev
        self.repeat = repeat
        self.shuffle = shuffle

       
    def playMusic(self, play):
        play = False;



    pass

class playlist():
    def __init__(self, adfile, addir, remfile, clist):
        self.adfile = adfile
        self.addir = addir
        self.remfile = remfile
        self.cllist = clist


    def addingFile(self, adfile):
        global current_song

        for song in playlist:
            song_listbox.insert("end", song)

    def addingDirectoryfile(self, addir):

        for file in os.listdir(root.directory):
            name, ext = os.path.splitext(file)
            if ext == '.mp3' or '.MP3':
                playlist.append(file)
            elif ext == '.wav' or '.WAV':
                playlist.append(file)
            elif ext == '.flac' or '.FLAC':
                playlist.append(file)
            elif ext == '.ogg' or '.OGG':
                playlist.append(file)
            else:
                print('Unknown Format.')

    def clearPlaylist(self, clist):
        playlist.clear()
        song_listbox.delete(0, END)

class tagdit():

    pass