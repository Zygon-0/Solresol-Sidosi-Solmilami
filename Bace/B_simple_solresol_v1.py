# Imported packages
from tkinter import *


# globally usable functions
def font_set(font_size=12, is_fancy_font=0, is_bold=0, is_italic=0):
    """
    creates font in a very simple way
    :param is_fancy_font: changes font to gorgia if set to <1>
    :param font_size: sets font size to chosen number (default <12>)
    :param is_bold: makes font bold if set to <1>
    :param is_italic: makes font italic if set to <1>
    """

    font = ["Arial", font_size]

    if is_fancy_font == 1:
        font.pop(0)
        font.append("Georgia")
        font.reverse()

    if is_bold == 1:
        font.append("bold")

    if is_italic == 1:
        font.append("italic")

    return tuple(font)


class Start_menu:
    """
    Runs the main start menu
    """

    def __init__(self):
        """
        start menu GUI
        """

        self.all_calculations_list = []

        self.temp_frame = Frame(padx=10, pady=10)
        self.temp_frame.grid()

        self.temp_heading = Label(self.temp_frame, text="\n Solresol Sidosi\n Solmilami", font=font_set(24, 1, 1))

        self.temp_heading.grid(row=0)

        # line seperator (also insures correct center alignment)
        self.line = Label(self.temp_frame, text="────────────────────",
                          font=font_set(24, 1, 1), justify="center")
        self.line.grid(row=1, padx=400)

        heading_note = "Welcome to the Solresol learning app. \n please select an option below \n"
        self.temp_instructions = Label(self.temp_frame, text=heading_note, width=40, justify="center",
                                       font=font_set(is_fancy_font=1))
        self.temp_instructions.grid(row=2)

        # convertion help history and errors
        self.button_frame = Frame(self.temp_frame)
        self.button_frame.grid(row=5)

        buttons_list = [
            ["Familiar - Written Form", "#3377BB", "#115599", None],
            ["Transitional - Musical Notation", "#229922", "#007700", None],
            ["Tough - Line Form", "#CC6600", "#aa4400", None],
            ["Extreme - Audio Form", "#990000", "#770000", None]
        ]

        # list to hold buttons once they have been made
        self.button_ref_list = []

        for count, item in enumerate(buttons_list):
            self.make_button = Button(self.button_frame, text=item[0], bg=item[1], height=2, activebackground=item[2],
                                      fg="#EEEEEE", font=font_set(is_bold=1), width=25, activeforeground="#333333",
                                      command=item[3])
            self.make_button.grid(row=count, padx=5, pady=10)

            self.button_ref_list.append(self.make_button)







# main routine

if __name__ == "__main__":
    root = Tk()
    root.title("Solresol Sidosi Solmilami")
    root.geometry("1280x720")
    Start_menu()
    root.mainloop()
