from pathlib import Path
from tkinter import Tk,ttk, Canvas, Entry, Text, Button, PhotoImage, Listbox
from tkinter import *
from time import sleep
from PIL import Image
import path as p
import Controller as C
import Calibration as Cb
import ChamberStatus as CS
import ToolpathGenerator as TP
import LScheck
import threading
path = p.program_path
# OUTPUT_PATH = Path(__file__).parent
# ASSETS_PATH = OUTPUT_PATH / Path(r"\assets\frame0")
# def relative_to_assets(path: str) -> Path:
#     return ASSETS_PATH / Path(path)

window = Tk()
window.geometry("1366x768")
window.configure(bg = "#EEEEEE")
window.title('CNC-ME')


font_name = p.main_font
#---------button functions-----------
stringCng = 0
print_numberCng = 0
ln_cng = 0
current_positionCng = {'X':0.00, 'Y':0.00, 'Z':0.00, 'F':0.00}
tempJ = C.home_position
progress_barValue = 0
progress = 0
time_rem = StringVar()
pointer_position = {'X':0.00, 'Y':0.00}
pnt_gcode = False

def bg_ftns():
    global stringCng
    global print_numberCng
    global current_positionCng
    global progress
    global btnMove
    global btnX_plus
    global btnX_minus
    global btnXY_plus
    global btnXY_minus
    global btnXY_plusMinus
    global btnXY_minusplus
    global ln_cng
    global pnt_gcode
    while True:
        if len(C.stringC)!= stringCng:
            # if stringCng == 5:
            #     stringCng = 0
            for i in range (stringCng, len(C.stringC)):
                # if C.stringC[i] != '':
                    print_command(f'{C.stringC[i]} ({threading.active_count()})')
            if len(C.stringC) > 10: C.stringC = []
            stringCng = len(C.stringC)
            # stringCng = C.stringCount
            # if stringCng == 5:
            #     stringCng = 0
            
        #LScheck.ls_safety()
        
        #enabling and disabling buttons 
        if C.x_true:
            btnX_plus.config(state= 'disabled')
            btnX_minus.config(state = 'disabled')
        else:
            btnX_plus.config(state= 'active')
            btnX_minus.config(state = 'active')


        if C.y_true:
            btnY_plus.config(state= 'disabled')
            btnY_minus.config(state = 'disabled')
        else: 
            btnY_plus.config(state= 'active')
            btnY_minus.config(state = 'active')
        
            
        if C.z_true:
            btnZ_minus.config(state = 'disabled')
            btnZ_plus.config(state = 'disabled')
        else:
            btnZ_minus.config(state = 'active')
            btnZ_plus.config(state = 'active')
            
        if C.f_true:
            btnF_minus.config(state = 'disabled')
            btnF_plus.config(state = 'disabled')
        else:
            btnF_minus.config(state = 'active')
            btnF_plus.config(state = 'active')
        
        if C.x_true or C.y_true or C.z_true or C.f_true:  btnMove.config(state = 'disabled')
        else : btnMove.config(state = 'active')
        
        if C.x_true or C.y_true:
            btnXY_plus.config(state = 'disabled')
            btnXY_minusplus.config(state= 'disabled')
            btnXY_plusMinus.config(state= 'disabled')
            btnXY_minus.config(state= 'disabled')
        else:
            btnXY_plus.config(state = 'active')
            btnXY_minusplus.config(state= 'active')
            btnXY_plusMinus.config(state= 'active')
            btnXY_minus.config(state= 'active')
            
        #toolpath animation
        if current_positionCng['X']!= C.current_position['X'] and current_positionCng['Y']!= C.current_position['Y']:
            tp_Animate(C.current_position['X']-pointer_position['X'], C.current_position['Y']-pointer_position['Y'])
            current_positionCng['X'] = C.current_position['X'] 
            current_positionCng['Y'] = C.current_position['Y'] 
            
        elif current_positionCng['X']!= C.current_position['X'] and current_positionCng['Y']== C.current_position['Y']:
            tp_Animate(C.current_position['X']-pointer_position['X'], 0)
            current_positionCng['X'] = C.current_position['X'] 
           
        elif current_positionCng['X']== C.current_position['X'] and current_positionCng['Y']!= C.current_position['Y']:
            tp_Animate(0, C.current_position['Y']-pointer_position['Y'])
            current_positionCng['Y'] = C.current_position['Y'] 
        
        if TP.toolpath[C.print_number]['M'] == 101:
            M01()
        
        #gcode window update
        # print(C.print_number)
        # print('Toolpath: ' ,end = '')
        # print (TP.toolpath[C.print_number]['N'])
        # print (f'ln_cng: {ln_cng}')
        # if TP.toolpath[C.print_number]['N'] != ln_cng:
        #     # print('-----------')
        #     # print(ln_cng)
        #     # print(TP.toolpath[C.print_number]['LN'])

        #     point_gcode()
        #     ln_cng  += 1
        
        
        
        #current postion viewer
        tempx = round(C.current_position['X'],2)
        x_cPosition.set(f'{tempx} mm')

        tempy = round(C.current_position['Y'],2)
        y_cPosition.set(f'{tempy} mm')
        
        tempz = round(C.current_position['Z'],2)
        z_cPosition.set(f'{tempz} mm')
        
        tempf = round(C.current_position['F'],2)
        f_cPosition.set(f'{tempf} mm')
            
        #progress bar update
        if C.print_number != print_numberCng:
            time_rem.set(f'Estimated Time: {C.print_time[TP.toolpath_number - 2 - C.print_number]} H')
            progress += progress_barValue
            progress_var.set(progress)
            print_numberCng += 1
        sleep(0.016)
        

