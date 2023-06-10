#import RPi.GPIO as GPIO
from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
from tkinter import *
from time import sleep
OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\at339\Desktop\IFproject\BjetController\Gui\build\assets2\frame0")
def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

ls_font_name = "Slabo 13px"

LS1X=13
LS2X=12
LS3Y=4
LS4Y=6
LS5Z = 13 #connect limit switch to any empty port
LS6Z = 14
LS7F = 15
LS8F = 21
LS_safety = True

#----condition of each Limit switch------

lsX_plusS = True
lsY_plusS = True
lsZ_plusS = True
lsF_plusS = True
lsX_minusS = True
lsY_minusS = True
lsZ_minusS = True
lsF_minusS = True

#----mode of each variable-----


opened = 0
enableX_plus = True
enableY_plus = True
enableZ_plus = True
enableF_plus = True
enableX_minus = True
enableY_minus = True
enableZ_minus = True
enableF_minus = True

condition = True #condition for normally controlled circuite

# GPIO.setwarnings(False)
# GPIO.setmode(GPIO.BCM)

# GPIO.setup(LS1X,GPIO.IN)
# GPIO.setup(LS2X,GPIO.IN)
# GPIO.setup(LS3Y,GPIO.IN)
# GPIO.setup(LS4Y,GPIO.IN)
# GPIO.setup(LS5Z,GPIO.IN)
# GPIO.setup(LS6Z,GPIO.IN)
# GPIO.setup(LS7F,GPIO.IN)
# GPIO.setup(LS8F,GPIO.IN)

temp1X = True
temp1Y = True
temp1Z = True
temp1F = True
temp2X = True
temp2Y = True
temp2Z = True
temp2F = True


    
def ls_safety():
    global lsX_plusS
    global lsY_plusS
    global lsZ_plusS
    global lsF_plusS
    global lsX_minusS
    global lsY_minusS
    global lsZ_minusS
    global lsF_minusS
    
    if enableX_plus == False: lsX_plusS = True
    elif enableX_plus:
        if temp1X == condition: lsX_plusS = True
        else: lsX_plusS = False
        
    if enableY_plus == False: lsY_plusS = True
    elif enableY_plus:
        if temp1Y == condition: lsY_plusS = True
        else: lsY_plusS = False
        
    if enableZ_plus == False: lsZ_plusS = True
    elif enableZ_plus:
        if temp1Z == condition: lsZ_plusS = True
        else: lsZ_plusS = False
        
    if enableF_plus == False: lsF_plusS = True
    elif enableF_plus:
        if temp1F == condition: lsF_plusS = True
        else: lsF_plusS = False
    
    if enableX_minus == False: lsX_minusS = True
    elif enableX_minus:
        if temp2X == condition: lsX_minusS = True
        else: lsX_minusS = False
        
    if enableY_minus == False: lsY_minusS = True
    elif enableY_minus:
        if temp2Y == condition: lsY_minusS = True
        else: lsY_minusS = False
        
    if enableZ_minus == False: lsZ_minusS = True
    elif enableZ_minus:
        if temp2Z == condition: lsZ_minusS = True
        else: lsZ_minusS = False
        
    if enableF_minus == False: lsF_minusS = True
    elif enableF_minus:
        if temp2F == condition: lsF_minusS = True
        else: lsF_minusS = False
        



