from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, Label
from tkinter import *
from time import sleep
OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\at339\Desktop\IFproject\BjetController\code\Program\assets3\frame0")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


cs_font_name = "Slabo 13px"

Zclear = True
Fclear = True
mZ_clear = False
mF_clear = False
P_head = 50 #difference between print head and chamber length
C_move  = ''

    

def get_warning(str):
    global btnMove
    global btnDone
    window = Tk()

    window.geometry("387x115")
    window.configure(bg = "#EEEEEE")
    
    Display = ''
    def ftnM_clear ():
        global C_move
        if str != 'Fill Feed':
            C_move = str
        window.destroy()
        
    def ftnDone():
        global Zclear
        global Fclear
        if str == 'Z':
            Zclear = True
        elif str == 'Feed':
            Fclear = True
        elif str == 'Fill Feed':
            Fclear = False
        window.destroy()    
        
            
    canvas = Canvas(window,
        bg = "#EEEEEE",
        height = 155,
        width = 387,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge")
    canvas.place(x = 0, y = 0)
    
    

    
    btnMove = Button(
        window,
        borderwidth = 1,
        border = 1,
        bg= '#E2E2E2',
        text= 'Move to clear',
        font=(cs_font_name, 15 * -1),
        command=lambda: ftnM_clear(),
        relief="solid"
        
    )
    btnMove.place( x=69.0,y=65.0,width=110.81415557861328,height=30.406070709228516)

    btnDone = Button(
        window,
        borderwidth = 1,
        border = 1,
        bg= '#E2E2E2',
        text= 'Done',
        font=(cs_font_name, 15 * -1),
        command=lambda: ftnDone(),
        relief="solid"
    )
    btnDone.place(
        x=201.0,
        y=65,
        width=110.81414794921875,
        height=30.406070709228516
    )
    if str == 'Fill Feed': 
        Text=  "Please fill the feed"
        Dislay = 'Done'
        btnMove.config(state = 'disabled')
    elif str == 'Print Head': 
        Text = "Please move the print head"
        btnMove.config(state = 'disabled')
    else: 
        Text = f"is the {str} chamber cleared?"
        Display = 'Cleared'
        btnMove.config(state = 'active')
    canvas.create_text(
        70,
        19,
        anchor="nw",
        text=Text,
        fill="#000000",
        justify = 'center',
        font=(cs_font_name, 16 * -1)
    )

    sleep(5)
    window.destroy()

    window.resizable(False, False)
    window.mainloop()
    
    
    
    
    
    
def check_chamber():
    checkChamber = Toplevel()

    checkChamber.geometry("345x227")
    checkChamber.configure(bg = "#EEEEEE")
    global Zclear
    global Fclear
    global Fclear
    global zcheck
    global fcheck
    global button_1
    global button_2
    global button_3

    
    fs = IntVar()
    zs = IntVar()
    
    
    
    def ftnUpdate():
        global Zclear
        global Fclear
        update.delete('all')
        if zs.get() == 0: Zclear = False
        elif zs.get() == 1: Zclear = True
        if fs.get() == 0: Fclear = False
        elif fs.get() == 1: Fclear = True
        tempZ = ''
        tempF = ''
        if Zclear: tempZ = 'Cleared'
        else: tempZ = 'Not Cleared'
        if Fclear: tempF = 'Cleared'
        else: tempF = 'Not Cleared'
        update.create_text(
        0,
        0,
        anchor="nw",
        text=tempZ,
        fill="#000000",
        font=(cs_font_name, 16 * -1)
    )
        update.create_text(
        0,
        29,
        anchor="nw",
        text=tempF,
        fill="#000000",
        font=(cs_font_name, 16 * -1)
        )
        
        
    def ftnZ():
        global C_move
        C_move= 'Z'
        checkChamber.destroy()
    def ftnFeed():
        global C_move
        C_move = 'F'
        checkChamber.destroy()
        
    canvas = Canvas(
        checkChamber,
        bg = "#EEEEEE",
        height = 227,
        width = 345,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge"
    )

    canvas.place(x = 0, y = 0)
    button_image_1 = PhotoImage(
        file=relative_to_assets("button_1.png"))
    button_1 = Button(
        checkChamber,
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: ftnUpdate(),
        relief="flat"
    )
    if Zclear: 
        tempZ = 'Cleared'
        zs.set(1)
    else: 
        tempZ = 'Not Cleared'
        zs.set(0)
    fs.set(0)
    if Fclear: 
        tempF = 'Cleared'
        fs.set(1)
    else: 
        tempF = 'Not Cleared'
        fs.set(0)
    
    update = Canvas(checkChamber,
        bg = "#EEEEEE",
        height = 55,
        width = 90,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge")
    update.place(x = 221, y = 61)
    update.create_text(
        0,
        0,
        anchor="nw",
        text=tempZ,
        fill="#000000",
        font=(cs_font_name, 16 * -1)
    )

    update.create_text(
        0,
        29,
        anchor="nw",
        text=tempF,
        fill="#000000",
        font=(cs_font_name, 16 * -1)
    )
    button_1.place(
        x=135.0,
        y=123.0,
        width=77.09459686279297,
        height=27.593929290771484
    )

    canvas.create_text(
        120.0,
        28.0,
        anchor="nw",
        text="Clear? ",
        fill="#000000",
        font=(cs_font_name, 18 * -1)
    )

    canvas.create_text(
        35.0,
        60.0,
        anchor="nw",
        text="Z",
        fill="#000000",
        font=(cs_font_name, 18 * -1)
    )

    canvas.create_text(
        35.0,
        91.0,
        anchor="nw",
        text="Feed",
        fill="#000000",
        font=(cs_font_name, 18 * -1)
    )
    
    # canvas.create_text(
    #     221.0,
    #     61.0,
    #     anchor="nw",
    #     text="1cleared",
    #     fill="#000000",
    #     font=(cs_font_name, 16 * -1)
    # )

    # canvas.create_text(
    #     219.0,
    #     90.0,
    #     anchor="nw",
    #     text="1uncleared",
    #     fill="#000000",
    #     font=(cs_font_name, 16 * -1)
    # )

    canvas.create_text(
        219.0,
        27.0,
        anchor="nw",
        text="Status",
        fill="#000000",
        font=(cs_font_name, 18 * -1)
    )
    
    zcheck = Checkbutton( checkChamber, variable = zs).place(x=125, y = 61)
    fcheck = Checkbutton( checkChamber,variable = fs).place(x=125, y = 90)
    

    canvas.create_text(
        34.0,
        185.0,
        anchor="nw",
        text="Clear: ",
        fill="#000000",
        font=(cs_font_name, 18 * -1)
    )

    button_image_2 = PhotoImage(
        file=relative_to_assets("button_2.png"))
    button_2 = Button(
        checkChamber,
        image=button_image_2,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: ftnZ(),
        relief="flat"
    )
    button_2.place(
        x=135.0,
        y=180.0,
        width=77.09459686279297,
        height=24.406070709228516
    )

    button_image_3 = PhotoImage(
        file=relative_to_assets("button_3.png"))
    button_3 = Button(
        checkChamber,
        image=button_image_3,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: ftnFeed(),
        relief="flat"
    )
    button_3.place(
        x=226.0,
        y=180.0,
        width=77.0946044921875,
        height=24.406070709228516
    )
    checkChamber.resizable(False, False)
    checkChamber.mainloop()    
# def fill_feed():
if __name__ == '__main__':
    get_warning('Z')
    get_warning('Feed')
    get_warning('Fill Feed')
    