def bg_jogAnimate():
    #jog animation 
    while True:
        # if tempJ['X'] != C.current_position['X']: 
        #     x_animate(C.current_position['X']-tempJ['X'])
        #     tempJ['X'] = C.current_position['X']
        if abs(tempJ['X'] - C.current_position['X']) > 4: 
            x_animate(C.current_position['X']-tempJ['X'])
            tempJ['X'] = C.current_position['X']
            
        if abs(tempJ['Y'] - C.current_position['Y']) > 4: 
            y_animate(C.current_position['Y']- tempJ['Y'])
            tempJ['Y'] = C.current_position['Y']
            
        if tempJ['Z'] != C.current_position['Z']: 
            z_animate(C.current_position['Z']- tempJ['Z'])
            tempJ['Z'] = C.current_position['Z']
            
        if tempJ['F'] != C.current_position['F']: 
            f_animate(C.current_position['F']- tempJ['F'])
            tempJ['F'] = C.current_position['F']
        if C.print_stat: point_gcode(TP.toolpath[C.print_number]['N'])
        
#-------------animation functions--------------

def x_animate(x):
    if x < 0: 
        animate_jog_top.move(x_view, 1 , 0)
        animate_jog_top.move(y_view, 1, 0)
        # sleep(1.75) 
    elif x > 0: 
        animate_jog_top.move(x_view, -1, 0)
        animate_jog_top.move(y_view, -1, 0)
        # sleep(1.75) 
    return 
    
            
def y_animate(y):
    if y < 0: 
        animate_jog_top.move(y_view, 0 , 1)
        # sleep(1.2) 
            
    elif y > 0: 
        animate_jog_top.move(y_view, 0, -1)
        # sleep(1.2)
            
            
def z_animate(z):
    if z < 0: 
        animate_jog_side.move(z_view, 0, -1)
        sleep(2.8) 
        
            
    
    elif z > 0: 
        animate_jog_side.move(z_view, 0, 1)
        sleep(2.8) 
            
            
def f_animate(f):
    if f < 0: 

        animate_jog_side.move(f_view, 0, -1)
        sleep(2.8) 
            
    
    elif f > 0: 
        animate_jog_side.move(f_view, 0, 1)
        sleep(2.8) 

#toolpathAnimation 

def tp_Animate(x, y):
    # toolpathview.move(pointer, round(1.4*x,0), -round(1.4*y,0))
    global pointer_image
    global pointer
    global pointer_position
    
    toolpathview.delete('p')
    pointer_image = PhotoImage(file=f"{path}{path}assets/frame0/pointer-01.png")
    pointer = toolpathview.create_image(
        1.288*(60.0+y+pointer_position['Y']),
        1.288*(340-x-pointer_position['X']),
        image = pointer_image,
        tags = 'p'
    )
    pointer_position['X'] += x
    pointer_position['Y'] += y
    
def M01():
    toolpathview.create_rectangle(
        1.288*(60+pointer_position['Y'])-1,
        1.288*(340-pointer_position['X'])-1,
        1.288*(60+pointer_position['Y'])+1,
        1.288*(340-pointer_position['X'])+1,
        fill= 'black',
        tags = 'M01'
        
    )
#------Button functions--------
        
