from random import randint
from tkinter import *

from Solresol.Components.Grp_DB.C0_grq_db_v1 import questions_list



def font_set(font_size=12, is_fancy_font=0, is_bold=0, is_italic=0):
    """
    creates font in a very simple way
    :param is_fancy_font: changes font to georgia if set to <1> (default <0>)
    :param font_size: sets font size to chosen number (default <12>)
    :param is_bold: makes font bold if set to <1> (default <0>)
    :param is_italic: makes font italic if set to <1> (default <0>)
    :return:
    """

    font = ["Arial", font_size]

    if is_fancy_font == 1:
        font[0] = "Georgia"

    if is_bold == 1:
        font.append("bold")

    if is_italic == 1:
        font.append("italic")

    return tuple(font)


class StartMenu:
    """
    Runs the main start menu
    """

    def __init__(self):
        """
        start menu GUI
        """

        # Configure row and column weights for centering
        root.grid_columnconfigure(0, weight=1)  # Column left of the widget
        root.grid_columnconfigure(2, weight=1)  # Column right of the widget

        self.all_calculations_list = []

        self.temp_frame = Frame(padx=10, pady=10)
        self.temp_frame.grid(row=1, column=1)

        self.temp_heading = Label(self.temp_frame, text="\nSolresol  Sidosi\nSolmilami",
                                  font=font_set(24, 1, 1))

        self.temp_heading.grid(row=0, pady=5)

        # line seperator (also insures correct center alignment)
        self.line = Label(self.temp_frame, text="────────────────────",
                          font=font_set(24, 1, 1), justify="center")
        self.line.grid(row=1)

        self.heading_english = Label(self.temp_frame, text="(language learning program)", font=font_set(10), foreground="#555555")
        self.heading_english.place(relx=0.5, rely=0.5, anchor="center", y=-119)

        heading_note = "Welcome to the Solresol learning app. \n please select an option below \n"
        self.temp_instructions = Label(self.temp_frame, text=heading_note, width=40, justify="center",
                                       font=font_set(is_fancy_font=1))
        self.temp_instructions.grid(row=2)

        # convertion help history and errors
        self.button_frame = Frame(self.temp_frame)
        self.button_frame.grid(row=5)

        buttons_list = [
            ["Familiar - Written Form", "#3377BB", "#115599", self.to_familiar],
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


    def to_familiar(self):
        FQMenu()
        root.withdraw()



class FQMenu:

    def __init__(self):
        """
        Questions area for the familiar grade questions
        """

        self.f_q_box = Toplevel()
        self.f_q_box.geometry("1280x720+310+120")

        # Configure row and column weights for centering
        self.f_q_box.grid_columnconfigure(0, weight=1)  # Column left of the widget
        self.f_q_box.grid_columnconfigure(2, weight=1)  # Column right of the widget

        self.f_q_box.protocol('WM_DELETE_WINDOW', root.destroy)

        self.all_calculations_list = []

        self.f_q_frame = Frame(self.f_q_box, padx=10, pady=10)
        self.f_q_frame.grid(row=1, column=1)

        self.temp_heading = Label(self.f_q_frame, text="\n Resolsila  Sisolsi ",
                                  font=font_set(24, 1, 1))

        self.temp_heading.grid(row=0, pady=5)

        # line seperator (also insures correct center alignment)
        self.line = Label(self.f_q_frame, text="────────────────────",
                          font=font_set(24, 1, 1), justify="center")
        self.line.grid(row=1, padx=400)

        self.heading_english = Label(self.f_q_box, text="(familiar questions)", font=font_set(10),
                                     justify="center", foreground="#555555")
        self.heading_english.place(relx=0.5, rely=0.5, anchor="center", y=-246)

        heading_note = " ### In this section you will learn ### \n Familiar and simple, one syllable solresol, \n using writen english lettering "
        self.temp_instructions = Label(self.f_q_frame, text=heading_note, width=40, justify="center",
                                       font=font_set(is_fancy_font=1))
        self.temp_instructions.grid(row=2)

        self.question_frame = Frame(self.f_q_frame)
        self.question_frame.grid(row=3)

        self.new_question()

    def new_question(self):
        # var setup
        current_question = 2

        def make_widget(widget):

            for count, item in enumerate(widget):
                if item[0] == "l":
                    widget_made = Label(self.question_frame, wraplength=500, text=item[1], justify="left",
                                    font=font_set(16))
                    widget_made.grid(row=count, pady=item[2])

                elif item[0] == "b":
                        widget_made = Button(self.question_frame, text=item[1], bg=item[2], height=2, fg="#EEEEEE",
                                         font=font_set(is_bold=1), width=25, activeforeground="#333333",
                                         activebackground=item[3], command=item[4])
                        widget_made.grid(row=count, pady=item[5])
        

                elif item[0] == "i":
                    img = PhotoImage(file="../../Images/"+item[1], width=item[2], height=item[3])
                    widget_made = Label(self.question_frame, image=img)
                    widget_made.grid(row=count, pady=item[4])

        make_widget( questions_list[0][randint(0, int(len(questions_list[0]))) - 1] )


        # Initial start screen
        if current_question == 1:
            starting_text = ("\nIn Solresol there are only 7 letters, which come together to create around 300 words,"
                             " below 4 syllables. these letters are the common scale of.\n\n")
            tmp_label_1 = Label(self.question_frame, wraplength=500, text=starting_text, justify="left",
                                font=font_set(16))
            tmp_label_1.grid(row=3)
            tmp_label_1_colours = [
                ["Do,", "#E33", 0],
                ["Re,", "#F80", 1],
                ["Mi,", "#DB0", 2],
                ["Fa,", "#0A0", 3],
                ["Sol,", "#3C9", 4],
                ["La,", "#06F", 5.15],
                ["Si.", "#609", 6.15]
            ]
            for i in range(0, len(tmp_label_1_colours)):
                tmp_label_1_1 = Label(self.question_frame, wraplength=500, text=tmp_label_1_colours[i][0],
                                      justify="left", font=font_set(16), foreground=tmp_label_1_colours[i][1],
                                      background="#EEE")
                tmp_label_1_1.place(x=(40 * tmp_label_1_colours[i][2]), y=96)



# main routine

if __name__ == "__main__":
    root = Tk()

    # Set default screen size position and is resizable
    root.title("Solresol Sidosi Solmilami")
    root.geometry("1280x720+310+120")
    root.resizable(width=True, height=True)

    # Bind the F11 key to the toggle_fullscreen function
    def toggle_fullscreen(event=None):
        state = not root.attributes("-fullscreen")
        root.attributes("-fullscreen", state)
    root.bind("<F11>", toggle_fullscreen)

    # Start application
    root.update_idletasks()
    StartMenu()
    root.mainloop()
