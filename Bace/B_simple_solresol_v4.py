import random
import tkinter
from random import randint
from tkinter import *
from functools import partial
from Components.Grp_DB.C_grq_db_v4 import questions_list

# global vars
root_geometry = ""
current_question = 0
current_streak = 0
best_streak = 0
questions_diff_group = 0
placed_widgets = []
temp_instructions_list = []

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
            ["Familiar", "#3377BB", "#115599", partial(self.to_familiar, 0, 0)],
            ["Transitional", "#229922", "#007700", partial(self.to_familiar, 16, 1)],
            ["Tough", "#CC6600", "#aa4400", partial(self.to_familiar, 32, 2)],
            ["Extreme", "#990000", "#770000", partial(self.to_familiar, 48, 3)]
        ]

        # list to hold buttons once they have been made
        self.button_ref_list = []

        for count, item in enumerate(buttons_list):
            self.make_button = Button(self.button_frame, text=item[0], bg=item[1], height=2, activebackground=item[2],
                                      fg="#EEEEEE", font=font_set(is_bold=1), width=25, activeforeground="#333333",
                                      command=item[3])
            self.make_button.grid(row=count, padx=5, pady=10)

            self.button_ref_list.append(self.make_button)


    def to_familiar(self, int_start, dif_start):
        global current_question
        global questions_diff_group
        global root_geometry
        current_question = int_start
        questions_diff_group = dif_start
        root.update()
        root_geometry = root.winfo_geometry()
        root.attributes("-fullscreen")
        FQMenu()
        root.withdraw()