def ftnLoad_gcode():
    btnLoad_gcode.config(state = 'disabled')
    global gcode_getline
    global progress_barValue
    global pnt_gcode
    gcode_getline = []
    
    C.printC('Loading G code')
    TP.GCODE()
    TP.tp_visualizer()
    toolpathview.delete('M01')
    view_layer(1)
    
    gcode_getline = TP.gcode_line
    for i in range (0,10): gcode_getline.append('')
    # point_gcode()
    # pnt_gcode = True
    
    C.print_timeCalculator()
    time_rem.set(f'Estimated Time {C.print_time[len(C.print_time)-1]} H')
    progress_barValue = 100/TP.toolpath_number
    print(f'progress bar value {progress_barValue}')
    
    print_gcode()
    C.printC('Gcode has been loaded')
    btnLoad_gcode.config(state = 'active')
    return 
    

def ftnLS_check():
    LScheck.check()

def ftnC_status():
    print(CS.Zclear)
    CS.check_chamber()
    # C.clear_chamber(CS.C_move)
    
def ftnPrint():
    # display_time(0)
    global pnt_gcode
    threading.Thread(target= C.start_print).start()
    pnt_gcode = True

def ftnRes_print():
    C.printC('Resuming Print')
    C.print_backup()
    C.print_timeCalculator(C.res_printLine)
    C.start_print(C.res_printLine)
    
    
def ftnView_tp():
    LN = 0
    if z_variable != '':
        z = float(z_variable.get())
    else: 
        z = 0
    for i in range(0 , TP.toolpath_number):
        if TP.toolpath[i]['Z'] == z:
            LN = TP.toolpath[i]['LN']
    
    view_layer(int(LN))
       
def view_layer(l = 0):
    global layer_image
    global layer_view
    print('Viewing layer')
    toolpathview.delete('bg')
    # layer_view.destory
    layer_image = PhotoImage(file=f"{path}{path}assets/frame0/layer_{l}.png")
    layer_view = toolpathview.create_image(
        299,
        232,
        image = layer_image,
        tags = 'bg'
        )
    tp_Animate(C.current_position['X'], C.current_position['Y'])
    
def ftnResume():
    global x_input 
    global y_input 
    global z_input 
    global f_input 
    C.xy_move(x_input - C.current_position['X'], y_input - C.current_position['Y'])
    C.z_move(z_input - C.current_position['Z'])
    C.f_move(f_input- C.current_position['F'] )
    
#--------Jog controllers--------
x_input = 10.00 + Cb.x_cf
y_input = 10.00 + Cb.y_cf 
z_input = 10.00 + Cb.z_cf
f_input = 10.00 + Cb.f_cf


def ftnMove():
    global x_input
    global y_input
    global z_input
    global f_input
    global x_variable
    global y_variable
    global z_variable
    global f_variable
    if x_variable.get() != '':
        x_input = float(x_variable.get()) + Cb.x_cf
        
    if y_variable.get() != '':
        y_input = float(y_variable.get()) + Cb.y_cf
        
    if z_variable.get() != '':
        z_input = float(z_variable.get()) + Cb.z_cf
        
    if f_variable.get() != '':
        f_input = float(f_variable.get()) + Cb.f_cf
    
    if x_variable.get() != '' and y_variable.get() == '': 
        threading.Thread(target= C.x_move, args= (x_input-C.current_position['X'],2)).start()
    
    elif x_variable.get() == '' and y_variable.get() != '': 
        threading.Thread(target= C.y_move, args= (y_input-C.current_position['Y'],2)).start()

    
    elif x_variable.get() != '' and y_variable.get() != '': 
        threading.Thread(target= C.xy_move, args= (x_input-C.current_position['X'],y_input-C.current_position['Y'])).start()
          
    
    if z_variable.get() !='':
        threading.Thread(target = C.z_move, args = [(z_input-C.current_position['Z'])]).start()
        
    if f_variable.get() !='': 
        threading.Thread(target = C.f_move, args= [(f_input-C.current_position['F'])]).start()

#-----

def ftnX_plus():
    threading.Thread(target= C.x_move, args= (abs(x_input),2)).start()
   
def ftnX_minus():
    threading.Thread(target= C.x_move, args= (-abs(x_input),2)).start()
            

def ftnY_plus():
    threading.Thread(target= C.y_move, args= (abs(y_input),2)).start()

def ftnY_minus():
    threading.Thread(target= C.y_move, args= (-abs(y_input),2)).start()

#----
 
def ftnZ_plus():
    threading.Thread(target = C.z_move, args = [abs(z_input)]).start()

def ftnZ_minus():
    threading.Thread(target = C.z_move, args = [-abs(z_input)]).start()


def ftnF_plus(): 
    threading.Thread(target = C.f_move, args = [abs(z_input)]).start()


def ftnF_minus():
    threading.Thread(target = C.f_move, args= [-abs(f_input)]).start()
    
#----

def ftnXY_plus():
    threading.Thread(target= C.xy_move, args= (abs(x_input),abs(y_input))).start()
    