def check():
    
    root = Toplevel()
    root.geometry("344x503")
    root.configure(bg = "#EEEEEE")
    
    global condition
    
    global lsX_plusS
    global lsY_plusS
    global lsZ_plusS
    global lsF_plusS
    global lsX_minusS
    global lsY_minusS
    global lsZ_minusS
    global lsF_minusS
    
    
    global enableX_plus
    global enableY_plus
    global enableZ_plus
    global enableF_plus
    global enableX_minus
    global enableY_minus
    global enableZ_minus
    global enableF_minus
    
    enableX_plusVar= IntVar()
    enableY_plusVar= IntVar()
    enableZ_plusVar= IntVar()
    enableF_plusVar= IntVar()
    enableX_minusVar= IntVar()
    enableY_minusVar= IntVar()
    enableZ_minusVar= IntVar()
    enableF_minusVar= IntVar()
    opened = IntVar()
    
    #-------setting mode of limit swtiches--------

    enableX_plusVar.set(int(enableX_plus))
    enableY_plusVar.set(int(enableY_plus))
    enableZ_plusVar.set(int(enableZ_plus))
    enableF_plusVar.set(int(enableF_plus))
    enableX_minusVar.set(int(enableX_minus))
    enableY_minusVar.set(int(enableY_minus))
    enableZ_minusVar.set(int(enableZ_minus))
    enableF_minusVar.set(int(enableF_minus))
    if condition: opened.set(0)
    else: opened.set(1)
    
    
    
    
    if opened.get() == 1: 
        condition = False
    else: 
        condition = True
    
    if condition: lsX_plus = "#05FF00"
    else: lsX_plus = "#FF0000"
    
    if condition: lsX_minus = "#05FF00"
    else: lsX_minus = "#FF0000"
    
    if condition: lsY_plus = "#05FF00"
    else: lsY_plus = "#FF0000"
    
    if condition: lsY_minus = "#05FF00"
    else: lsY_minus = "#FF0000"
    
    if condition: lsZ_plus = "#05FF00"
    else: lsZ_plus = "#FF0000"
    
    if condition: lsZ_minus = "#05FF00"
    else: lsZ_minus = "#FF0000"
    
    if condition: lsX_plus = "#05FF00"
    else: lsX_plus = "#FF0000"
    
    if condition: lsF_plus = "#05FF00"
    else: lsF_plus = "#FF0000"
    
    if condition: lsF_minus = "#05FF00"
    else: lsF_minus = "#FF0000"           
    
    
                                            
 
                                             
 
    global btnDone
    global btnUpdate
    global xsfc
    global ysfc
    global zsfc
    global fsfc
    global xsfc2
    global ysfc2
    global zsfc2
    global fsfc2
    
    

    def ftnDone():
        global LS_safety
        LS_safety = True
        root.destroy()
        
    canvas = Canvas(
        root,
        bg = "#EEEEEE",
        height = 503,
        width = 344,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge"
    )

    canvas.place(x = 0, y = 0)
    button_image_1 = PhotoImage(
        file=r"C:\Users\at339\Desktop\IFproject\BjetController\code\Program\assets2\frame0\button_1.png")
    btnDone = Button(
        root,
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: ftnDone(),
        relief="flat"
    )
    btnDone.place(
        x=259.0,
        y=471.8125,
        width=77.85897064208984,
        height=24.3309326171875
    )
    
    btnUpdate_img = PhotoImage(
        file=r"C:\Users\at339\Desktop\IFproject\BjetController\code\Program\assets2\frame0\checkpng.png")
    btnUpdate = Button(
        root,
        image=btnUpdate_img,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: update(),
        relief="flat"
    )
    btnUpdate.place(
        x=179,
        y=471.8125,
        width=77.85897064208984,
        height=24.3309326171875
    )
    
    # opened = IntVar()
    # enableX_plus= IntVar()
    # enableY_plus= IntVar()
    # enableZ_plus= IntVar()
    # enableF_plus= IntVar()
    condition = Checkbutton( root, text = 'Opened', variable = opened, font= ('Slabo13px Regular',14), )
    condition.place( x=122, y= 404)
    
    xsfc = Checkbutton( root, variable = enableX_plusVar)
    xsfc.place( x=110, y= 150)
    
    ysfc = Checkbutton( root, variable = enableY_plusVar )
    ysfc.place( x=110, y= 211)
    
    zsfc = Checkbutton( root, variable = enableZ_plusVar )
    zsfc.place( x=110 , y= 270)
    
    fsfc = Checkbutton( root, variable = enableF_plusVar )
    fsfc.place( x=110, y= 329)
    
    xsfc2 = Checkbutton( root, variable = enableX_minusVar).place( x=300, y= 150)
    
    ysfc2 = Checkbutton( root, variable = enableY_minusVar ).place( x=300, y= 211)
    
    zsfc2 = Checkbutton( root, variable = enableZ_minusVar ).place( x=300, y= 270)
    
    fsfc2 = Checkbutton( root, variable = enableF_minusVar ).place( x=300, y= 329)
    
    
    canvas.create_text(
        65.0,
        144.57691955566406,
        anchor="nw",
        text="X",
        fill="#000000",
        font=(ls_font_name, 25 * -1)
    )

    

    canvas.create_text(
        65.0,
        320.59613037109375,
        anchor="nw",
        text="F",
        fill="#000000",
        font=(ls_font_name, 25 * -1)
    )

    

    canvas.create_text(
        65.0,
        261.923095703125,
        anchor="nw",
        text="Z",
        fill="#000000",
        font=(ls_font_name, 25 * -1)
    )

    
    canvas.create_text(
        65.0,
        203.25,
        anchor="nw",
        text="Y",
        fill="#000000",
        font=(ls_font_name, 25 * -1)
    )

    canvas.create_text(
        82.0,
        49.0,
        anchor="nw",
        text="Limit Switches Status",
        fill="#000000",
        font=(ls_font_name, 19 * -1)
    )

    canvas.create_text(
        169.0,
        104.0,
        anchor="nw",
        text="+",
        fill="#000000",
        font=(ls_font_name, 25 * -1)
    )

    canvas.create_text(
        251.0,
        104,
        anchor="nw",
        text="-",
        fill="#000000",
        font=(ls_font_name, 25 * -1)
    )

    canvas.create_text(
        122.0,
        404.0,
        anchor="nw",
        text="Opened",
        fill="#000000",
        font=(ls_font_name, 15 * -1)
    )
    
    
    #------limit switches canvas-------
    status = Canvas(
    root,
    bg = "#EEEEEE",
    height = 260,
    width = 140,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
    )

    status.place(x = 142, y = 132)
    status.create_rectangle(
    8.442306518554688,
    12.576919555664062,
    55.52564239501953,
    59.660255432128906,
    fill=lsX_plus,
    outline="black")

    status.create_rectangle(
        85.94871520996094,
        12.576919555664062,
        133.03205108642578,
        59.660255432128906,
        fill=lsX_minus,
        outline="black")
    

    status.create_rectangle(
        8.442306518554688,
        71.25,
        55.52564239501953,
        118.33333587646484,
        fill=lsY_plus,
        outline="black")

    status.create_rectangle(
        85.94871520996094,
        71.25,
        133.03205108642578,
        118.33333587646484,
        fill=lsY_minus,
        outline="black")
    
    status.create_rectangle(
        8.442306518554688,
        129.923095703125,
        55.52564239501953,
        177.00643157958984,
        fill=lsZ_plus,
        outline="black")

    status.create_rectangle(
        85.94871520996094,
        129.923095703125,
        133.03205108642578,
        177.00643157958984,
        fill=lsZ_minus,
        outline="black")

    status.create_rectangle(
        8.442306518554688,
        188.59613037109375,
        55.52564239501953,
        235.6794662475586,
        fill=lsF_plus,
        outline="black")

    status.create_rectangle(
        85.94871520996094,
        188.59613037109375,
        133.03205108642578,
        235.6794662475586,
        fill=lsF_minus,
        outline="black")
    
    

    
    
    def update():
        status.delete()
        #------display-------
        global lsX_plus 
        global lsX_minus 
        global lsY_plus 
        global lsY_minus 
        global lsZ_plus 
        global lsZ_minus 
        global lsF_plus 
        global lsF_minus
        
        
        global condition
        
        global enableX_plus
        global enableY_plus
        global enableZ_plus
        global enableF_plus
        global enableX_minus
        global enableY_minus
        global enableZ_minus
        global enableF_minus
        
        #-------updating conditions from checkboxes---------
        
        enableX_plus = bool(enableX_plusVar.get())
        enableY_plus = bool(enableY_plusVar.get())
        enableZ_plus = bool(enableZ_plusVar.get())
        enableF_plus = bool(enableF_plusVar.get())
        enableX_minus = bool(enableX_minusVar.get())
        enableY_minus = bool(enableY_minusVar.get())
        enableZ_minus = bool(enableZ_minusVar.get())
        enableF_minus = bool(enableF_minusVar.get())
        
        
        
        if opened.get() == 1: condition = False
        else: condition = True
        
        #----updating display-------
        
        if temp1X == condition: lsX_plus = "#05FF00"
        else: lsX_plus = "#FF0000"
        
        if temp2X ==condition: lsX_minus = "#05FF00"
        else: lsX_minus = "#FF0000"
        
        if temp1Y ==condition: lsY_plus = "#05FF00"
        else: lsY_plus = "#FF0000"
        
        if temp2Y ==condition: lsY_minus = "#05FF00"
        else: lsY_minus = "#FF0000"
        
        if temp1Z == condition: lsZ_plus = "#05FF00"
        else: lsZ_plus = "#FF0000"
        
        if temp2Z == condition: lsZ_minus = "#05FF00"
        else: lsZ_minus = "#FF0000"
    
        
        if temp1F == condition: lsF_plus = "#05FF00"
        else: lsF_plus = "#FF0000"
        
        if temp2F == condition: lsF_minus = "#05FF00"
        else: lsF_minus = "#FF0000"
        
        
        status.create_rectangle(
            8.442306518554688,
            12.576919555664062,
            55.52564239501953,
            59.660255432128906,
            fill=lsX_plus,
            outline="black")
        
        status.create_rectangle(
            85.94871520996094,
            12.576919555664062,
            133.03205108642578,
            59.660255432128906,
            fill=lsX_minus,
            outline="black")
        

        status.create_rectangle(
            8.442306518554688,
            71.25,
            55.52564239501953,
            118.33333587646484,
            fill=lsY_plus,
            outline="black")

        status.create_rectangle(
            85.94871520996094,
            71.25,
            133.03205108642578,
            118.33333587646484,
            fill=lsY_minus,
            outline="black")
        
        status.create_rectangle(
            8.442306518554688,
            129.923095703125,
            55.52564239501953,
            177.00643157958984,
            fill=lsZ_plus,
            outline="black")

        status.create_rectangle(
            85.94871520996094,
            129.923095703125,
            133.03205108642578,
            177.00643157958984,
            fill=lsZ_minus,
            outline="black")

        status.create_rectangle(
            8.442306518554688,
            188.59613037109375,
            55.52564239501953,
            235.6794662475586,
            fill=lsF_plus,
            outline="black")

        status.create_rectangle(
            85.94871520996094,
            188.59613037109375,
            133.03205108642578,
            235.6794662475586,
            fill=lsF_minus,
            outline="black")
        
    # sleep(30)
    # root.destroy()
    
    root.resizable(False, False)
    root.mainloop()


if __name__ == '__main__':
    check()