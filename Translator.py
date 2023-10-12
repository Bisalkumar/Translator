import json
from tkinter import Tk, Label, Button, Entry, StringVar, OptionMenu, Text, Scrollbar
from googletrans import Translator

def load_languages(filename="language.json"):
    with open(filename, 'r') as file:
        return json.load(file)

class TranslatorGUI:
    def __init__(self, master):
        self.master = master
        master.title("Language Translator")

        self.translator = Translator()
        self.languages = load_languages()

        self.title_label = Label(master, text="Language Translator", font=("Arial", 24))
        self.title_label.pack(pady=20)

        self.lang_var = StringVar(master)
        self.lang_var.set(list(self.languages.keys())[0])  # default value

        self.option_label = Label(master, text="Select Language")
        self.option_label.pack(pady=10)

        self.lang_dropdown = OptionMenu(master, self.lang_var, *self.languages.keys())
        self.lang_dropdown.pack()

        self.input_label = Label(master, text="Enter Text")
        self.input_label.pack(pady=10)

        self.input_text = Text(master, height=5, width=50)
        self.input_text.pack()

        self.translate_button = Button(master, text="Translate", command=self.translate_text)
        self.translate_button.pack(pady=20)

        self.output_label = Label(master, text="Translated Text")
        self.output_label.pack(pady=10)

        self.output_text = Text(master, height=5, width=50)
        self.output_text.pack()

    def translate_text(self):
        source_text = self.input_text.get("1.0", "end-1c")
        dest_code = self.lang_var.get()

        try:
            translated = self.translator.translate(source_text, dest=dest_code)
            self.output_text.delete("1.0", "end")
            self.output_text.insert("1.0", translated.text)
        except Exception as e:
            self.output_text.delete("1.0", "end")
            self.output_text.insert("1.0", f"An error occurred: {e}")

if __name__ == "__main__":
    root = Tk()
    gui = TranslatorGUI(root)
    root.mainloop()