def ftnXY_minusplus():
    threading.Thread(target= C.xy_move, args= (-abs(x_input),abs(y_input))).start()


def ftnXY_minus():
    threading.Thread(target= C.xy_move, args= (-abs(x_input),-abs(y_input))).start()


def ftnXY_plusminus():
    threading.Thread(target= C.xy_move, args= (abs(x_input),-abs(y_input))).start()

#------background fucntions-----

bgftn = threading.Thread(target= bg_ftns)
j = threading.Thread(target = bg_jogAnimate)

#------

canvas = Canvas(
    window,
    bg = "#EEEEEE",
    height = 768,
    width = 1366,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)


canvas.place(x = 0, y = 0)

canvas.create_line(415.78,0,415.78,585.87)
canvas.create_line(415.78,585.87,0,585.87)

toolpathview = Canvas(
    window,
    bg = "#EEEEEE",
    height = 464,
    width = 600,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)
toolpathview.place(x= 438,  y= 52 )
layer_image = PhotoImage(file=r"C:\Users\at339\Desktop\IFproject\BjetController\code\Program\layer_500.png")
layer_view = toolpathview.create_image(
    299,
    232,
    image = layer_image,
    tags = 'bg'
)
pointer_image = PhotoImage(file=f"assets/frame0/pointer-01.png")
pointer = toolpathview.create_image(
    1.288*60.0,
    1.288*340,
    image = pointer_image,
    tags = 'p'
)

canvas.create_text(
    166.0,  
    7.0,
    anchor="nw",
    text="Jog Mode",
    fill="#000000",
    font=(font_name, 18 * -1)
)



canvas.create_rectangle(
    1.0,
    683.0,
    422.0,
    758.0,
    fill="#2B2D2E",
    outline="")

canvas.create_rectangle(
    36.0,
    699.0,
    82.0,
    744.0,
    fill="#2C4044",
    outline="")

canvas.create_text(
    44.0,
    708.0,
    anchor="nw",
    text="Zo",
    fill="#D7F8FF",
    font=(font_name, 21 * -1)
)

canvas.create_rectangle(
    0.0,
    599.0,
    19.0,
    674.0,
    fill="#2B2D2E",
    outline="")

canvas.create_rectangle(
    0.0,
    683.0,
    19.0,
    758.0,
    fill="#2B2D2E",
    outline="")

canvas.create_rectangle(
    252.0,
    699.0,
    299.0,
    744.0,
    fill="#2C4044",
    outline="")


canvas.create_text(
    269.0,
    708.0,
    anchor="nw",
    text="F",
    fill="#D7F8FF",
    font=(font_name, 21 * -1)
)

canvas.create_text(
    787.0,
    9.0,
    anchor="nw",
    text="Binder Jet Controller",
    fill="#000000",
    font=(font_name, 21)
)

canvas.create_rectangle(
    1.0,
    599.0,
    422.0,
    674.0,
    fill="#2B2D2E",
    outline="")

canvas.create_rectangle(
    36.0,
    616.0,
    82.0,
    660.0,
    fill="#2C4044",
    outline="")

canvas.create_text(
    44.0,
    625.0,
    anchor="nw",
    text="Xo",
    fill="#D7F8FF",
    font=(font_name, 21 * -1)
)

canvas.create_rectangle(
    252.0,
    616.0,
    299.0,
    660.0,
    fill="#2C4044",
    outline="")

#-------------current Position Labels-------------

x_cPosition = StringVar()
y_cPosition = StringVar()
z_cPosition = StringVar()
f_cPosition = StringVar()

x_cPosition.set(f'0.00 mm')
y_cPosition.set(f'0.00 mm')
z_cPosition.set(f'0.00 mm')
f_cPosition.set(f'0.00 mm')

Label( window, font=(font_name, 19 * -1), textvariable= x_cPosition, fg="#D7F8FF", bg= '#2B2D2E').place(x=103, y=625)
Label( window, font=(font_name, 19 * -1), textvariable= y_cPosition, fg="#D7F8FF", bg= '#2B2D2E').place(x=319, y=625)
Label( window, font=(font_name, 19 * -1), textvariable= z_cPosition, fg="#D7F8FF", bg= '#2B2D2E').place(x=103, y=709)
Label( window, font=(font_name, 19 * -1), textvariable= f_cPosition, fg="#D7F8FF", bg= '#2B2D2E').place(x=319, y=709)


#---------------------
canvas.create_text(
    262.0,
    625.0,
    anchor="nw",
    text="Yo",
    fill="#D7F8FF",
    font=(font_name, 21 * -1)
)

canvas.create_text(
    72.0,
    452.0,
    anchor="nw",
    text="X:",
    fill="#000000",
    font=(font_name, 19 * -1)
)

