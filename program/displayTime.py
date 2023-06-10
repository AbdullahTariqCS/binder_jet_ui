from tkinter import Tk, ttk, Label, Canvas
window = Tk()
time_value = 0
time_canvas = Canvas(
        window,
        bg = "#2B2D2E",
        height = 463-(17*20),
        width = 294,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge"
    )
time_canvas.place(x= 1056, y =50+(17*20)+11)
# def Progress_bar():

def display():
    global time_text 
    time_text = Label(time_canvas, text = f'Estimated time: {time_value} H', font=("Cascadia Code", 15 * -1)).place(x = 16.0, y = (17*1)+11, )
    exe_progress -= ttk.Progressbar(time_canvas, orient = 'horizontal', lentgth = 100, mode = "determinate")
window.mainloop()