class FQMenu:

    def __init__(self):
        """
        Area for the different grades of questions
        """
        self.starting_question = current_question
        self.starting_text = ""
        self.f_q_box = Toplevel()
        global root_geometry
        self.f_q_box.geometry(root_geometry)
        self.f_q_box.minsize(486, 600)
        self.f_q_box.attributes("-fullscreen", root.attributes("-fullscreen"))

        # Bind the F11 key to the toggle_fullscreen function
        def toggle_fullscreen(event=None):
            state = not self.f_q_box.attributes("-fullscreen")
            self.f_q_box.attributes("-fullscreen", state)
        self.f_q_box.bind("<F11>", toggle_fullscreen)

        self.f_q_box.resizable(width=True, height=True)

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
        self.heading_english.place(relx=0.5, rely=0, anchor="n", y=103)

        heading_note = " ### In this section you will learn ### \n The \"familiar\" and simple order of the letters in Solresol, and what all the syllable\'s are."
        self.temp_instructions = Label(self.f_q_frame, text=heading_note, width=40, justify="center",
                                       font=font_set(is_fancy_font=1), wraplength=350)
        self.temp_instructions.grid(row=2)

        self.question_frame = Frame(self.f_q_frame)
        self.question_frame.grid(row=3)

        self.questions_options = []

        self.new_question(self.questions_options)






    def new_question(self, questions_options):
        # var setup
        global current_question
        global temp_instructions_list
        current_question += 1
        last_question = None
        if questions_options:
            questions_options.clear()
        for item in self.question_frame.winfo_children():
            item.grid_forget()
        for item in self.question_frame.winfo_children():
            try:
                item.place_forget()
            except AttributeError:
                pass
        for item in self.f_q_frame.winfo_children():
            try:
                item.place_forget()
            except AttributeError:
                pass

        def make_widget(widget):
            for count, item in enumerate(widget):
                if item[0] == "l":
                    widget_made = Label(self.question_frame, wraplength=500, text=item[1], justify="left",
                                    font=font_set(16))
                    questions_options.append(widget_made)

                elif item[0] == "b":
                    widget_made = Button(self.question_frame, text=item[1], bg=item[2], height=2, fg="#EEEEEE",
                                     font=font_set(is_bold=1), width=25, activeforeground="#333333",
                                     activebackground=item[3], command=partial(wrong_button_clicked, str(item[7])))
                    global temp_instructions_list
                    questions_options.append(widget_made)
                    temp_instructions_list.append(item[7])

            for c, i in enumerate(widget):
                if len(i) > 3:
                    print("i", i[6])
                    if i[6] == 1:
                        global current_streak
                        questions_options[c].config(command=lambda: correct_button_clicked())
            print("")
            questions_options[0].grid(row=0, pady=5)
            questions_options.pop(0)
            random.shuffle(questions_options)
            for count, item in enumerate(questions_options):
                item.grid(row=count+1, pady=5)

            self.help_button = Button(self.f_q_frame, text="     ℹ️", padx=0, pady=0, font=("Arial", 30),
                                highlightthickness=0, bd=0, fg="#EC0",
                                command=lambda: self.to_help())
            self.help_button.place(relx=0.5, x=-220, y=75, width=20, height=40)

        def keep_practicing():
            global current_question
            global questions_diff_group
            current_question -= 17
            questions_diff_group -= 1
            self.new_question(questions_options)

        def correct_button_clicked():
            global best_streak
            global current_streak
            current_streak += 1
            if current_streak > best_streak:
                best_streak = current_streak
            self.new_question(questions_options)

        def wrong_button_clicked(error_text, button_text):
            self.temp_instructions.config(text=error_text, fg="#E33")
            widget_text = ""
            for widget in questions_list[questions_diff_group][question]:
                if len(widget) > 3:
                    if widget[7] == error_text:
                        widget_text = widget[1]
            global best_streak
            global current_streak
            if current_streak > best_streak:
                best_streak = current_streak
            current_streak = 0

            for item in questions_options:
                if item.cget("text") == widget_text:
                    item.config(state=DISABLED)


        if current_question > 17:
            self.temp_instructions.config(text=f"Current Question: {current_question - self.starting_question - 17}",
                                          fg="#000")
        elif current_question > 1:
            self.temp_instructions.config(text=f"Current Question: {current_question - self.starting_question - 1}",
                                          fg="#000")


        global questions_diff_group
        # diff # starting info screen
        if current_question == 1:
            self.starting_text = ("\nIn Solresol there are only 7 letters, which come together to create around 300 words,"
                             " below 4 syllables. these letters are the common scale of.\nDo, Re, Mi, Fa, Sol, La, Si.\n")
            tmp_label_1 = Label(self.question_frame, wraplength=500, text=self.starting_text, justify="left",
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
                tmp_label_1_1.place(x=(37 * tmp_label_1_colours[i][2]), y=96)

            continue_button = Button(self.question_frame, text="Continue", bg="#0A0", height=2, fg="#EEEEEE",
                                 font=font_set(is_bold=1), width=25, activeforeground="#333333",
                                 activebackground="#070", command=lambda: self.new_question(questions_options))
            continue_button.grid(row=10)

        elif current_question == 17:
            if self.starting_question == 0:
                self.starting_question += 1
            else:
                self.starting_question -= 16
            self.temp_instructions.config(text="### In this section you will learn ###\nThe \"transitional\","
                                               " and mildly difficult, definitions of all 7 of the 1 syllable"
                                               " Solresol word\'s")
            self.starting_text = ("\nNow that you have a bit of a grasp on the letters in Solresol, "
                             "lets get you familiar with each syllables word definitions."
                             "\nThe definitions are as follows"
                             "\n\n ●   Do is   \"No, not, nor\""
                             "\n ●   Re is   \"And\""
                             "\n ●   Mi is   \"Or\""
                             "\n ●   Fa is   \"At, to\""
                             "\n ●   Sol is  \"If\""
                             "\n ●   la  is  \"The\""
                             "\n ●   Si is   \"Yes, willingly\""
                             "\n\n")
            tmp_label_1 = Label(self.question_frame, wraplength=500, text=self.starting_text, justify="left",
                                font=font_set(16))
            tmp_label_1.grid(row=3)
            tmp_label_1_colours = [
                ["Do", "#E33", 0],
                ["Re", "#F80", 1],
                ["Mi", "#DB0", 2],
                ["Fa", "#0A0", 3],
                ["Sol", "#3C9", 4],
                ["La", "#06F", 5],
                ["Si", "#609", 6]
            ]
            for i in range(0, len(tmp_label_1_colours)):
                tmp_label_1_1 = Label(self.question_frame, wraplength=500, text=tmp_label_1_colours[i][0],
                                      justify="left", font=font_set(16), foreground=tmp_label_1_colours[i][1],
                                      background="#EEE")
                tmp_label_1_1.place(x=34, y=144 + (23.9 * tmp_label_1_colours[i][2]))

            continue_button = Button(self.question_frame, text="Continue", bg="#0A0", height=2, fg="#EEEEEE",
                                     font=font_set(is_bold=1), width=25, activeforeground="#333333",
                                     activebackground="#070", command=lambda: self.new_question(questions_options))
            continue_button.grid(row=4)

            back_button = Button(self.question_frame, text="Practice longer", bg="#DB0", height=1, fg="#EEEEEE",
                                     font=font_set(is_bold=1), width=25, activeforeground="#333333",
                                     activebackground="#070", command=lambda: keep_practicing())
            back_button.grid(row=5)

            self.heading_english.config(text="(between questions)")
            self.temp_heading.config(text="\n Mimiresol  Sisolsi ")

        elif current_question == 33:
            if self.starting_question == 16 or self.starting_question == 0:
                self.starting_question += 1
            else:
                self.starting_question -= 16

            self.temp_instructions.config(text="### In this section you will learn ###\nThe \"Tough\","
                                               " and relatively difficult, definitions of 13 of the 2 syllable"
                                               " Solresol word\'s")
            self.starting_text = ("\nNow that you\'ve learned some the verry basic\'s of the solresol word,"
                                  " its time to up the difficulty with 13 of the most helpful to know, 2 SYLLABLE,"
                                  " words in Solresol. But this time with no info Here so you'll just have to guess for"
                                  " any new words you come across, but dont worry you\'ll get it down eventually"
                                "\n\n")
            tmp_label_1 = Label(self.question_frame, wraplength=500, text=self.starting_text, justify="left",
                                font=font_set(16))
            tmp_label_1.grid(row=3)

            continue_button = Button(self.question_frame, text="Continue", bg="#0A0", height=2, fg="#EEEEEE",
                                     font=font_set(is_bold=1), width=25, activeforeground="#333333",
                                     activebackground="#070", command=lambda: self.new_question(questions_options))
            continue_button.grid(row=4)

            back_button = Button(self.question_frame, text="Practice longer", bg="#DB0", height=1, fg="#EEEEEE",
                                     font=font_set(is_bold=1), width=25, activeforeground="#333333",
                                     activebackground="#070", command=lambda: keep_practicing())
            back_button.grid(row=5)

            self.heading_english.config(text="(extreme questions)")
            self.temp_heading.config(text="\n Misisolsol  Sisolsi ")

        elif current_question == 49:
            if self.starting_question == 16 or self.starting_question == 0 or self.starting_question == 32:
                self.starting_question += 1
            else:
                self.starting_question -= 16

            self.temp_instructions.config(text="### In this section you will learn ###\nThe \"Extreme\","
                                               " and quite difficult, responses to a few short sentences"
                                               " Solresol word\'s")
            self.starting_text = ("\n!!! This section assumes that you have extensively practised the last three"
                                  "sections !!! Aside from that the only additional info needed for this section"
                                  "is that a sol st the verry end of a sentence means that sentence is a question"
                                  "\n\n")
            tmp_label_1 = Label(self.question_frame, wraplength=500, text=self.starting_text, justify="left",
                                font=font_set(16))
            tmp_label_1.grid(row=3)

            continue_button = Button(self.question_frame, text="Continue", bg="#0A0", height=2, fg="#EEEEEE",
                                     font=font_set(is_bold=1), width=25, activeforeground="#333333",
                                     activebackground="#070", command=lambda: self.new_question(questions_options))
            continue_button.grid(row=4)

            back_button = Button(self.question_frame, text="Practice longer", bg="#DB0", height=1, fg="#EEEEEE",
                                     font=font_set(is_bold=1), width=25, activeforeground="#333333",
                                     activebackground="#070", command=lambda: keep_practicing())
            back_button.grid(row=5)

            self.heading_english.config(text="(tough questions)")
            self.temp_heading.config(text="\n Resire  Sisolsi ")

        else:
            global questions_diff_group
            question = randint(0, int(len(questions_list[questions_diff_group]))) - 1
            while question == last_question:
                question = randint(0, int(len(questions_list[questions_diff_group]))) - 1
            last_question = question
            make_widget(questions_list[questions_diff_group][question])

        # go to next diff
        if ((current_question == 17) or (current_question == 0) or (current_question == 33) or (current_question == 49)) and (self.starting_question > current_question):
            questions_diff_group += 1



    def to_help(self):
        DisplayHelp(self, current_question)



class DisplayHelp:

    def __init__(self, partner, current_question):
        # setup dialogue box and background colour
        background = "#ffe6cc"
        c_s_color = ""
        b_s_color = "#FF3"
        self.help_box = Toplevel()

        partner.stats_button.config(state=DISABLED)
        for item in partner.questions_options:
            item.config(state=DISABLED)

        self.help_box.protocol('WM_DELETE_WINDOW', partial(self.close_help, partner, current_question))

        self.help_frame = Frame(self.help_box, width=300, height=200)
        self.help_frame.grid()

        help_text = (f"\n Current Question \n\n"
                     f"\n Current Streak \n\n"
                     f"\n Best Streak \n\n")
        self.help_label = Label(self.help_frame, wraplength=500, text=help_text, justify="c", font=font_set(16))
        self.help_label.grid()

        # color config for the numbers
        if current_streak == best_streak:
            b_s_color = "#585"
            c_s_color = "#0C0"
        elif current_streak > best_streak - 3:
            b_s_color = "#0A0"
            c_s_color = "#DD0"
        elif best_streak > current_streak:
            b_s_color = "#0A0"
            c_s_color = "#F22"
        if current_streak == 0:
            c_s_color = "#000"
        if best_streak == 0:
            b_s_color = "#000"


        tmp_label_1_colours = [
            [f"{current_question - 1}", "#000", 0],
            [f"{current_streak}", c_s_color, 1],
            [f"{best_streak}", b_s_color, 2.01]
        ]
        for i in range(0, len(tmp_label_1_colours)):
            tmp_label_1_1 = Label(self.help_frame, wraplength=500, text=tmp_label_1_colours[i][0],
                                  justify="left", font=font_set(16), foreground=tmp_label_1_colours[i][1],
                                  background=background)
            tmp_label_1_1.place(relx=0.5, x=-10, y=50 + (71 * tmp_label_1_colours[i][2]))

        self.dismiss_button = Button(self.help_frame, font=("Arial", "16", "bold"), text="Dismiss", width=25,
                                     bg="#CC6600", fg="#FFFFFF",
                                     command=partial(self.close_help, partner, current_question))
        self.dismiss_button.grid(row=2, padx=10, pady=10)

        recolour_list = [self.help_frame, self.help_label]

        for item in recolour_list:
            item.config(bg=background)

    def close_help(self, partner, rounds_played):
        partner.stats_button.config(state=NORMAL)
        for item in partner.questions_options:
            item.config(state=NORMAL)
        self.help_box.destroy()



# main routine

if __name__ == "__main__":
    root = Tk()

    # Set default screen size position and is resizable
    root.title("Solresol Sidosi Solmilami")
    root.geometry("1280x720+310+120")
    root.resizable(width=True, height=True)
    root.minsize(486, 600)

    # Bind the F11 key to the toggle_fullscreen function
    def toggle_fullscreen(event=None):
        state = not root.attributes("-fullscreen")
        root.attributes("-fullscreen", state)
    root.bind("<F11>", toggle_fullscreen)

    # Start application
    root.update_idletasks()
    StartMenu()
    root.mainloop()
