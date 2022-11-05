# importing pygame library
import pygame
# importing system from os
from os import system
# importing graphic library
from tkinter import *
# application module
def Application(self, master=None):
    pygame.init()
    # play/stop function
    def Play():
        if self.playing == False:
            self.playingLabel['text'] = 'Tocando: '
            self.playing = True
            pygame.mixer.music.load('song.mp3')
            pygame.mixer.music.play()
            pygame.event.wait()
            self.play['text'] = 'Parar'
        else:
            self.playingLabel['text'] = 'Tocar: '
            self.playing = False
            pygame.mixer.music.load('song.mp3')
            pygame.mixer.music.stop()
            self.play['text'] = 'Tocar'
    system('clear') # clean terminal at program starts
    # playing status
    self.playing = False
    # top frame
    self.top = Frame(master)
    # display widget
    self.display = Frame(self.top)
    # playing label
    self.playingLabel = Label(self.display, height=4, font=('', 18, 'bold'), text='Tocar: ')
    self.playingLabel.pack(side=LEFT)
    # song name label
    self.songName = Label(self.display, fg='purple', height=4, font=('', 13, 'bold'), text='All I am\nby Dyalla')
    self.songName.pack(side=LEFT)
    self.display.pack()
    # exit button
    self.exit = Button(self.top, command=self.top.quit, text='Sair')
    self.exit.pack(side=LEFT, padx=(0, 2))
    # play/stop button
    self.play = Button(self.top, command=Play, bg='#d02a2a', text='Tocar')
    self.play.pack(side=LEFT, padx=(2, 0))
    self.top.pack()
# application setup
root = Tk()
root.title('MP3Player')
root.geometry('400x200')
# application start
Application(root)
# mainloop
root.mainloop()
