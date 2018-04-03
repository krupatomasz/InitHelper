from player import *
from tkinter import *


class InitList:
    def __init__(self, window, canvas, width):
        self.window = window
        self.canvas = canvas
        self.width = width
        self.players = []
        self.bindMouse()

    def draw(self):
        self.canvas.delete('all')
        for i, player in enumerate(self.players):
            y0 = 30*i
            y1 = 30*(i+1)
            if player.isActive:
                self.canvas.create_rectangle(0, y0, self.width, y1, fill='#00ff00')
            if player.focus and not player.isActive:
                self.canvas.create_rectangle(0, y0, self.width, y1, fill='#aaaaaa')
            self.canvas.create_line(0, y1, self.width, y1)
            self.canvas.create_text(20, y1-15, text=player.name, anchor=W)
            if player.conc:
                self.canvas.create_text(self.width-50, y1-15, text='©', fill='red')
            self.canvas.create_text(self.width-10, y1-15, text=player.initiative, anchor=E)

    def add_player(self, player):
        self.players.append(player)
        self.sort()
        self.draw()

    def start(self):
        if not self.players:
            return
        self.sort()
        self.clearFocus()
        self.players[0].activate()
        self.draw()

    def stahp(self):
        for player in self.players:
            player.isActive = False
            player.activeEffects = []
        self.draw()
        self.window.editFrameLogic.draw()

    def next(self):
        self.clearFocus()
        for i, player in enumerate(self.players):
            if player.isActive:
                player.deactivate()
                if i < len(self.players)-1:
                    self.players[i+1].activate()
                else:
                    self.players[0].activate()
                break
        self.draw()

    def sort(self):
        self.players = sorted(self.players, key=lambda x: x.initiative, reverse=True)

    def clearFocus(self):
        for player in self.players:
            if player.focus:
                player.focus = False
                break

    def bindMouse(self):
        def bindL(event):
            y = event.y
            y = int(y/30)
            if y >= len(self.players):
                return
            self.clearFocus()
            self.players[y].setFocus()
            self.draw()
        self.canvas.bind('<Button-1>', bindL)

        def bindM(event):
            y = event.y
            y = int(y/30)
            if y >= len(self.players):
                return
            self.players[y].toggleConc()
            self.draw()
        self.canvas.bind('<Button-2>', bindM)

        def bindR(event):
            y = event.y
            y = int(y/30)
            if y >= len(self.players):
                return
            if self.players[y].focus:
                self.window.editFrame.grid_remove()
            del self.players[y]
            self.draw()
        self.canvas.bind('<Button-3>', bindR)