import tkinter as tk
from tkinter import ttk,PhotoImage
import tkinter.font as font
import chat

COLOUR_LIGHT_BACKGROUND_1 = "#fff"
COLOUR_LIGHT_BACKGROUND_2 = "#f2f3f5"
COLOUR_LIGHT_BACKGROUND_3 = "#e3e5e8"

COLOUR_LIGHT_TEXT = "#aaa"

COLOUR_BUTTON_NORMAL = "#5fba7d"
COLOUR_BUTTON_ACTIVE = "#58c77c"
COLOUR_BUTTON_PRESSED = "#44e378"


class Messenger(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.geometry("590x600")
        self.minsize(100, 500)
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
        self.title("Vision")
        self.chat_frame = chat.Chat(
            self,
            background=COLOUR_LIGHT_BACKGROUND_3,
            style="Messages.TFrame"
        )

        self.chat_frame.grid(row=0, column=0, sticky="NSEW")

root = Messenger()

font.nametofont("TkDefaultFont").configure(size=14)

style = ttk.Style(root)
style.theme_use("clam")
img=PhotoImage(file="assets/on.png")
img1=PhotoImage(file="assets/off.png")
style.configure("Messages.TFrame", background=COLOUR_LIGHT_BACKGROUND_3)

style.configure("Controls.TFrame", background=COLOUR_LIGHT_BACKGROUND_2)

style.configure("SendButton.TButton", borderwidth=0, background=COLOUR_BUTTON_NORMAL)
style.map(
    "SendButton.TButton",
    background=[("pressed", COLOUR_BUTTON_PRESSED), ("active", COLOUR_BUTTON_ACTIVE)],
)
style.configure("offButton.TButton", image=img1)
style.configure("TgButton.TButton",image=img)
style.configure(
    "FetchButton.TButton", background=COLOUR_LIGHT_BACKGROUND_1, borderwidth=0
)

style.configure(
    "Time.TLabel",
    padding=5,
    background=COLOUR_LIGHT_BACKGROUND_1,
    foreground=COLOUR_LIGHT_TEXT,
    font=8
)

style.configure("Avatar.TLabel", background=COLOUR_LIGHT_BACKGROUND_3)
style.configure("Message.TLabel", background=COLOUR_LIGHT_BACKGROUND_2)
root.mainloop()