canvas.create_text(
    153.0,
    452.0,
    anchor="nw",
    text="mm",
    fill="#000000",
    font=(font_name, 19 * -1)
)

canvas.create_text(
    225.0,
    452.0,
    anchor="nw",
    text="Y:",
    fill="#000000",
    font=(font_name, 19 * -1)
)

canvas.create_text(
    306.0,
    452.0,
    anchor="nw",
    text="mm",
    fill="#000000",
    font=(font_name, 19 * -1)
)

canvas.create_text(
    72.0,
    485.0,
    anchor="nw",
    text="Z:",
    fill="#000000",
    font=(font_name, 19 * -1)
)

canvas.create_text(
    153.0,
    485.0,
    anchor="nw",
    text="mm",
    fill="#000000",
    font=(font_name, 19 * -1)
)

canvas.create_text(
    225.0,
    485.0,
    anchor="nw",
    text="F:",
    fill="#000000",
    font=(font_name, 19 * -1)
)

canvas.create_text(
    306.0,
    485.0,
    anchor="nw",
    text="mm",
    fill="#000000",
    font=(font_name, 19 * -1)
)

button_image_1 = PhotoImage(
    file=f"{path}{path}assets/frame0/button_28.png")
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_1 clicked"),
    relief="flat"
)
button_1.place(
    x=755.774658203125,
    y=687.6525268554688,
    width=133.2182159423828,
    height=62.908599853515625
)

button_image_2 = PhotoImage(
    file=f"{path}{path}assets/frame0/button_3.png")
btnPrint = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: ftnPrint(),
    relief="flat"
)
btnPrint.place(
    x=610.71484375,
    y=687.6525268554688,
    width=133.2182159423828,
    height=62.908599853515625
)

button_image_3 = PhotoImage(
    file=f"{path}{path}assets/frame0/button_4.png")
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_3 clicked"),
    relief="flat"
)
button_3.place(
    x=462.694580078125,
    y=689.1326904296875,
    width=133.2182159423828,
    height=62.908599853515625
)

button_image_4 = PhotoImage(
    file=f"{path}{path}assets/frame0/button_5.png")
btnLoad_gcode = Button(
    image=button_image_4,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: threading.Thread(target=ftnLoad_gcode).start(),
    relief="flat"
)
btnLoad_gcode.place(
    x=755.774658203125,
    y=610.6819458007812,
    width=133.2182159423828,
    height=62.908599853515625
)

button_image_5 = PhotoImage(
    file=f"{path}{path}assets/frame0/button_29.png")
btnC_status = Button(
    image=button_image_5,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: ftnC_status(),
    relief="flat"
)
btnC_status.place(
    x=610.71484375,
    y=610.6819458007812,
    width=133.2182159423828,
    height=62.908599853515625
)

btnLS_img = PhotoImage(
    file=f"{path}{path}assets/frame0/button_6.png")
btnLS = Button(
    image=btnLS_img,
    borderwidth=0,
    highlightthickness=0,
    command= lambda: ftnLS_check(),
    relief="flat"
)
btnLS.place(
    x=462.694580078125,
    y=612.1621704101562,
    width=133.2182159423828,
    height=62.908599853515625
)

button_image_7 = PhotoImage(
    file=f"{path}{path}assets/frame0/button_7.png")
btnCalibrate = Button(
    image=button_image_7,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: Cb.cbWindow(),
    relief="flat"
)
btnCalibrate.place(
    x=755.0345458984375,
    y=533.7114868164062,
    width=133.2182159423828,
    height=62.908599853515625
)

btnSethome_img = PhotoImage(
    file=f"{path}{path}assets/frame0/button_8.png")
btnSethome = Button(
    image=btnSethome_img,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: C.set_home(),
    relief="flat"
)
btnSethome.place(
    x=609.9747314453125,
    y=533.7114868164062,
    width=133.2182159423828,
    height=62.908599853515625
)

btnHome_img = PhotoImage(
    file=f"{path}{path}assets/frame0/button_9.png")
btnHome = Button(
    image=btnHome_img,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: C.home(),
    relief="flat"
)
btnHome.place(
    x=462.694580078125,
    y=533.7114868164062,
    width=133.2182159423828,
    height=62.908599853515625
)

button_image_10 = PhotoImage(
    file=f"{path}{path}assets/frame0/button_30.png")
button_10 = Button(
    image=button_image_10,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print_command("button_10 clicked"),
    relief="flat"
)
button_10.place(
    x=1253.9814453125,
    y=12.493896484375,
    width=82.1512451171875,
    height=22.943145751953125
)

