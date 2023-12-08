from vroom_gui import *
import time, os, random, sys
from tkinter import messagebox


class Logic(Gui):
    def __init__(self, window):
        super().__init__(window)
        self.upButton.config(command=self.upClick)
        self.downButton.config(command=self.downClick)
        self.leftButton.config(command=self.leftClick)
        self.rightButton.config(command=self.rightClick)
        self.button_start.config(command=self.start)
        self.button_reset.config(command=self.reset)

        self.player_list = []
        self.computer_list = []
        self.DIRECTIONS = ["up", "down", "left", "right"]

        # self.MOVE_LENGTH = random.randint(1, 2)
        self.MOVE_LENGTH = 2
        self.startmovenum = 2

        self.WAIT_TIME = 1
        self.SCORE = 0
        self.ATTEMPT = 0
        self.currentTurn = 'cpu'
        self.isPlayerTurn = False
        self.isgameStarted = False

    def rightClick(self) -> list:
        """Function is ran when the right button is clicked, user image is updated, 'right' is added to
        player's move list and 1 is added to attempts"""
        self.user_lbl["image"] = self.right_image
        self.player_list.append("right")
        self.ATTEMPT += 1
        self.attempt_lbl.config(text=f'Attempt: {self.ATTEMPT}')
        # self.attempt_lbl.after(500, self.pdefault_state())
        # self.user_lbl.update()
        # self.user_lbl.update_idletasks()
        return self.player_list

    def leftClick(self) -> list:
        """Function is ran when the left button is clicked, user image is updated, 'left' is added to
                player's move list and 1 is added to attempts"""
        self.user_lbl["image"] = self.left_image
        self.player_list.append("left")
        self.ATTEMPT += 1
        # self.attempt_lbl.config(text=f'Attempt: {self.ATTEMPT}')
        # self.attempt_lbl.after(500, self.pdefault_state())
        # self.attempt_lbl.update()
        # self.attempt_lbl.update_idletasks()

        return self.player_list

    def upClick(self) -> list:
        """Function is ran when the up button is clicked, user image is updated, 'up' is added to
                player's move list and 1 is added to attempts"""
        self.user_lbl["image"] = self.up_image
        self.player_list.append("up")
        self.ATTEMPT += 1
        self.attempt_lbl.config(text=f'Attempt: {self.ATTEMPT}')
        # self.attempt_lbl.after(500, self.pdefault_state())
        # self.user_lbl.update()
        # self.user_lbl.update_idletasks()
        return self.player_list

    def downClick(self) -> list:
        """Function is ran when the down button is clicked, user image is updated, 'down' is added to
                player's move list and 1 is added to attempts"""
        self.user_lbl["image"] = self.down_image

        self.player_list.append("down")
        self.ATTEMPT += 1
        self.attempt_lbl.config(text=f'Attempt: {self.ATTEMPT}')
        # self.attempt_lbl.after(500, self.pdefault_state())
        # self.attempt_lbl.update()
        # self.attempt_lbl.update_idletasks()
        return self.player_list

    def game(self, startmovenum: int):
        """If the length of computer's list is not equal to MOVE_LENGTH, Moves for durango (cpu) will be generated,
        image is updated to match the move, and is then added to durango's move list.
        If player got a point, MOVE_LENGTH increase by 1; but; previous move(s) are still the same."""

        global move
        if len(self.computer_list) != self.MOVE_LENGTH:
            self.isPlayerTurn = False
            # show move for computer list
        for m in self.computer_list:
            print(m)
            self.show_moves(m)
            self.caller_lbl.update()
            self.caller_lbl.update_idletasks()
            time.sleep(self.WAIT_TIME)
        for i in range(startmovenum):
            # need to revert back to default image before next call of move
            if len(self.computer_list) < self.MOVE_LENGTH:
                move = random.choice(self.DIRECTIONS)
            self.caller_lbl.after(300,
                                  self.cdefault_state())  # waits # of seconds before reverting back to default image.
            self.caller_lbl.update()
            self.caller_lbl.update_idletasks()
            self.upButton.config(state=DISABLED)
            self.downButton.config(state=DISABLED)
            self.leftButton.config(state=DISABLED)
            self.rightButton.config(state=DISABLED)
            time.sleep(self.WAIT_TIME)  # delay between moves
            self.show_moves(move)
            self.caller_lbl.update()
            self.caller_lbl.update_idletasks()
            print(move)
            self.computer_list.append(move)
        self.caller_lbl.after(1000, self.cdefault_state())  # waits # of seconds before reverting back to default image.
        self.caller_lbl.update()
        self.caller_lbl.update_idletasks()

        self.move_lbl.config(text="Your Turn")
        self.caller_lbl["image"] = self.caller_img
        time.sleep(2)
        self.isPlayerTurn = True
        self.upButton.config(state=NORMAL)
        self.downButton.config(state=NORMAL)
        self.leftButton.config(state=NORMAL)
        self.rightButton.config(state=NORMAL)
        self.playerTurn()

    def show_moves(self, move: list):
        """Gets the element of move and compares it to one of the four directions, changing the caller's image and text"""
        self.caller_lbl.config(text=" ")
        # move = range(self.computer_list)
        if move == "up":
            self.caller_lbl["image"] = self.up_image
            self.move_lbl["text"] = f'Durango says: {move}'
            # print('UP')

        elif move == "down":  # down
            self.caller_lbl["image"] = self.down_image
            self.move_lbl["text"] = f'Durango says: {move}'
            # print('DOWN')

        elif move == "left":  # left
            self.caller_lbl["image"] = self.left_image
            self.move_lbl["text"] = f'Durango says: {move}'
            # print('LEFT')

        elif move == "right":  # right
            self.caller_lbl["image"] = self.right_image
            self.move_lbl["text"] = f'Durango says: {move}'
            # print('RIGHT')

    def cdefault_state(self):
        """Default image and text for the cpu 'caller'. """
        self.caller_lbl.config(image=self.caller_img)
        self.move_lbl.config(text=' ')

    def pdefault_state(self):
        """Default image for user"""
        self.user_lbl["image"] = self.player_image
        # self.move_lbl.config(text=f'Durango says: ')

    def reset(self):
        """
            This function restarts the Python program when called.
            """
        print("Reset Button pressed")
        python = sys.executable
        os.execl(python, python, *sys.argv)

    def start(self):
        """Once the User press ok on the message box or press the Return key,the direction window will close."""
        messagebox.showerror(message="Directions: Watch the different directions Durango prints.\n\nClick the arrows "
                                     "according to the order.\n\n"
                                     "Every correct turn a score will be added and the number of directions will increase by 1\n"
                                     "\nIf player loses, the program will close.")

        self.button_start.config(state=DISABLED)
        self.button_reset.config(state=NORMAL)
        self.isgameStarted = True
        self.game(self.startmovenum)

    def playerTurn(self):
        """handles user input and compares to durango (cpu list)"""
        self.caller_lbl.after(100, self.playerTurn)
        # self.user_lbl.after(2000, self.pdefault_state)
        if len(self.player_list) == len(self.computer_list):
            # print("list are equal")
            self.upButton.config(state=DISABLED)
            self.downButton.config(state=DISABLED)
            self.leftButton.config(state=DISABLED)
            self.rightButton.config(state=DISABLED)
            self.scoreChecker()
            self.eachTurn()

    def eachTurn(self):
        """After each 'turn' of the user, the caller and user's image are reverted to its initial
        image and player's move list is cleared."""
        self.cdefault_state()
        self.pdefault_state()
        self.player_list.clear()

    def scoreChecker(self):
        """Will get the length of both lists, if equal, then it will go into each list indexes and compare the
        directions, if matches, the function player_win is executed. If not, the function player_lose is executed."""
        try:
            if len(self.player_list) == len(self.computer_list):
                # self.upButton["state"] = DISABLED
                for i in range(len(self.player_list)):
                    if self.player_list[i] != self.computer_list[i]:
                        self.player_lose()
                self.player_win()
                print(self.computer_list)
        except IndexError:
            pass

    def player_lose(self):
        """Function prints text to terminal and quits the program."""
        print("Incorrect")
        # self.button_start.config(text="Retry")
        # self.eachTurn()
        self.window(quit())

    def player_win(self):
        """Prints text in terminal, 1 point is added to score, durango's caller list number
        increase by 1, score is updated. Instead of calling two moves, initially, only one additional move will be created.
        """
        print("Correct")
        self.SCORE += 1
        self.MOVE_LENGTH += 1
        self.score_lbl.config(text=f'Score: {self.SCORE}')
        self.eachTurn()
        self.game(1)
