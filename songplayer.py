import pygame
import tkinter as tkr
from tkinter.filedialog import askdirectory
import os



music_player = tkr.Tk()
music_player.geometry("450x350")
music_player.title("My Music Player")

directory = askdirectory() 
os.chdir(directory) 
song_list=os.listdir()
play_list = tkr.Listbox(music_player, font="Helvetica 12 bold", bg='black',selectmode=tkr.SINGLE)

for item in song_list:
    pos = 0
    play_list.insert(pos, item)
    pos += 1
pygame.init()
pygame.mixer.init()

def play():
    pygame.mixer.music.load(play_list.get(tkr.ACTIVE))
    var.set(play_list.get(tkr.ACTIVE))
    pygame.mixer.music.play()
def stop():
    pygame.mixer.music.stop()
def pause():
    pygame.mixer.music.pause()
def unpause():
    pygame.mixer.music.unpause()

Button1=tkr.Button(music_player, width=5, height=3, font="Helvetica 12 bold", text="PLAY",command=play, bg="green", fg="black")
Button2=tkr.Button(music_player, width=5, height=3, font="Helvetica 12 bold", text="STOP",command=stop, bg="red", fg="black")
Button3=tkr.Button(music_player, width=5, height=3, font="Helvetica 12 bold", text="PAUSE",command=pause, bg="yellow", fg="black")
Button4=tkr.Button(music_player, width=5, height=3, font="Helvetica 12 bold", text="UNPAUSE",command=unpause, bg="white", fg="black")


var= tkr.StringVar()
song_title = tkr.Label(music_player, font="Helvetica 12 bold", textvariable=var)

song_title.pack()
Button1.pack(fill="x")
Button2.pack(fill="x")
Button3.pack(fill="x")
Button4.pack(fill="x")

play_list.pack(fill="both", expand="yes")
music_player.mainloop()