button_image_11 = PhotoImage(
    file=f"{path}{path}assets/frame0/button_11.png")
button_11 = Button(
    image=button_image_11,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_11 clicked"),
    relief="flat"
)
button_11.place(
    x=438.1128845214844,
    y=12.493896484375,
    width=113.9755859375,
    height=22.943145751953125
)

button_image_12 = PhotoImage(
    file=f"{path}{path}assets/frame0/button_31.png")
button_12 = Button(
    image=button_image_12,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_12 clicked"),
    relief="solid"
)
button_12.place(
    x=275.0,
    y=524.0,
    width=100.0,
    height=44.40606689453125
)

btnMove_img = PhotoImage(
    file=f"{path}{path}assets/frame0/button_13.png")
btnMove = Button(
    image=btnMove_img,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: ftnMove(),
    relief="flat"
)
btnMove.place(
    x=42.0,
    y=524.0,
    width=100.0,
    height=44.40606689453125
)

button_image_14 = PhotoImage(
    file=f"{path}{path}assets/frame0/button_14.png")
btnView_tp = Button(
    image=button_image_14,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: ftnView_tp(),
    relief="flat"
)
btnView_tp.place(
    x=158.0,
    y=524.0,
    width=100.0,
    height=44.40606689453125
)

x_variable = StringVar()
y_variable = StringVar()
z_variable = StringVar()
f_variable = StringVar()
entry_image_1 = PhotoImage(
    file=f"{path}{path}assets/frame0/entry_1.png")
entry_bg_1 = canvas.create_image(
    121.5,
    460.0,
    image=entry_image_1
)

entryX = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0,
    textvariable = x_variable
)
entryX.place(
    x=98.0,
    y=449.0,
    width=47.0,
    height=20.0
)

entry_image_2 = PhotoImage(
    file=f"{path}{path}assets/frame0/entry_2.png")
entry_bg_2 = canvas.create_image(
    274.0,
    460.0,
    image=entry_image_2
)

entryY = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0,
    textvariable= y_variable
)
entryY.place(
    x=250.0,
    y=449.0,
    width=48.0,
    height=20.0
)

entry_image_3 = PhotoImage(
    file=f"{path}{path}assets/frame0/entry_3.png")
entry_bg_3 = canvas.create_image(
    121.5,
    493.0,
    image=entry_image_3
)
entryZ = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0,
    textvariable= z_variable
)
entryZ.place(
    x=98.0,
    y=482.0,
    width=47.0,
    height=20.0
)

entry_image_4 = PhotoImage(
    file=f"{path}{path}assets/frame0/entry_4.png")
entry_bg_4 = canvas.create_image(
    274.0,
    493.0,
    image=entry_image_4
)
entryF = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0,
    textvariable = f_variable
)
entryF.place(
    x=250.0,
    y=482.0,
    width=48.0,
    height=20.0
)

btnZ_plus_img = PhotoImage(
    file=f"{path}{path}assets/frame0/button_15.png")
btnZ_plus = Button(
    image=btnZ_plus_img,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: ftnZ_plus(),
    relief="flat"
)
btnZ_plus.place(
    x=368,
    y=369.4089937210083,
    width=25.9,
    height=56
)

btnF_plus_img = PhotoImage(
    file=f"{path}{path}assets/frame0/button_16.png")
btnF_plus = Button(
    image=btnF_plus_img,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: ftnF_plus(),
    relief="flat"
)
btnF_plus.place(
    x=23,
    y=369.4089937210083,
    width=25.9,
    height=56
)

btnZ_minus_img = PhotoImage(
    file=f"{path}{path}assets/frame0/button_17.png")
btnZ_minus = Button(
    image=btnZ_minus_img,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: ftnZ_minus(),
    relief="flat"
)
btnZ_minus.place(
    x=368,
    y=306.5003967285156,
    width=25.9,
    height=54.77
)

btnF_minus_img = PhotoImage(
    file=f"{path}{path}assets/frame0/button_18.png")
btnF_minus = Button(
    image=btnF_minus_img,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: ftnF_minus(),
    relief="flat"
)
btnF_minus.place(
    x=23,
    y=306.5003967285156,
    width=25.9,
    height=56
)

btnXY_minus_img = PhotoImage(
    file=f"{path}{path}assets/frame0/button_19.png")
btnXY_minus = Button(
    image=btnXY_minus_img,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: ftnXY_minus(),
    relief="flat"
)
btnXY_minus.place(
    x=317.476318359375,
    y=259.1339111328125,
    width=76.97052001953125,
    height=22.203033447265625
)

btnY_minus_img = PhotoImage(
    file=f"{path}{path}assets/frame0/button_20.png")
