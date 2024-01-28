import pygame
import os
import Negocio as negocio
import GUI as gui
import DatabaseManager as database
import DAOs

database.setUp()
app = gui.MusicPlayer()
app.mainloop()