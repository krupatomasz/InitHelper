from tkinter import *

class EditFrame:
    def __init__(self, window, frame, width):
        self.window = window
        self.frame = frame
        self.width = width
        self.player = None
        self.name = Label(self.frame)
        self.name.grid(row=0, column=0, columnspan=3)
        self.init = Label(self.frame, text='Initiative')
        self.init.grid(row=1, column=0)
        self.initEntry = Entry(self.frame)
        self.initEntry.grid(row=1, column=1)
        self.initEntry.bind('<Return>', lambda event: self.alterInit())
        self.changeInit = Button(self.frame, text='Change', command=self.alterInit)
        self.changeInit.grid(row=1, column=2)

        self.effectLabel = Label(self.frame, text='Effect')
        self.effectLabel.grid(row=2, column=0)
        self.effectEntry = Entry(self.frame)
        self.effectEntry.grid(row=2, column=1)
        self.effectEntry.bind('<Return>', lambda event: self.addEffect())
        self.effectButton = Button(self.frame, text='Add', command=self.addEffect)
        self.effectButton.grid(row=2, column=2)

        self.effectList = Canvas(self.frame, height=400)
        self.effectList.grid(row=3, column=0, columnspan=3)
        self.delf()

    def draw(self):
        if not self.player:
            return
        self.name.config(text=self.player.name + ' ' + str(self.player.initiative))
        self.initEntry.delete(0, END)
        self.effectEntry.delete(0, END)
        self.effectList.delete('all')
        for i, effect in enumerate(self.player.activeEffects):
            y = 20*(i+1)
            self.effectList.create_text(20, y-10, text=effect, anchor=W)
            self.effectList.create_line(0, 20*(i+1), 200, 20*(i+1))

    def alterInit(self):
        init = self.initEntry.get()
        self.initEntry.delete(0, END)
        if not init or not init.isdigit():
            return
        self.player.initiative = int(init)
        self.draw()
        self.window.initList.draw()

    def addEffect(self):
        name = self.effectEntry.get()
        self.effectEntry.delete(0, END)
        if not name:
            return
        self.player.activeEffects.append(name)
        self.draw()

    def delf(self):
        def bindR(event):
            y = event.y
            print(y)
            y = int(y/20)
            if y >= len(self.player.activeEffects):
                return
            del self.player.activeEffects[y]
            self.draw()
        self.effectList.bind('<Button-3>', bindR)