btnY_minus= Button(
    image=btnY_minus_img,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: ftnY_minus(),
    relief="flat"
)
btnY_minus.place(
    x=105.73883056640625,
    y=259.1339111328125,
    width=206.556884765625,
    height=22.203033447265625
)

btnXY_plusMinus_img = PhotoImage(
    file=f"{path}{path}assets/frame0/button_21.png")
btnXY_plusMinus = Button(
    image=btnXY_plusMinus_img,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: ftnXY_plusminus(),
    relief="flat"
)
btnXY_plusMinus.place(
    x=21.4359130859375,
    y=259.1338806152344,
    width=76.97052001953125,
    height=22.203033447265625
)


btnX_minus_img = PhotoImage(
    file=f"{path}{path}assets/frame0/button_22.png")
btnX_minus = Button(
    image=btnX_minus_img,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: ftnX_minus(),
    relief="flat"
)
btnX_minus.place(
    x=347.8206787109375,
    y=61.526885986328125,
    width=68.00741577148438,
    height=188.72579956054688
)

btnX_plus_img = PhotoImage(
    file=f"{path}{path}assets/frame0/button_23.png")
btnX_plus = Button(
    image=btnX_plus_img,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: ftnX_plus(),
    relief="flat"
)
btnX_plus.place(
    x=0.713134765625,
    y=61.526885986328125,
    width=68.00738525390625,
    height=188.72579956054688
)

btnXY_minusplus_img = PhotoImage(
    file=f"{path}{path}assets/frame0/button_24.png")
btnXY_minusplus = Button(
    image=btnXY_minusplus_img,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: ftnXY_minusplus(),
    relief="flat"
)
btnXY_minusplus.place(
    x=317.476318359375,
    y=34.143157958984375,
    width=76.97052001953125,
    height=22.203033447265625
)

btnY_plus_img = PhotoImage(
    file=f"{path}{path}assets/frame0/button_25.png")
btnY_plus = Button(
    image=btnY_plus_img,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: ftnY_plus(),
    relief="flat"
)
btnY_plus.place(
    x=103.587158203125,
    y=34.143157958984375,
    width=206.556884765625,
    height=22.203033447265625
)

btnXY_plus_img = PhotoImage(
    file=f"{path}{path}assets/frame0/button_26.png")
btnXY_plus= Button(
    image=btnXY_plus_img,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: ftnXY_plus(),
    relief="flat"
)
btnXY_plus.place(
    x=21.4359130859375,
    y=34.143157958984375,
    width=76.97052001953125,
    height=22.203033447265625
)
#-----jog view -------
animate_jog_top = Canvas(
    window,
    bg = "#EEEEEE",
    height = 183,
    width = 251,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge",
)

animate_jog_top.place( x= 82, y= 67)


top_img = PhotoImage(
    file=f"{path}{path}assets/frame0/Binder Jet-01.png")
top_view= animate_jog_top.create_image(
    251/2,
    183/2,
    image=top_img
)
x_img = PhotoImage(
    file=f"{path}{path}assets/frame0/Binder Jet-02.png")
y_img = PhotoImage(
    file=f"{path}{path}assets/frame0/Binder Jet-03.png")

x_view = animate_jog_top.create_image(
    251-(53+C.current_position['X']),
    181/2,
    image=x_img,
    tags = 'x_view'
)
y_view = animate_jog_top.create_image(
    251-(50+C.current_position['X']),
    143-C.current_position['Y'],
    image=y_img,
    tags = 'y_view'
)
animate_jog_side = Canvas(
    window,
    bg = "#EEEEEE",
    height = 124,
    width = 307,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge",
)

animate_jog_side.place( x= 55, y= 303)


side_img = PhotoImage(
    file=f"{path}{path}assets/frame0/Binder Jet-04.png")
side_view= animate_jog_side.create_image(
    307/2,
    124/2,
    image=side_img
)
f_img = PhotoImage(
    file=f"{path}{path}assets/frame0/Binder Jet-05.png")
z_img = PhotoImage(
    file=f"{path}{path}assets/frame0/Binder Jet-05.png")

z_view = animate_jog_side.create_image(
    307-78,
    5+C.current_position['Z'],
    image=z_img
)
f_view = animate_jog_side.create_image(
    80,
    5+C.current_position['F'],
    image=f_img
)
#-------------------
# image_image_2 = PhotoImage(
#     file=f"{path}{path}assets/frame0/image_2.png"))
# image_2 = canvas.create_image(
#     207.0,
#     363.0,
#     image=image_image_2
# )

#------terminal view-------
exe_win = Canvas(
        window,
        bg = "#2B2D2E",
        height = 463,
        width = 294,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge"
    )


