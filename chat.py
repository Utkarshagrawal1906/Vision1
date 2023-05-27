import tkinter as tk
from tkinter import *
from tkinter import ttk
import message_window as mw
import main
messages = main.Voice.greet(main.Voice)
message_labels = []

class Chat(ttk.Frame):
    def __init__(self, container, background, *args, **kwargs):
        super().__init__(container, *args, **kwargs)

        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
        self.message_window = mw.MessageWindow(self, background=background)
        self.message_window.grid(row=0, column=0, sticky="NSEW", pady=5)
        input_frame = ttk.Frame(self, style="Controls.TFrame", padding=10)
        input_frame.grid(row=1, column=0, sticky="EW")

        self.message_input = tk.Entry(input_frame, font=("Times New Roman",20))
        self.message_input.grid(row=0,column=0,sticky="EW")
        self.message_input.focus()
        message_submit = ttk.Button(
            input_frame,
            text="Send",
            style="SendButton.TButton",
            command=self.query
        )
        message_submit.grid(row=0,column=1,padx=(0,10),sticky="E")
        self.voice_message=ttk.Button(input_frame,style="SendButton.TButton",command=self.voice,text="Voice")
        self.voice_message.grid(row=0,column=2,padx=(2,10))
        labelDict=ttk.Label(input_frame,text="Text Dictation")
        labelDict.grid(row=1,column=0,sticky="W",padx=(5,0))
        if main.dicts==False:
            self.Dictation = ttk.Button(input_frame, style="offButton.TButton",command=self.dict, text="Dictation")
        else:
            self.Dictation = ttk.Button(input_frame, style="TgButton.TButton",command=self.dict, text="Dictation")
        self.Dictation.grid(row=1, column=0,pady=(10,5),sticky="E",padx=(5,30))
        labelFace = ttk.Label(input_frame, text="Face Recognition")
        labelFace.grid(row=1, column=1)
        if main.face==False:
            self.face = ttk.Button(input_frame, style="offButton.TButton",command=self.faceD, text="Face")
        else:
            self.face = ttk.Button(input_frame, style="TgButton.TButton",command=self.faceD, text="Face")
        self.face.grid(row=1, column=2,pady=(10,5))
        self.message_input.bind("<Return>", self.query)
        self.message_window.create_message_container(messages, message_labels)

    def query(self,*args):
        message = self.message_input.get()
        self.message_input.delete(0,END)
        self.message_window.create_received_mess(message, message_labels)
        if message !="sorry":
            self.message_window.create_message_container(main.Voice.search(self, message), message_labels)
        self.message_input.delete(0,END)
        main.Voice.__init__(main.Voice)

    def dict(self):
        if self.Dictation["style"]=="TgButton.TButton":
            self.Dictation.configure(style="offButton.TButton")
            main.dicts=False
        else:
            self.Dictation.configure(style="TgButton.TButton")
            main.dicts=True
        print(self.Dictation["style"])

    def faceD(self):
        if self.face["style"]=="TgButton.TButton":
            self.face.configure(style="offButton.TButton")
            main.face=False
        else:
            self.face.configure(style="TgButton.TButton")
            main.face=True
        print(self.face["style"])

    def voice(self):
        message = main.Voice.voice(main.Voice)
        self.message_window.create_received_mess(message, message_labels)
        if message !="sorry":
            self.message_window.create_message_container(main.Voice.search(self, message), message_labels)
        main.Voice.__init__(main.Voice)
