import tkinter as tk
from tkinter import ttk
from tkinter import font
from tkinter import messagebox
import customtkinter as ctk

class MusicPlayer(tk.Tk):
    def __init__(self):
        super().__init__()

        # Load the FontAwesome font
        self.font_awesome = ctk.CTkFont(family="FontAwesome", size=16)

        self.title("Music Player ^^")
        self.geometry("600x440")
        self.configure(bg='#484444')
        
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
        

        edit_playlist_button = ctk.CTkButton(main_frame, text="Edit", command=self.create_playlist,width=75)
        edit_playlist_button.place(relx=0.50, rely=0.85, anchor=tk.N)

        delete_playlist_button = ctk.CTkButton(main_frame, text="Delete", command=self.create_playlist,width=75)
        delete_playlist_button.place(relx=0.85, rely=0.85, anchor=tk.N)

        play_button = ctk.CTkButton(player_frame, text="\uf04b", font=self.font_awesome, command=self.play_music,width=50)
        play_button.place(relx=0.5, rely=0.65, anchor=tk.N)

        back_button = ctk.CTkButton(player_frame, text="\uf04a", font=self.font_awesome, command=self.go_back,width=50)
        back_button.place(relx=0.15, rely=0.65, anchor=tk.N)

        forward_button = ctk.CTkButton(player_frame, text="\uf04e", font=self.font_awesome, command=self.go_forward,width=50)
        forward_button.place(relx=0.85, rely=0.65, anchor=tk.N)

        shuffle_button = ctk.CTkButton(fill_frame, text="\u21c4", font=self.font_awesome, command=self.go_forward,width=50)
        shuffle_button.place(relx=0.5, rely=0.65, anchor=tk.N)

    def create_playlist(self):
        messagebox.showinfo("Playlist", "Playlist Created :0")

    def play_music(self):
        messagebox.showinfo("Play", "Playing")

    def go_back(self):
        messagebox.showinfo("Back", "Going back")

    def go_forward(self):
        messagebox.showinfo("Forward", "Going forward")

if __name__ == "__main__":
    app = MusicPlayer()
    app.mainloop()