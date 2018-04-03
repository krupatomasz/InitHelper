from editPlayer import *
from initList import *


class Window:

    def __init__(self):
        self.master = Tk()
        self.master.title('Hello there')

        width = 200

        initListCanvas = Canvas(self.master, width=width, height=500)
        initListCanvas.grid(row=0, column=0, rowspan=50, columnspan=3)
        self.initList = InitList(self, initListCanvas, 200)
        self.initList.draw()

        self.addAddingPlayers()
        self.addEditFrame()
        self.add_battle_control_buttons()

        self.isBattle = False
        self.playerOnFocus = None

    def task(self):
        self.master.after(1000, self.task)

    def mainloop(self):
        self.master.after(1000, self.task)
        self.master.mainloop()

    def addAddingPlayers(self):
        def add_player_button_function():
            name = self.addPlayerTextbox.get()
            init = self.initTextbox.get()
            if name == '' or init == '' or not init.isdigit():
                return
            player = Player(self, name, init)
            self.initList.add_player(player)
            self.addPlayerTextbox.delete(0, END)
            self.initTextbox.delete(0, END)
            self.addPlayerTextbox.focus()

        nameLabel = Label(self.master, text='Name: ')
        nameLabel.grid(row=50, column=0)

        self.addPlayerTextbox = Entry(self.master)
        self.addPlayerTextbox.grid(row=50, column=1, columnspan=2)

        initLabel = Label(self.master, text='Initiative: ')
        initLabel.grid(row=50, column=3)

        self.initTextbox = Entry(self.master)
        self.initTextbox.grid(row=50, column=4)

        self.addPlayerTextbox.bind('<Return>', lambda event: add_player_button_function())
        self.initTextbox.bind('<Return>', lambda event: add_player_button_function())

        addPlayerButton = Button(self.master, text='Add', command=add_player_button_function)
        addPlayerButton.grid(row=50, column=5)

    def add_battle_control_buttons(self):
        def fight():
            if not self.initList.players:
                return
            self.isBattle = True
            self.initList.start()
            startButton.grid_remove()
            stahpButton.grid()
            self.nextButton.grid()

        def stahp():
            self.isBattle = False
            self.initList.stahp()
            stahpButton.grid_remove()
            self.nextButton.grid_remove()
            startButton.grid()

        def next():
            self.initList.sort()
            self.initList.next()

        startButton = Button(self.master, text='INTO BATTLE', command=fight, bg='#00ff00', width=20)
        startButton.grid(row=0, column=3, columnspan=3)

        stahpButton = Button(self.master, text='HOL\' UP', command=stahp, bg='#ee5500', width=20)
        stahpButton.grid(row=1, column=3, columnspan=3)
        stahpButton.grid_remove()

        self.nextButton = Button(self.master, text='NEXT', command=next, bg='#00aaff', width=20)
        self.nextButton.grid(row=0, column=3, columnspan=3)
        self.nextButton.grid_remove()

        self.master.bind('<space>', lambda event: next())

    def addEditFrame(self):
        self.editFrame = Frame(self.master, width=100, height=400)
        self.editFrame.grid(row=5, column=3, rowspan=10, columnspan=3)
        self.editFrame.grid_remove()
        self.editFrameLogic = EditFrame(self, self.editFrame, 200)
        self.editFrameLogic.draw()

    def activatePlayerMenu(self, player):
        self.playerOnFocus = player
        self.editFrame.grid()
        self.editFrameLogic.player = player
        self.editFrameLogic.draw()
