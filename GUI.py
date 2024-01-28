import tkinter as tk
from tkinter import ttk
from tkinter import font
from tkinter import messagebox
from tkinter import simpledialog
import customtkinter as ctk
import Negocio as negocio
import Dominio
import DAOs
import random
from PIL import Image as PILImage, ImageTk


class ListDialog(tk.simpledialog.Dialog):
    def __init__(self, parent, title, items):
        self.items = items
        super().__init__(parent, title)

    def body(self, master):
        self.listbox = tk.Listbox(master, selectmode=tk.MULTIPLE)
        for item in self.items:
            self.listbox.insert(tk.END, item)
        self.listbox.pack()
        return self.listbox

    def apply(self):
        self.result = self.listbox.curselection()

class MusicPlayer(tk.Tk):
    def __init__(self):
        super().__init__()
        self.current_playlist=[]
        self.current_playlist_frame = None 
        # Load the FontAwesome font
        self.font_awesome = ctk.CTkFont(family="FontAwesome", size=16)
        self.title("Music Player ^^")
        self.geometry("600x440")
        self.configure(bg='#484444')
        self.resizable(False, False)
        global playlists_list
        global main_frame
        

        main_frame = ctk.CTkFrame(self, width=450, height=310,border_width=1)
        main_frame.grid(row=0, column=0,sticky="nsew")

        queue_frame = ctk.CTkScrollableFrame(self, width=90, height=310,border_width=1)
        queue_frame.grid(row=0, column=1,sticky="nsew")

        player_frame = ctk.CTkFrame(self, width=480, height=120,border_width=1)
        player_frame.grid(row=1, column=0,sticky="nsew")

        fill_frame = ctk.CTkFrame(self, width=120, height=120,border_width=1)
        fill_frame.grid(row=1, column=1,sticky="nsew")

        create_playlist_button = ctk.CTkButton(main_frame, text="Create", command=self.create_playlist,width=75)
        create_playlist_button.place(relx=0.15, rely=0.85, anchor=tk.N)
        

        edit_playlist_button = ctk.CTkButton(main_frame, text="Select folder", command=self.select_folder,width=75)
        edit_playlist_button.place(relx=0.50, rely=0.85, anchor=tk.N)

        playlists_list = tk.Listbox(main_frame)
        self.current_playlist_frame = tk.Listbox(queue_frame)

        self.delete_playlist_button = ctk.CTkButton(main_frame, text="Delete", command=self.delete_playlist,width=75)
        self.delete_playlist_button.place(relx=0.85, rely=0.85, anchor=tk.N)

        self.addSongs_button = ctk.CTkButton(main_frame, text="Add Songs", font=self.font_awesome, command=self.addSongs,width=75)
        self.addSongs_button.place(relx=0.85, rely=0.15, anchor=tk.N)

        self.deleteSongs_button = ctk.CTkButton(main_frame, text="Delete Songs", font=self.font_awesome, command=self.delete_song,width=75)
        self.deleteSongs_button.place(relx=0.85, rely=0.30, anchor=tk.N)

        self.startPlaylist_button = ctk.CTkButton(main_frame, text="Start playlist", font=self.font_awesome, command=self.start_playlist,width=75)
        self.startPlaylist_button.place(relx=0.85, rely=0.45, anchor=tk.N)

        self.play_button = ctk.CTkButton(player_frame, text="\uf04b", font=self.font_awesome, command=self.play_music,width=50)
        self.play_button.place(relx=0.5, rely=0.65, anchor=tk.N)

        back_button = ctk.CTkButton(player_frame, text="\uf04a", font=self.font_awesome, command=self.go_back,width=50)
        back_button.place(relx=0.15, rely=0.65, anchor=tk.N)

        forward_button = ctk.CTkButton(player_frame, text="\uf04e", font=self.font_awesome, command=self.go_forward,width=50)
        forward_button.place(relx=0.85, rely=0.65, anchor=tk.N)

        shuffle_button = ctk.CTkButton(fill_frame, text="\u21c4", font=self.font_awesome, command=self.shuffle,width=50)
        shuffle_button.place(relx=0.5, rely=0.65, anchor=tk.N)

        negocio.playlist_list_setUp(playlists_list)
        negocio.setUp()

    def delete_playlist(self):
        selected_index = playlists_list.curselection()
        if selected_index:
            selected_playlist = playlists_list.get(selected_index[0])  # Get the selected object
            negocio.delete_playlist(selected_playlist)
            messagebox.showinfo("Success", "Playlist deleted.")

    def showSongSelectionDialog(self, all_songs):
        # Create a list of strings to display in the dialog
        song_strings = [f"{song.get_name()} - {song.get_artist()}" for song in all_songs]

        # Show the dialog
        dlg = ListDialog(self.master, "Select Songs", song_strings)
        selected_song_indices = dlg.result
        print(selected_song_indices)


        # Map selected indices to corresponding Song objects
        selected_songs=[]
        for index in selected_song_indices:
            selected_songs.append(all_songs[index])
        return selected_songs

    

    def apply(self):
        selected_indices = self.listbox.curselection()
        self.result = selected_indices

    def delete_song(self):
        selected_index = playlists_list.curselection()
        if selected_index:
            selected_playlist = playlists_list.get(selected_index[0])  # Get the selected object
            
            all_songs = [negocio.convert_db_song(db_song) for db_song in DAOs.PlayListSongDAO.getPlaylistSongs(selected_playlist)]
            selected_songs = self.showSongSelectionDialog(all_songs)

            if selected_songs:
                # Insert selected songs into the playlist
                playlist_name = selected_playlist
                print("------------------------------------")
                for song in selected_songs:
                    print ("Name: ",song.get_name())
                    # Assuming Song has attributes like ID and name
                    song_name = song.get_name()  # Replace with the actual method to get the name
    
                    # Assuming you have a method to get the playlist name
                    playlist_name = selected_playlist
    
                    DAOs.PlayListSongDAO.deleteSongFromPlaylist(song_name, playlist_name)

                else:
                        print(f"Invalid song format: {song}")

                
                messagebox.showinfo("Success", "Songs deleted from the playlist.")

    def addSongs(self):
        selected_index = playlists_list.curselection()
        if selected_index:
            selected_playlist = playlists_list.get(selected_index[0])  # Get the selected object
           
            all_songs = [negocio.convert_db_song2(db_song) for db_song in DAOs.SongDAO.getAllSongs()]
            selected_songs = self.showSongSelectionDialog(all_songs)
            
            print(selected_songs)

            if selected_songs:
                # Insert selected songs into the playlist
                playlist_name = selected_playlist
                print("------------------------------------")
                for song in selected_songs:
                    print ("Name: ",song.get_name())
                    # Assuming Song has attributes like ID and name
                    song_name = song.get_name()  # Replace with the actual method to get the name
    
                    # Assuming you have a method to get the playlist name
                    playlist_name = selected_playlist
    
                    DAOs.PlayListSongDAO.insertSongIntoPlaylist(song_name, playlist_name)

                else:
                        print(f"Invalid song format: {song}")

                
                messagebox.showinfo("Success", "Songs added to the playlist.")

    def deleteSongs(self):
        print ("b")

    def select_folder(self):
        negocio.loadSongs()

    def create_playlist(self):
        name=simpledialog.askstring("Input", "Enter a string:")

        if name:
            negocio.create_playlist(name)

    def start_playlist(self):
        selected_index = playlists_list.curselection()
        if selected_index:
            selected_playlist = playlists_list.get(selected_index[0])
            selected = DAOs.PlayListSongDAO.getPlaylistSongs(selected_playlist)
            self.current_playlist = [negocio.convert_db_song(db_song) for db_song in selected]

        negocio.playlist = self.current_playlist
        negocio.playlistIndex = 0

        negocio.playSong(self.current_playlist, 0)
        negocio.setUpQueue(self.current_playlist, self.current_playlist_frame)  # Use self.current_playlist_frame

    
    def play_music(self):

        new_button_text = negocio.play_button(self.current_playlist)
        self.play_button.configure(text=new_button_text)
        
    def shuffle(self):  # Make shuffle an instance method
        playlist_backup = self.current_playlist
        random.shuffle(playlist_backup)
        self.current_playlist = playlist_backup
        negocio.setUpQueue(self.current_playlist, self.current_playlist_frame)


    def go_back(self):
        negocio.playPreviousSong(self.current_playlist)

    def go_forward(self):
        negocio.playNextSong(self.current_playlist)

if __name__ == "__main__":
    app = MusicPlayer()
    app.mainloop()