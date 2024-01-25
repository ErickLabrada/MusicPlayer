import customtkinter as ctk
from tkinter import ttk

width = 480
height = 320

window = ctk.CTk()
window.geometry("600x440")
window.title("Music Player ^^")

mainFrame = ttk.Frame(window, width= 480, height = 320, borderwidth=1, relief=ctk.RAISED)
mainFrame.grid(row=0, column=0)
queueFrame = ttk.Frame(window, width=120, height=320,borderwidth=1, relief=ctk.RAISED)
queueFrame.grid(row=0,column=1)
playerFrame= ttk.Frame(window, width=480, height=120,borderwidth=1, relief=ctk.RAISED)
playerFrame.grid(row=1,column=0)
fillFrame= ttk.Frame(window, width=120, height=120,borderwidth=1, relief=ctk.RAISED)
fillFrame.grid(row=1,column=1)
createPlaylistButton = ctk.CTkButton(mainFrame, text="Create playlist", command=lambda: print("Playlist Created :0"))
createPlaylistButton.place(relx=0.5, rely=0.90, anchor= ctk.N)
playButton = ctk.CTkButton(playerFrame, text =">", command = lambda: print("Playing"))
playButton.place(relx=0.5, rely=0.5, anchor=ctk.N)
backButton = ctk.CTkButton(playerFrame, text ="<--", command = lambda: print("Going back"))
backButton.place(relx=0.15, rely=0.5, anchor=ctk.N)
forwardButton = ctk.CTkButton(playerFrame, text ="-->", command = lambda: print("Going forward"))
forwardButton.place(relx=0.85, rely=0.5, anchor=ctk.N)


window.mainloop()