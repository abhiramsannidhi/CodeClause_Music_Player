import time
from tkinter import *
from tkinter import filedialog
from pygame import mixer
import os
from PIL import Image, ImageTk
import tkinter as tk

root = Tk()
root.title("Music player")
root.geometry("500x700")
root.configure(background="#333333")
root.resizable(False, False)

mixer.init()

def AddMusic():
    path = filedialog.askdirectory()
    if path:
        os.chdir(path)
        songs = os.listdir(path)
        for song in songs:
            if song.endswith(".mp3"):
                Playlist.insert(tk.END, os.path.basename(song))

def PlayMusic():
    current_song_index = Playlist.curselection()[0]
    mixer.music.load(Playlist.get(current_song_index))
    mixer.music.play()

def StopMusic():
    mixer.music.stop()

def PauseMusic():
    mixer.music.pause()

def UnpauseMusic():
    mixer.music.unpause()

def PlayNext():
    current_song_index = Playlist.curselection()[0]
    next_song_index = current_song_index + 1
    if next_song_index < Playlist.size():
        Playlist.selection_clear(current_song_index)
        Playlist.selection_set(next_song_index)
        Playlist.activate(next_song_index)
        Playlist.see(next_song_index)
        mixer.music.load(Playlist.get(next_song_index))
        mixer.music.play()

def PlayPrevious():
    current_song_index = Playlist.curselection()[0]
    previous_song_index = current_song_index - 1
    if previous_song_index >= 0:
        Playlist.selection_clear(current_song_index)
        Playlist.selection_set(previous_song_index)
        Playlist.activate(previous_song_index)
        Playlist.see(previous_song_index)
        mixer.music.load(Playlist.get(previous_song_index))
        mixer.music.play()

framesCnt = 30
frames = [PhotoImage(file='D:/Music player using Python/AA1.gif', format='gif - %i' % i) for i in range(framesCnt)]


def update(ind):
    frame = frames[ind]
    ind += 1
    if ind == framesCnt:
        ind = 0
    label.configure(image=frame)
    root.after(40, update, ind)

label = Label(root)
label.place(x=0, y=0)
root.after(0, update, 0)

image_play = Image.open("D:/Music player using Python/Play.png")
image_play = image_play.resize((30, 30), Image.LANCZOS)
ButtonPlay = ImageTk.PhotoImage(image_play)
Button(root, image=ButtonPlay, bg="#FFFFFF", bd=0, height=30, width=30, command=PlayMusic).place(x=10, y=487)

image_stop = Image.open("D:/Music player using Python/Stop.png")
image_stop = image_stop.resize((30, 30), Image.LANCZOS)
ButtonStop = ImageTk.PhotoImage(image_stop)
Button(root, image=ButtonStop, bg="#FFFFFF", bd=0, height=30, width=30, command=StopMusic).place(x=50, y=487)

image_volume = Image.open("D:/Music player using Python/Volume.png")
image_volume = image_volume.resize((30, 30), Image.LANCZOS)
Buttonvolume = ImageTk.PhotoImage(image_volume)
Button(root, image=Buttonvolume, bg="#000000", bd=0, height=30, width=30, command=UnpauseMusic).place(x=90, y=487)

image_pause = Image.open("D:/Music player using Python/Pause.png")
image_pause = image_pause.resize((30, 30), Image.LANCZOS)
ButtonPause = ImageTk.PhotoImage(image_pause)
Button(root, image=ButtonPause, bg="#FFFFFF", bd=0, height=30, width=30, command=PauseMusic).place(x=130, y=487)

image_previous = Image.open("D:/Music player using Python/Previous.png")
image_previous = image_previous.resize((30, 30), Image.LANCZOS)
ButtonPrevious = ImageTk.PhotoImage(image_previous)
Button(root, image=ButtonPrevious, bg="#FFFFFF", bd=0, height=30, width=30, command=PlayPrevious).place(x=170, y=487)

image_next = Image.open("D:/Music player using Python/Next.png")
image_next = image_next.resize((30, 30), Image.LANCZOS)
ButtonNext = ImageTk.PhotoImage(image_next)
Button(root, image=ButtonNext, bg="#FFFFFF", bd=0, height=30, width=30, command=PlayNext).place(x=210, y=487)

Menu = PhotoImage(file="D:/Music player using Python/menu.png")
Label(root, image=Menu).place(x=0, y=580, width=485, height=120)

Frame_Music = Frame(root, bd=2, relief=RIDGE)
Frame_Music.place(x=0, y=585, width=485, height=100)

Button(root, text="Browse Music", width=59, height=1, font=("calibri", 12, "bold"), fg="Black", bg="#FFFFFF", command=AddMusic).place(x=0, y=550)

Scroll = Scrollbar(Frame_Music)
Playlist = Listbox(Frame_Music, width=100, font=("Times new roman", 10), bg="#333333", fg="grey", selectbackground="lightblue", cursor="hand2", bd=0, yscrollcommand=Scroll.set)
Scroll.config(command=Playlist.yview)
Scroll.pack(side=RIGHT, fill=Y)
Playlist.pack(side=RIGHT, fill=BOTH)

root.mainloop()

