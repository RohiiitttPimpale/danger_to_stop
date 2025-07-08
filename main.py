from tkinter import *


def count_down(count,old_text=None):

    new_text = textbox.get("1.0",END)
    if not new_text == old_text:
        count= 0
    else:
        if count == 5:
            textbox.delete("1.0","end")
            count = 0
    window.after(1000,count_down,count+1,new_text)

window = Tk()
window.title("Danger_when_stop")
window.config(height=500,width=500,pady=20,padx=20)

label = Label(text="Keep writing, otherwise after 5s all text will delete")
label.config(font=("Arial", 15,"bold"))
label.pack()

textbox = Text()
textbox.pack()

count_down(0)
window.mainloop()