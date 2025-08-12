from tkinter import *
from functools import partial

_shown_widgets = []


def clear_screen():
    """
    Removes everything below the note
    :return: None
    """
    for i in _shown_widgets:
        i.grid_forget()
    _shown_widgets.clear()


def refresh_screen():
    """
    Adds everything in the _shown_widgets list to the screen in order
    :return: None
    """
    for count, i in enumerate(_shown_widgets):
        i.grid(row=count + 3)


class Start:
    """
    Temp Converter between °C °F
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
                                  font=("Georgia", "32", "bold"), justify="center")

        self.main_heading.grid()

        # line seperator (also insures correct center alignment)
        self.line = Label(self.temp_frame, text="────────────────────",
                          font=("Georgia", "32", "bold"), justify="center")
        self.line.grid(row=1)

        # Sub-heading / note label
        note = "Welcome to the Solresol learning app.\n please select an option below"
        self.note_label = Label(self.temp_frame, text=note, width=40, font=("Arial", "16"),
                                justify="center")
        self.note_label.grid(row=2)





        ### Buttons ###

        # familiar button
        self.familiar_button = Button(self.temp_frame, text="Familiar", highlightthickness=0, bd=0,
                                      activeforeground="#222280", font=("Arial", "24", "bold"), padx=0, pady=0,
                                      command=partial(self.familiar_clicked))

        def on_hover_familiar(event):
            event.widget.configure(fg="#2222aa", text="Written Form")

        def on_leave_familiar(event):
            event.widget.configure(fg="#333333", text="Familiar")

        self.familiar_button.bind("<Enter>", on_hover_familiar)
        self.familiar_button.bind("<Leave>", on_leave_familiar)
        _shown_widgets.append(self.familiar_button)

        # transitional button
        self.transitional_button = Button(self.temp_frame, text="Transitional", highlightthickness=0, bd=0,
                                          activeforeground="#222280", font=("Arial", "24", "bold"), padx=0, pady=0)

        def on_hover_transitional(event):
            event.widget.configure(fg="#2222aa", text="Musical Notation")

        def on_leave_transitional(event):
            event.widget.configure(fg="#333333", text="Transitional")

        self.transitional_button.bind("<Enter>", on_hover_transitional)
        self.transitional_button.bind("<Leave>", on_leave_transitional)
        _shown_widgets.append(self.transitional_button)

        # tough button
        self.tough_button = Button(self.temp_frame, text="Tough", highlightthickness=0, bd=0,
                                   activeforeground="#222280", font=("Arial", "24", "bold"), padx=0, pady=0)

        def on_hover_tough(event):
            event.widget.configure(fg="#2222aa", text="Line Form")

        def on_leave_tough(event):
            event.widget.configure(fg="#333333", text="Tough")

        self.tough_button.bind("<Enter>", on_hover_tough)
        self.tough_button.bind("<Leave>", on_leave_tough)
        _shown_widgets.append(self.tough_button)

        # extreme button
        self.extreme_button = Button(self.temp_frame, text="Extreme", highlightthickness=0, bd=0,
                                     activeforeground="#222280", font=("Arial", "24", "bold"), padx=0, pady=0)

        def on_hover_extreme(event):
            event.widget.configure(fg="#2222aa", text="Audio Form")

        def on_leave_extreme(event):
            event.widget.configure(fg="#333333", text="Extreme")

        self.extreme_button.bind("<Enter>", on_hover_extreme)
        self.extreme_button.bind("<Leave>", on_leave_extreme)
        _shown_widgets.append(self.extreme_button)

        for count, i in enumerate(_shown_widgets):
            i.grid(row=count + 3)





    ### Button click functions ###

    # Familiar button function
    def familiar_clicked(self):

        # Change title labels
        self.main_heading.config(text="Familiar")
        self.note_label.config(text="In this section you will learn: \n Familiar and simple one syllable solresol "
                                    "\n writen using english symbols")

        # load new screen
        clear_screen()

        _shown_widgets.append(self.extreme_button)

        refresh_screen()




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
