from tkinter import *

from PIL import ImageTk, Image


# import vroom_logic


# from vroom_logic import *


class Gui:

    def __init__(self, window):
        # Image variables

        # self.computer_list = []
        # self.listofdirect = ['up', 'down', 'left', 'right']
        self.player_image = ImageTk.PhotoImage(Image.open("images/mavs.png"))
        self.caller_img = ImageTk.PhotoImage(Image.open("images/durango.png"))
        self.right_image = ImageTk.PhotoImage(Image.open("images/right.png"))
        self.left_image = ImageTk.PhotoImage(Image.open("images/‎left.png"))
        self.up_image = ImageTk.PhotoImage(Image.open("images/‎up.png"))
        self.down_image = ImageTk.PhotoImage(Image.open("images/‎down.png"))
        self.window = window

        # Caller Frame
        self.frame_one = Frame(self.window)
        self.caller_lbl = Label(self.frame_one, image=self.caller_img, width=180)
        self.move_lbl = Label(self.frame_one, text="Durango says: ")
        self.score_lbl = Label(self.frame_one, text="Score: ")
        self.attempt_lbl = Label(self.frame_one, text="Attempt: ")

        # self.input_name = Entry(self.frame_one, width=20)
        # self.input_name.pack(side='right')
        self.caller_lbl.pack(side='left')
        self.score_lbl.pack(side="top")
        self.attempt_lbl.pack(side='top')
        self.move_lbl.pack(side="right")
        self.frame_one.pack()

        self.frame_one2 = Frame(self.window)  # spacer
        self.label_age = Label(self.frame_one2, width=6)
        self.label_age = Label(self.frame_one2, text="---------", width=6)
        self.label_age.pack(side='left')
        self.frame_one2.pack()
        # Age Frame
        self.frame_two = Frame(self.window)
        self.user_lbl = Label(self.frame_two, image=self.player_image, width=180)
        self.user_lbl.pack(side='left')
        self.frame_two.pack()
        # Arrow Keys
        self.direct_button = Frame(self.frame_two)
        self.label_stat = Label(self.direct_button, text="Options")
        """Buttons: Up, Down, Left, Right """
        self.upButton = Button(self.direct_button, text="⇧", state=DISABLED)
        # self.upButton.bind('<KP_Up>', self.upClick)
        self.downButton = Button(self.direct_button, text="⇩", state=DISABLED)
        self.leftButton = Button(self.direct_button, text="⇦", state=DISABLED)
        self.rightButton = Button(self.direct_button, text="⇨", state=DISABLED)
        self.upButton.pack(side="top")
        self.downButton.pack(side="bottom")
        self.leftButton.pack(side="left")
        self.rightButton.pack(side="right")
        self.direct_button.pack()
        # Start Button
        self.start_btn = Frame(self.window)
        self.button_start = Button(self.start_btn, text='▷', width=2)
        self.button_start.grid(row=0, column=2)
        self.start_btn.pack()

        self.reset_btn = Frame(self.window)
        self.button_reset = Button(self.reset_btn, text="↻")
        self.reset_btn.pack()
        self.button_reset.pack()
        # Direction Label
        self.direct = Frame(self.window)
        self.label_direct = Label(self.direct, text='')
        self.label_direct.pack(side='left')
        self.direct.pack()
