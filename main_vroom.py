from vroom_logic import *


def main():
    window = Tk()
    window.title(" Durango Says")
    window.geometry("500x500")
    window.resizable(False, False)

    Logic(window)

    window.mainloop()


if __name__ == '__main__':
    main()