exe_win.place(x = 1056, y = 50)



lineE = []
print_count = 0
def print_command(str):
    ex_font_name = "Cascadia Code"
    global print_count
    global exe_win
    if print_count < 16:
        exe_win.create_text(
        16.0,
        (print_count*20)+11,
        anchor="nw",
        text=str,
        fill="#EEEEEE",
        font=(ex_font_name, 15 * -1)
        )
        lineE.append(str)
        print_count += 1
    else:
        lineE.pop(0)
        exe_win.delete('all')
        for i in range (0, len(lineE)):
            exe_win.create_text(
            16.0,
            (i*20)+11,
            anchor="nw",
            text=lineE[i],
            fill="#EEEEEE",
            font=(ex_font_name, 15 * -1)
            )
        print_count -= 1
        print_command(str)
        
bgftn.start()
j.start()

#------progress bar ------
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
time_canvas.create_text(
        0,
        (17*0)+10,
        anchor="nw",
        text='-----------------------------------',
        fill="#EEEEEE",
        font=("Cascadia Code", 15 * -1)
        )
s = ttk.Style()
s.configure("red.Horizontal.TProgressbar", troughcolor='#EEEEEE', background='red', bordercolor = '#D8F9FF', 
            lightcolor = 'red', darkcolor = 'red')


time_rem.set(f'Estimated time: 0 H')
time_text = Label(time_canvas, textvariable = time_rem, font=("Cascadia Code", 15 * -1),
                  bg='#2B2D2E', fg = '#EEEEEE').place(x = 16.0, y = (17*1)+11, )

progress_var = DoubleVar()
exe_progress = ttk.Progressbar(time_canvas, style = "red.Horizontal.TProgressbar", variable = progress_var, 
                               orient = 'horizontal', length = 294-2*16, maximum = 100,  mode = "determinate", ).place(x= 16, y = (17*2)+20)

#------------------

# canvas.create_rectangle(
#     924.0,
#     528.0,
#     1350.0,
#     751.0,
#     fill="blue",
#     outline="")
# gcode_frame_1 = Frame(window, height= 751-528, width = 1350-924, bg= '#2B2D2E').place(x=924, y=528)
# gcode_canvas = Canvas(gcode_frame_1, bg='#2B2D2E').place( x= 924, y = 528)
# gcode_scrollbar = ttk.Scrollbar(gcode_frame_1, orient = VERTICAL, command = gcode_canvas.yview).pack(side = RIGHT, fill = Y, )
# gcode_canvas.configure(yscrollcommand = gcode_scrollbar.set)
# gcode_canvas.bind('<Configure>', lambda e: gcode_canvas.configure(scrollregion = gcode_canvas.bbox("all")) )
# gcode_frame_2 = Frame(gcode_canvas)

# gcode_canvas.create_window((0,0), window = gcode_frame_2, anchor = 'nw')

#--------gcode window --------

gcode_win = Canvas( window, height= 751-528, width = 1350-924, bg = '#2B2D2E')
gcode_win.place(x=924, y=528)
gcode_line = [Label() for i in range (0,10)]
gcode_getline = []

gcode_point = Label()
point_gcodeNum = 0
line_temp = 0
def point_gcode(i):
    global gcode_getline
    global point_gcodeNum
    global gcode_point
    global line_temp
    gcode_win.delete('point')
    if i < 9:   
        gcode_win.create_rectangle(
            16.0,
            (i*23)+10.5,
            1350-924-16,
            (i*23)+34,
            fill="#EEEEEE",
            tags = 'point',
            outline=''
            
            )
        gcode_win.create_text(
            20.0,
            (i*23)+11,
            text=gcode_getline[i],
            fill="#2B2D2E",
            anchor = 'nw',
            font=('Cascadia Code', 15 * -1),
            tags = 'point'
            ) 
        # point_gcodeNum +=1
    else:
        for x in range (0, i-9):
            gcode_getline.pop(0)
        print_gcode()
        # point_gcodeNum-= 1
        point_gcode(8)

    


def print_gcode():

    gcode_win.delete('line')
    
    for i in range(0, 5):
        # gcode_line[i] = Label(gcode_win, text=gcode_getline[i], fg= '#EEEEEE', bg = '#2B2D2E', font=("Cascadia Code", 15 * -1) ).place(x= 16, y = 11+(i*23))
        gcode_win.create_text(
            20.0,
            (i*23)+11,
            anchor="nw",
            text=gcode_getline[i],
            fill="#EEEEEE",
            font=('Cascadia Code', 15 * -1),
            tags = 'line'
            )  


    
#--------------

    

    

window.resizable(True, True)
window.mainloop()
