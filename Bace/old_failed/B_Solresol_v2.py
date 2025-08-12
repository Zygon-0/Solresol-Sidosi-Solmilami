# initial imports and variables
from tkinter import *
_shown_widgets = []
_available_buttons = []
_last_screen = []




# screen change functions
def load_screen(self, screen_number):
    """
    Adds everything in the _shown_widgets list to the screen in order
    :return: None
    """

    print(_available_buttons)

    screens_list = [
        ["Familiar", "In this section you will learn: \n Familiar and simple one syllable solresol "
         "\n writen using english symbols", _available_buttons[0]]
    ]

    _last_screen.append(self.main_heading.cget("text"))
    _last_screen.append(self.note_label.cget("text"))
    for i in _shown_widgets:
        _last_screen.append(i)
        if i == _available_buttons[0]:
            i.place_forget()
        else:
            i.grid_forget()
    _shown_widgets.clear()

    self.main_heading.config(text=screens_list[screen_number][0])
    self.note_label.config(text=screens_list[screen_number][1])
    for count, item in enumerate(screens_list[screen_number]):
        if count == 0 or count == 1:
            pass
        else:
            _shown_widgets.append(item)

    for count, i in enumerate(_shown_widgets):
        if i == _available_buttons[0]:
            i.place(x=655, y=221)

        else:
            print(i, i)
            i.grid(row=count + 3)


class Start:
    """
    Main application gui control
    """

    def __init__(self):
        """
        Main application gui control
        """





        ### Frame and heading ###

        # Create bace frame
        self.temp_frame = Frame(padx=(root.winfo_width()/2)-300, pady=150, width=1920, height=1080)
        self.temp_frame.grid()

        # Main heading label
        self.main_heading = Label(self.temp_frame, text="Solresol Sidosi\n Solmilami",
                                  font=("Georgia", 32, "bold"), justify="center")

        self.main_heading.grid()

        # line seperator (also insures correct center alignment)
        self.line = Label(self.temp_frame, text="────────────────────",
                          font=("Georgia", 32, "bold"), justify="center")
        self.line.grid(row=1)

        # Sub-heading / note label
        self.note_label = Label(self.temp_frame, text="Welcome to the Solresol learning app.\n please select an option below", width=40, font=("Arial", 16),
                                justify="center")
        self.note_label.grid(row=2)





        ### Buttons ###

        # create buttons
        def create_button(button, number):
            """
            Creates a fully functional button out of a self.Variable equal to None
            :param button: The self.Variable to be made into a working button
            :param number: The number in the for loop the given button is
            :return:
            """

            pixel = PhotoImage(width=1, height=1)

            if number is None:
                button = Button(root, text="◄", padx=0, pady=0, font=("Arial", 23), width=20, height=27,
                                image=pixel, highlightthickness=0, bd=0, fg="#000000", compound="center",
                                command=self.back_clicked)
                print(button)
                _available_buttons.append(button)

                def on_hover(event):
                    event.widget.configure(fg="#2222aa", image=pixel)

                def on_leave(event):
                    event.widget.configure(fg="#000000", image=pixel)

                button.bind("<Enter>", on_hover)
                button.bind("<Leave>", on_leave)
            else:

                # button list | text, active_text, clicked_function
                all_button_variables = [
                    ["Familiar", "Written Form", print("clicked")],
                    ["Transitional", "Musical Notation", None],
                    ["Tough", "Line Form", None],
                    ["Extreme", "Audio Form", None]
                ]
                print("we got here?")
                print(number)
                print(button)

                button = Button(self.temp_frame, text=all_button_variables[number][0], highlightthickness=0, bd=0,
                                font=("Arial", 24, "bold"), fg="#333333", padx=0, pady=0,
                                command=all_button_variables[number][2])

                print(button)
                _available_buttons.append(button)

                def on_hover(event):
                    event.widget.configure(fg="#2222aa", text=all_button_variables[number][1])

                def on_leave(event):
                    event.widget.configure(fg="#333333", text=all_button_variables[number][0])

                button.bind("<Enter>", on_hover)
                button.bind("<Leave>", on_leave)


        # setup buttons
        self.familiar_button = None
        self.transitional_button = None
        self.tough_button = None
        self.extreme_button = None
        self.back_button = None
        create_button(self.back_button, None)

        # add buttons to list and loop to create the actual buttons
        buttons_to_make = [
            self.familiar_button,
            self.transitional_button,
            self.tough_button,
            self.extreme_button
        ]
        if _shown_widgets == []:
            for count, item in enumerate(buttons_to_make):
                create_button(item, count)

            _shown_widgets.clear()
            self.main_heading.config(text="Solresol Sidosi\n Solmilami")
            self.note_label.config(text="Welcome to the Solresol learning app.\n please select an option below")
            _shown_widgets.append(_available_buttons[1])
            _shown_widgets.append(_available_buttons[2])
            _shown_widgets.append(_available_buttons[3])
            _shown_widgets.append(_available_buttons[4])
            _available_buttons[0].place_forget()

        for count, i in enumerate(_shown_widgets):
            print(i, i)
            i.grid(row=count + 3)




    ### Button click functions ###






    def back_clicked(self):

        # Change title labels
        self.main_heading.config(text=_last_screen[0])
        _last_screen.pop(0)
        self.note_label.config(text=_last_screen[0])
        _last_screen.pop(0)

        for count, i in enumerate(_last_screen):
            if i == _available_buttons[0]:
                pass
            else:
                _shown_widgets.append(i)
        _last_screen.clear()

        for count, i in enumerate(_shown_widgets):
            i.grid(row=count + 3)



# main routine

if __name__ == "__main__":
    root = Tk()
    root.title("Solresol Sidosi Solmilami")
    root.geometry("1920x1080")
    root.eval('tk::PlaceWindow . center')
    root.attributes("-fullscreen", True)

    # Bind the F11 key to the toggle_fullscreen function
    def toggle_fullscreen(event=None):
        state = not root.attributes("-fullscreen")
        root.attributes("-fullscreen", state)
    root.bind("<F11>", toggle_fullscreen)

    Start()
    root.mainloop()
