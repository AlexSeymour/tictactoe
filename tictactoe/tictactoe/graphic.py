from tkinter import *
from grid import grid, get_cases_empty
from tkinter import messagebox
from game import game

def case_callback(case_selected, button):
    if button['text']:
        return
    button['text'] = game.current_player.sign
    case_selected.status = 1
    case_selected.player = game.current_player
    grid_status = grid.check_winner()
    if grid_status:
        messagebox.askquestion("GAGNÉ", "{} A GAGNÉ".format(str.upper(game.current_player.name)))
    game.next_player()



class Application(object):
    """
    Représente la partie du programme, c' est à dire la fenêtre.
    """
    def __init__(self, parent):
        self.parent = parent
        self.cases = []
        self.reset = Button(text="Reset", command=lambda:self.reset_callback())
        self.reset.pack()
        self.frames = []

    def grid(self):
        """
        Initialise la grille en fonction de l' objet grid.grid

        """
        for line in grid.cases.values():
            frame = Frame(self.parent)
            frame.pack(side=BOTTOM)
            self.frames.append(frame)
            for _case in line:
                self.cases.append(self.case(frame, _case))

    def case(self, frame, current_case):
        b = Button(frame)
        b.configure(text="", command=lambda:case_callback(current_case, b))
        b.pack(side=LEFT)
        return b

    def reset_callback(self):

        for button in self.cases:
            button.destroy()

        for frame in self.frames:
            frame.destroy()

        grid.cases = grid.get_cases_empty()
        self.grid()


