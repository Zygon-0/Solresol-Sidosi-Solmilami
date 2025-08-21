##### Imports #####
import random
from random import randint
from tkinter import *
from functools import partial
from Solresol.Components.Grp_DB.C0_grq_db_v4 import questions_list





##### Global Variables #####

# var for the windows geometry
root_geometry = ""

# vars for the questions themselves
question_set_len = 1 + 1
current_question = 0
questions_right = 0
questions_wrong = 0
got_q_wrong = 0

# vars for the streak system
current_streak = 0
best_streak = 0

# var for which question dif the player is at
questions_diff_group = 0

# vars for repeated question prevention
last_question = 0
pre_last_question = 0

# global lists
placed_widgets = []
temp_instructions_list = []
colour_list = [
    ["#E33", "#C11"],
    ["#F80", "#D60"],
    ["#DB0", "#B90"],
    ["#0A0", "#080"],
    ["#3C9", "#1A7"],
    ["#06F", "#04D"],
    ["#609", "#407"]
]





##### Functions #####

# function for simplified font setting
def font_set(font_size=12, is_fancy_font=0, is_bold=0, is_italic=0):
    """
    creates font in a very simple way
    :param is_fancy_font: changes font to georgia if set to <1> (default <0>)
    :param font_size: sets font size to chosen number (default <12>)
    :param is_bold: makes font bold if set to <1> (default <0>)
    :param is_italic: makes font italic if set to <1> (default <0>)
    :return:
    """

    # basic font with no changes
    font = ["Arial", font_size]

    # change font to georgia if wanted
    if is_fancy_font == 1:
        font[0] = "Georgia"

    # make font bold if wanted
    if is_bold == 1:
        font.append("bold")

    # make font italic if wanted
    if is_italic == 1:
        font.append("italic")

    # return the tuple with all the correct info
    return tuple(font)





##### Classes #####

# starting screen
class StartMenu:
    """
    Runs the main start menu
    """
    def __init__(self):
        """
        start menu GUI
        """

        # Configure side columns to ensure centered widgets
        root.grid_columnconfigure(0, weight=1)
        root.grid_columnconfigure(2, weight=1)

        # tkinter frame to hold all the buttons and labels
        self.temp_frame = Frame(padx=10, pady=10)
        self.temp_frame.grid(row=1, column=1)

        #  the main heading
        self.main_heading = Label(self.temp_frame, text="\nSolresol  Sidosi\nSolmilami",
                                  font=font_set(24, 1, 1))

        self.main_heading.grid(row=0, pady=5)

        # line seperator to insure correct center alignment and look cool
        self.line = Label(self.temp_frame, text="────────────────────",
                          font=font_set(24, 1, 1), justify="center")
        self.line.grid(row=1)

        # small label showing the english translation of the title
        self.heading_english = Label(self.temp_frame, text="(language learning program)", font=font_set(10), foreground="#555555")
        self.heading_english.place(relx=0.5, rely=0.5, anchor="center", y=-119)

        # sub-heading with a small note about what is on the current screen
        sub_heading_note = "Welcome to the Solresol learning app. \n please select an option below \n"
        self.sub_heading = Label(self.temp_frame, text=sub_heading_note, width=40, justify="center",
                                 font=font_set(is_fancy_font=1))
        self.sub_heading.grid(row=2)

        # inner frame to hold all the buttons
        self.button_frame = Frame(self.temp_frame)
        self.button_frame.grid(row=5)

        # list of all the key info for each button
        buttons_list = [
            ["Familiar", "#3377BB", "#115599", partial(self.to_questions, 0, 0)],
            ["Transitional", "#229922", "#007700", partial(self.to_questions, question_set_len, 1)],
            ["Tough", "#CC6600", "#aa4400", partial(self.to_questions, 2 * question_set_len, 2)],
            ["Extreme", "#990000", "#770000", partial(self.to_questions, 3 * question_set_len, 3)]
        ]

        # list to hold buttons once they have been made
        self.button_ref_list = []

        # for loop to make the buttons using the above list
        for count, item in enumerate(buttons_list):
            self.make_button = Button(self.button_frame, text=item[0], bg=item[1], height=2, activebackground=item[2],
                                      fg="#EEEEEE", font=font_set(is_bold=1), width=25, activeforeground="#333333",
                                      command=item[3])
            self.make_button.grid(row=count, padx=5, pady=10)

            self.button_ref_list.append(self.make_button)

    # function to go to the questions screen itself
    def to_questions(self, int_start, dif_start):
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

