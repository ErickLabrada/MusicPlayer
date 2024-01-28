import pygame
import os
import eyed3
import Dominio
from tkinter import filedialog
from tkinter import messagebox
import GUI
import DAOs
import tkinter as tk

isPlaying = False
global songs
pygame.mixer.init()
global playlistIndex
playlistIndex=0
global playlist
global firstTime
firstTime=True

def setUp():
    db_songs = [convert_db_song2(db_song) for db_song in DAOs.SongDAO.getAllSongs()]    
    print("Songs from database:", db_songs,"\n\n")

    songs=[]
    path="C:/Users/HP 240 G8/Documents/Python/Software testing/Music Player/Files/Music"
    for filename in os.listdir(path):
        if filename.endswith(".mp3"):

            audio_file  = eyed3.load(path+"/"+filename)

            album_name = audio_file.tag.album
            artist_name = audio_file.tag.artist

            song= Dominio.Song(audio_file.tag.title, audio_file.tag.artist, path+"/"+filename)
            songs.append(song)

    print("Songs from folder:", songs,"\n\n")
    s=""
    for song in songs:
        print (song.get_name())
        s=s+("Canción: "+song.get_name()+"|Artista: "+song.get_artist()+"\n")
        
        if song not in db_songs :
            print(f"Song not in database: {song}","\n\n")
            DAOs.SongDAO.insertSongs(song)

    
def getSongByNameAndArtist(name, artist):
    return convert_db_song(DAOs.SongDAO.getSongByNameAndArtist(name, artist))
    
def getPlaylistByName(name):
    return convert_db_playlist(DAOs.PlayListDAO.getPlaylist(name))

def playlist_list_setUp(playlists_list):
    db_playlists = DAOs.PlayListDAO.getAllPlaylists()
    for playlist in db_playlists:
        playlists_list.insert(tk.END, playlist[0]) if playlist else playlists_list.insert(tk.END, "Unknown")
    playlists_list.pack()

def setUpQueue(playlist,queue):
    
    queue.delete(0, tk.END)

    for song in playlist:
        queue.insert(tk.END, song) if playlist else playlists_list.insert(tk.END, "Empty")
    queue.pack()

def songs_list_setUp(playlists_list):
    db_songs = [convert_db_song(db_song) for db_song in DAOs.SongDAO.getAllSongs()]
    for song in db_songs:
        playlists_list.insert(tk.END, song)
    playlists_list.pack()
    
def convert_db_playlist(db_playlist):
    # Convert a tuple from the database to a Playlist object
    return Dominio.Playlist(db_playlist[0])

def convert_db_song(db_song):
    # Convert a tuple from the database to a Song object
    return Dominio.Song(db_song[0], db_song[1], db_song[2])

def convert_db_song2(db_song):
    # Convert a tuple from the database to a Song object
    return Dominio.Song(db_song[1], db_song[2], db_song[3])

def getFolderPath():
    return filedialog.askdirectory()

def loadSongs():
    path = getFolderPath()
    songs=[]
    for filename in os.listdir(path):
        if filename.endswith(".mp3"):

            audio_file  = eyed3.load(path+"/"+filename)

            album_name = audio_file.tag.album
            artist_name = audio_file.tag.artist

            song= Dominio.Song(audio_file.tag.title, audio_file.tag.artist, path+"/"+filename)
            songs.append(song)

    return songs

def create_playlist(name):
    DAOs.PlayListDAO.insertPlaylist(name)

def delete_playlist(name):
    DAOs.PlayListDAO.deletePlaylist(name)

def play_button(songs):
        
    global isPlaying

    if isPlaying:
        pause_song()
        isPlaying = False
        return "\uf04b"
    else:
        resume_song()
        isPlaying = True
        return "\uf04c"

    

def printSongs(songs):
    for song in songs:
        print("Name: "+song.get_name())
        print("Artist: "+song.get_artist())
        print("Url: "+song.get_url())
        #print("Img; "+song.get_cover())

def playSong(songs,index):
    global playlistIndex
    playlistIndex=index
    print ("Songs: ", songs)
    print ("playlistIndex: ", playlistIndex)
    print ("Song: ", songs[playlistIndex])


    pygame.mixer.music.load(songs[playlistIndex].get_url())
    pygame.mixer.music.play()

def resume_song():
    pygame.mixer.music.unpause()

def pause_song():
    pygame.mixer.music.pause()

def playNextSong(songs):
    global playlistIndex
    if 0 <= playlistIndex < len(playlist) - 1:
        playlistIndex += 1
        playSong(playlist,playlistIndex)
    else:
        messagebox.showinfo("bruh", "This is already the last song")

def playPreviousSong(songs):
    global playlistIndex
    if 0 < playlistIndex <= len(playlist):
        playlistIndex -= 1
        playSong(playlist,playlistIndex)
    else:
        messagebox.showinfo("bruh", "This is already the first song")
