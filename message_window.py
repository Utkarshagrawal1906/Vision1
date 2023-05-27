import tkinter as tk
from tkinter import ttk
import main
SCREEN_SIZE_TO_MESSAGE_WIDTH = {
    1100: 830,
    950: 680,
    750: 480
}
n=0

class MessageWindow(tk.Canvas):
    def __init__(self, container, *args, **kwargs):
        super().__init__(container, *args, **kwargs, highlightthickness=0)

        self.messages_frame = ttk.Frame(container, style="Messages.TFrame")
        self.messages_frame.columnconfigure(0, weight=1)

        self.scrollable_window = self.create_window((0, 0), window=self.messages_frame, anchor="nw", width=self.winfo_width())

        def configure_scroll_region(event):
            self.configure(scrollregion=self.bbox("all"))

        def configure_window_size(event):
            self.itemconfig(self.scrollable_window, width=self.winfo_width())

        self.bind("<Configure>", configure_window_size)
        self.messages_frame.bind("<Configure>", configure_scroll_region)
        self.bind_all("<MouseWheel>", self._on_mousewheel)

        scrollbar = ttk.Scrollbar(container, orient="vertical", command=self.yview)
        scrollbar.grid(row=0, column=1, sticky="NS")

        self.configure(yscrollcommand=scrollbar.set)
        self.yview_moveto(1.0)


    def _on_mousewheel(self, event):
        self.yview_scroll(-int(event.delta / 120), "units")

    def create_message_container(self, message_content, message_labels):
        container = ttk.Frame(self.messages_frame, style="Messages.TFrame")
        container.columnconfigure(1, weight=1)
        container.grid(sticky="EW", padx=(10, 70), pady=10)

        def reconfigure_message_labels(event):
            closest_break_point = min(SCREEN_SIZE_TO_MESSAGE_WIDTH.keys(),
                                      key=lambda b: abs(b - container.winfo_width()))
            for label in message_labels:
                if label.winfo_width() < closest_break_point:
                    label.configure(wraplength=SCREEN_SIZE_TO_MESSAGE_WIDTH[closest_break_point])
            self.messages_frame.update()
            main.Voice.speak(message_content)
            main.Voice.fone(main.Voice)

        container.bind("<Configure>", reconfigure_message_labels)
        self._create_message_bubble(container, message_content, message_labels)

    def create_received_mess(self, message_content, message_labels):
        container = ttk.Frame(self.messages_frame, style="Messages.TFrame")
        container.columnconfigure(1, weight=1)
        container.grid(sticky="EW", padx=(70, 10), pady=10)

        def reconfigure_message_labels(event):
            closest_break_point = min(SCREEN_SIZE_TO_MESSAGE_WIDTH.keys(),
                                      key=lambda b: abs(b - container.winfo_width()))
            for label in message_labels:
                if label.winfo_width() < closest_break_point:
                    label.configure(wraplength=SCREEN_SIZE_TO_MESSAGE_WIDTH[closest_break_point])
            self.messages_frame.update()

        container.bind("<Configure>", reconfigure_message_labels)
        self._create_message_bubble(container, message_content, message_labels)

    def _create_message_bubble(self, container, message_content, message_labels):
        message_label = ttk.Label(
            container,
            text=message_content,
            wraplength=700,
            justify="left",
            anchor="w",
            style="Message.TLabel"
        )
        message_label.grid(row=1, column=1, sticky="NEW")

        message_labels.append(message_label)