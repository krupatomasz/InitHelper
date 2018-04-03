class Player:
    def __init__(self, window, name, init=0):
        self.window = window
        self.name = name
        self.isActive = False
        self.focus = False
        self.conc = False
        self.activeEffects = []
        self.initiative = int(init)

    def activate(self):
        self.isActive = True
        self.setFocus()

    def deactivate(self):
        self.isActive = False
        self.focus = False

    def setFocus(self):
        self.focus = True
        self.window.activatePlayerMenu(self)

    def toggleConc(self):
        self.conc = not self.conc