# questions screen
class FQMenu:
    def __init__(self):
        """
        Area for the different grades of questions
        """

        # initial var setup
        global current_question
        self.starting_question = current_question
        self.starting_text = ""

        # box shape and position setup
        self.f_q_box = Toplevel()
        global root_geometry
        self.f_q_box.geometry(root_geometry)
        self.f_q_box.minsize(486, 600)
        self.f_q_box.resizable(width=True, height=True)
        self.f_q_box.attributes("-fullscreen", root.attributes("-fullscreen"))

        # Bind the F11 key to the toggle_fullscreen function
        def toggle_fullscreen_function(event=None):
            state = not self.f_q_box.attributes("-fullscreen")
            self.f_q_box.attributes("-fullscreen", state)
        self.f_q_box.bind("<F11>", toggle_fullscreen_function)

        # Configure side columns to ensure centered widgets
        self.f_q_box.grid_columnconfigure(0, weight=1)
        self.f_q_box.grid_columnconfigure(2, weight=1)

        # closes the app properly if red X is pressed
        self.f_q_box.protocol('WM_DELETE_WINDOW', root.destroy)

        # frame to hold all the main labels and buttons
        self.f_q_frame = Frame(self.f_q_box, padx=10, pady=10)
        self.f_q_frame.grid(row=1, column=1)

        # the main heading
        self.main_heading = Label(self.f_q_frame, text="\n Resolsila  Sisolsi ",
                                  font=font_set(24, 1, 1))
        self.main_heading.grid(row=0, pady=5)

        # line seperator to insure correct center alignment and look cool
        self.line = Label(self.f_q_frame, text="────────────────────",
                          font=font_set(24, 1, 1), justify="center")
        self.line.grid(row=1, padx=400)

        # small english translation of the above title
        self.heading_english = Label(self.f_q_box, text="(familiar questions)", font=font_set(10),
                                     justify="center", foreground="#555555")
        self.heading_english.place(relx=0.5, rely=0, anchor="n", y=103)

        # sub-heading to describe what the current screen is and its default value
        heading_note = " ### In this section you will learn ### \n The \"familiar\" and simple order of the letters in Solresol, and what all the syllable\'s are."
        self.sub_heading = Label(self.f_q_frame, text=heading_note, width=40, justify="center",
                                 font=font_set(is_fancy_font=1), wraplength=350)
        self.sub_heading.grid(row=2)

        # inner frame to hold everything for the question itself
        self.question_frame = Frame(self.f_q_frame)
        self.question_frame.grid(row=3)

        # start the first question
        self.questions_options = []
        self.new_question(self.questions_options)





    # function to pick, configure, and display the question (this is most of the program)
    def new_question(self, questions_options):
        # resting the data in preparation for a new question
        global current_question
        current_question += 1
        global got_q_wrong
        got_q_wrong = 0
        global temp_instructions_list

        # clear all list data from the last question so the next questions info to be stored in them
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

        # function that sets the question label to the chosen question and makes all the needed buttons
        def make_widget(widget):
            # list of button colors that the buttons will be in order
            global colour_list
            random.shuffle(colour_list)

            # makes the actual widget for each widgets info in the chosen question
            for count, items in enumerate(widget):
                # if the widget id is "l" then make a label using the other items in the list
                if items[0] == "l":
                    widget_made = Label(self.question_frame, wraplength=500, text=items[1], justify="left",
                                        font=font_set(16))
                    questions_options.append(widget_made)

                # if the widget id is "b" then make the button and preset the command to wrong_button_clicked
                elif items[0] == "b":
                    widget_made = Button(self.question_frame, text=items[1], bg=colour_list[items[6]][0], height=2, fg="#EEEEEE",
                                         font=font_set(is_bold=1), width=25, activeforeground="#333333",
                                         activebackground=colour_list[items[6]][1], command=partial(wrong_button_clicked, str(items[7])))
                    global temp_instructions_list
                    questions_options.append(widget_made)
                    temp_instructions_list.append(items[7])

            # find the button that was the actual correct button and sets that buttons command to correct_button_clicked
            for c, ii in enumerate(widget):
                if len(ii) > 3:
                    if ii[6] == 1:
                        global current_streak
                        questions_options[c].config(command=lambda: correct_button_clicked())

            # add the question text to the grid then remove it from the widget list
            questions_options[0].grid(row=0, pady=5)
            questions_options.pop(0)

            # shuffle the buttons order then add each of those to the grid bellow the question text
            random.shuffle(questions_options)
            for count, items in enumerate(questions_options):
                items.grid(row=count + 1, pady=5)

            # make the stats screen button and place it on the screen
            self.stats_button = Button(self.f_q_frame, text="     ℹ️", padx=0, pady=0, font=("Arial", 30),
                                       highlightthickness=0, bd=0, fg="#EC0",
                                       command=lambda: self.to_help())
            self.stats_button.place(relx=0.5, x=-220, y=75, width=20, height=40)

        # function for the keep practicing button is pressed
        def keep_practicing():
            global current_question
            global questions_diff_group
            current_question -= question_set_len + 1
            self.starting_question -= question_set_len
            questions_diff_group -= 1
            self.new_question(questions_options)

        # function for when the correct answer button is pressed
        def correct_button_clicked():
            global best_streak
            global current_streak
            global questions_right
            questions_right += 1
            current_streak += 1
            if current_streak > best_streak:
                best_streak = current_streak
            self.new_question(questions_options)

        # function for when any of the wrong answer buttons are pressed
        def wrong_button_clicked(button):
            self.sub_heading.config(text=button, fg="#E33")
            widget_text = ""
            for widget in questions_list[questions_diff_group][question]:
                if len(widget) > 3:
                    if widget[7] == button:
                        widget_text = widget[1]
            global best_streak
            global current_streak
            global questions_wrong
            global got_q_wrong
            if got_q_wrong == 0:
                questions_wrong += 1
                got_q_wrong = 1

            if current_streak > best_streak:
                best_streak = current_streak
            current_streak = 0

            for j in questions_options:
                if j.cget("text") == widget_text:
                    j.config(state=DISABLED)

        # if the current question isn't the starting screen then display the current question to the user
        if current_question > 1:
            self.sub_heading.config(text=f"Current Question: {current_question - self.starting_question - 1}",
                                    fg="#000")

        global questions_diff_group
        global question_set_len
        # display info about the upcoming questions if at certain question numbers
        if current_question == 1:
            # the main info text to displayed
            self.starting_text = ("\nIn Solresol there are only 7 letters, which come together to create around 300 words,"
                             " below 4 syllables. these letters are the common scale of.\nDo, Re, Mi, Fa, Sol, La, Si.\n")
            tmp_label_1 = Label(self.question_frame, wraplength=500, text=self.starting_text, justify="left",
                                font=font_set(16))
            tmp_label_1.grid(row=3)

            # text and colors for some parts of the displayed text to be colored
            tmp_label_1_colours = [
                ["Do,", "#E33", 0],
                ["Re,", "#F80", 1],
                ["Mi,", "#DB0", 2],
                ["Fa,", "#0A0", 3],
                ["Sol,", "#3C9", 4],
                ["La,", "#06F", 5.15],
                ["Si.", "#609", 6.15]
            ]

            # for each piece of text to be colored make that colored text and pricelessly place it on screen
            for i in range(0, len(tmp_label_1_colours)):
                tmp_label_1_color = Label(self.question_frame, wraplength=500, text=tmp_label_1_colours[i][0],
                                      justify="left", font=font_set(16), foreground=tmp_label_1_colours[i][1],
                                      background="#EEE")
                tmp_label_1_color.place(x=(37 * tmp_label_1_colours[i][2]), y=96)

            # button to continue on with the next set of questions
            continue_button = Button(self.question_frame, text="Continue", bg="#0A0", height=2, fg="#EEEEEE",
                                 font=font_set(is_bold=1), width=25, activeforeground="#333333",
                                 activebackground="#070", command=lambda: self.new_question(questions_options))
            continue_button.grid(row=10)

        elif current_question == question_set_len + 1:
            # bullet proofing for the question that the program tells the user they are on
            if self.starting_question == 0:
                self.starting_question += 1

            # the main info text to displayed
            self.sub_heading.config(text="### In this section you will learn ###\nThe \"transitional\","
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

            # text and colors for some parts of the displayed text to be colored
            tmp_label_1_colours = [
                ["Do", "#E33", 0],
                ["Re", "#F80", 1],
                ["Mi", "#DB0", 2],
                ["Fa", "#0A0", 3],
                ["Sol", "#3C9", 4],
                ["La", "#06F", 5],
                ["Si", "#609", 6]
            ]
            # for each piece of text to be colored make that colored text and pricelessly place it on screen
            for i in range(0, len(tmp_label_1_colours)):
                tmp_label_1_color = Label(self.question_frame, wraplength=500, text=tmp_label_1_colours[i][0],
                                      justify="left", font=font_set(16), foreground=tmp_label_1_colours[i][1],
                                      background="#EEE")
                tmp_label_1_color.place(x=34, y=144 + (23.9 * tmp_label_1_colours[i][2]))

            # button to continue on with the next set of questions
            continue_button = Button(self.question_frame, text="Continue", bg="#0A0", height=2, fg="#EEEEEE",
                                     font=font_set(is_bold=1), width=25, activeforeground="#333333",
                                     activebackground="#070", command=lambda: self.new_question(questions_options))
            continue_button.grid(row=4)

            # button to go back to the previous set of questions
            back_button = Button(self.question_frame, text="Practice longer", bg="#DB0", height=1, fg="#EEEEEE",
                                     font=font_set(is_bold=1), width=25, activeforeground="#333333",
                                     activebackground="#070", command=lambda: keep_practicing())
            back_button.grid(row=5)

            # change the title and translation to the new sections corresponding text
            self.heading_english.config(text="(between questions)")
            self.main_heading.config(text="\n Mimiresol  Sisolsi ")

        elif current_question == (2 * question_set_len) + 1:
            # bullet proofing for the question that the program tells the user they are on
            if self.starting_question == 1 or self.starting_question == question_set_len:
                self.starting_question += 1

            # the main info text to displayed
            self.sub_heading.config(text="### In this section you will learn ###\nThe \"Tough\","
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

            # button to continue on with the next set of questions
            continue_button = Button(self.question_frame, text="Continue", bg="#0A0", height=2, fg="#EEEEEE",
                                     font=font_set(is_bold=1), width=25, activeforeground="#333333",
                                     activebackground="#070", command=lambda: self.new_question(questions_options))
            continue_button.grid(row=4)

            # button to go back to the previous set of questions
            back_button = Button(self.question_frame, text="Practice longer", bg="#DB0", height=1, fg="#EEEEEE",
                                     font=font_set(is_bold=1), width=25, activeforeground="#333333",
                                     activebackground="#070", command=lambda: keep_practicing())
            back_button.grid(row=5)

            # change the title and translation to the new sections corresponding text
            self.heading_english.config(text="(extreme questions)")
            self.main_heading.config(text="\n Misisolsol  Sisolsi ")

        elif current_question == (3 * question_set_len) + 1:
            # bullet proofing for the question that the program tells the user they are on
            if self.starting_question == 2 or self.starting_question == (question_set_len + 1) or self.starting_question == (2 * question_set_len):
                self.starting_question += 1

            # the main info text to displayed
            self.sub_heading.config(text="### In this section you will learn ###\nThe \"Extreme\","
                                               " and quite difficult, responses to a few short sentences"
                                               " Solresol word\'s")
            self.starting_text = ("\n!!! This section assumes that you have extensively practised the last three"
                                  "sections !!! Aside from that the only additional info needed for this section"
                                  "is that a sol st the verry end of a sentence means that sentence is a question"
                                  "\n\n")
            tmp_label_1 = Label(self.question_frame, wraplength=500, text=self.starting_text, justify="left",
                                font=font_set(16))
            tmp_label_1.grid(row=3)

            # button to continue on with the next set of questions
            continue_button = Button(self.question_frame, text="Continue", bg="#0A0", height=2, fg="#EEEEEE",
                                     font=font_set(is_bold=1), width=25, activeforeground="#333333",
                                     activebackground="#070", command=lambda: self.new_question(questions_options))
            continue_button.grid(row=4)

            # button to go back to the previous set of questions
            back_button = Button(self.question_frame, text="Practice longer", bg="#DB0", height=1, fg="#EEEEEE",
                                     font=font_set(is_bold=1), width=25, activeforeground="#333333",
                                     activebackground="#070", command=lambda: keep_practicing())
            back_button.grid(row=5)

            # change the title and translation to the new sections corresponding text
            self.heading_english.config(text="(tough questions)")
            self.main_heading.config(text="\n Resire  Sisolsi ")

        # if on an actual question pick the question and display it
        else:
            # globals needed
            global questions_diff_group
            global last_question
            global pre_last_question
            # set the question to a random question in the list of questions
            question = randint(1, int(len(questions_list[questions_diff_group]))) - 1

            # if the chosen question is the same as one of the last 2 questions then pick another question at random
            while question == last_question or question == pre_last_question:
                question = randint(1, int(len(questions_list[questions_diff_group]))) - 1
            pre_last_question = last_question
            last_question = question

            # once a valid question is selected rerun the function with that new question as the selected question
            make_widget(questions_list[questions_diff_group][question])

        # go to next diff with bullet proofing
        if (current_question == 0 or current_question % question_set_len == 0) and (self.starting_question < current_question):
            questions_diff_group += 1

    # function to take the user to the help screen
    def to_help(self):
        DisplayHelp(self, current_question, self.starting_question)

# info screen
class DisplayHelp:

    def __init__(self, partner, current_q, starting):
        # setup dialogue box and background colour
        background = "#ffe6cc"
        c_s_color = ""
        b_s_color = "#FF3"
        p_r_color = "#000"
        self.help_box = Toplevel()

        # diable answer buttons while looking at info
        partner.stats_button.config(state=DISABLED)
        for item in partner.questions_options:
            item.config(state=DISABLED)

        # closes info bow properly if top corner X is pressed
        self.help_box.protocol('WM_DELETE_WINDOW', partial(self.close_help, partner))

        # frame for all the text and buttons to go in
        self.help_frame = Frame(self.help_box, width=300, height=200)
        self.help_frame.grid()

        # the non colored text with gaps for the colored parts
        help_text = (f"\n Current Question \n\n"
                     f"\n Current Streak \n\n"
                     f"\n Best Streak \n\n"
                     f"\n Pass Rate \n\n")
        self.help_label = Label(self.help_frame, wraplength=500, text=help_text, justify="l", font=font_set(16))
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

        # try except code for if the pass rate calculation needs to divide by zero
        try:
            pass_rate = ((current_q - starting - questions_wrong - 2) / (current_q - starting - 2)) * 100
        except ZeroDivisionError:
            pass_rate = 0

        # color config for pass rate
        if pass_rate == 100:
            p_r_color = "#0C0"
        elif pass_rate > 75:
            p_r_color = "#696"
        elif pass_rate > 50:
            p_r_color = "#DB0"
        elif pass_rate > 25:
            p_r_color = "#F80"
        elif pass_rate > 0:
            p_r_color = "#E33"

        # list for the colored text to be placed
        tmp_label_1_colours = [
            [f"{current_q - starting - 1}", "#000", 0],
            [f"{current_streak}", c_s_color, 1.005],
            [f"{best_streak}", b_s_color, 2.01],
            [f"{pass_rate:.0f}%", p_r_color, 3.015]
        ]
        # for loop to place all the colored text in the correct places
        for i in range(0, len(tmp_label_1_colours)):
            tmp_label_1_1 = Label(self.help_frame, wraplength=500, text=tmp_label_1_colours[i][0],
                                  justify="left", font=font_set(16), foreground=tmp_label_1_colours[i][1],
                                  background=background)
            tmp_label_1_1.place(relx=0.5, x=-80, y=50 + (71 * tmp_label_1_colours[i][2]))

        # button to close the info screen
        self.dismiss_button = Button(self.help_frame, font=("Arial", "16", "bold"), text="Dismiss", width=25,
                                     bg="#CC6600", fg="#FFFFFF",
                                     command=partial(self.close_help, partner))
        self.dismiss_button.grid(row=2, padx=10, pady=10)

        # recolor the background of each item to orange
        recolour_list = [self.help_frame, self.help_label]

        for item in recolour_list:
            item.config(bg=background)

    # function for closing the info screen itself
    def close_help(self, partner):
        partner.stats_button.config(state=NORMAL)
        for item in partner.questions_options:
            item.config(state=NORMAL)
        self.help_box.destroy()





##### Main Routine #####
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
