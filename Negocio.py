import pygame
import os
import eyed3
import Dominio

pygame.mixer.init()
path="C:/Users/HP 240 G8/Documents/Python/Software testing/Music Player/Files/Music"

def loadSongs():
    songs=[]
    for filename in os.listdir(path):
        if filename.endswith(".mp3"):

            audio_file  = eyed3.load(path+"/"+filename)

            album_name = audio_file.tag.album
            artist_name = audio_file.tag.artist


            #for image in audio_file.tag.images:
                #image_file = open("{0} - {1}({2}).jpg".format(artist_name, album_name, image.picture), "wb")
                #image_file.write(image.image_data)
                #image_file.close()

            song= Dominio.Song(audio_file.tag.title, audio_file.tag.artist, "picture.png", path+"/"+filename)
            songs.append(song)

    return songs


def printSongs(songs):
    for song in songs:
        print("Name: "+song.get_name())
        print("Artist: "+song.get_artist())
        print("Url: "+song.get_url())
