import tkinter as tk


class MyFrame(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)

        canvas = tk.Canvas(
            self,
            width=300,
            height=200)
        canvas.create_rectangle(0, 0, 300, 200, fill="red")
        canvas.pack()

        button_texts = ['hello', 'world', 'goodbye', 'mars']

        for i, button_text in enumerate(button_texts):
            button = tk.Button(text=button_text)
            button.bind("<Button-1>", self.onclickButton)

            canvas.create_window(
                100, 50 + 30 * i,
                window=button,
            )

    def onclickButton(self, evt):
        evt.widget.config(padx=100)
        print(evt.widget.cget('text'))


root = tk.Tk()
root.geometry("500x300+10+0")
MyFrame(root).pack()
root.mainloop()
