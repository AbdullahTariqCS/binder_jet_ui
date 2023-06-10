from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
from tkinter import *
from Controller import x_move, y_move, z_move, f_move
OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\at339\Desktop\IFproject\BjetController\code\build\assets\frame0")
def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


path = 'C:/Users/at339/Desktop/IFproject/BjetController/code/Program/'

x_cf = 0
y_cf = 0
z_cf = 0
f_cf = 0
x_steps = 200
y_steps = 100
CB_num = 1
diff = {'X':0.0, 'Y':0.0, 'Z':0.0, 'F':0.0}

xM= 0.00
xS = 0
xo = 0.00
xf = 0.00
yo = 0.00
yf = 0.00
zo= 0.00
zf= 0.00
fo = 0.00
ff = 0.00
yM = 0.00
yS= 0
zM = 0.00
fM = 0.00



cb_font_name = "Slabo 13px"
convertcount = 0
def write(x,y,z, xs, ys):
    global path
    cf = open(f'{path}calibrationfactors.txt','w')
    cf.write('X')   
    cf.write(str(x))
    cf.write(' Y')
    cf.write(str(y))
    cf.write(' Z')
    cf.write(str(z))
    cf.write(' F')
    cf.write(str(z))
    cf.write(' x')
    cf.write(str(xs))
    cf.write(' y')
    cf.write(str(ys))
    
    
def cbWindow():
    root_cb = Toplevel()
    global entry_1
    global entry_2
    global entry_3
    global entry_4
    global entry_5
    global entry_6
    global entry_7
    global entry_8
    global entry_9
    global entry_10
    global entry_11
    global entry_12
    global entry_13
    global entry_14
    global btnDone
    global btnM_enter
    global btnMove_minus
    global btnReset
    global btnDone
    global btnS_enter
    global difference
    global calibrations
    

    xMv= StringVar()
    xSv = StringVar()
    xov = StringVar()
    xfv = StringVar()
    yov = StringVar()
    yfv = StringVar()
    zov= StringVar()
    zfv= StringVar()
    fov = StringVar()
    ffv = StringVar()
    yMv = StringVar()
    ySv= StringVar()
    zMv= StringVar()
    fMv = StringVar()



    root_cb.geometry("1049x468")
    root_cb.configure(bg = "#EEEEEE")


    canvas = Canvas(
        root_cb,
        bg = "#EEEEEE",
        height = 468,
        width = 1049,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge"
    )

    canvas.place(x = 0, y = 0)
    difference = Canvas(
        root_cb,
        bg = "#EEEEEE",
        height = 165,
        width = 44,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge"
        )


    difference.place(x = 493, y = 200)
    difference.create_rectangle(
        0.0,
        0.0,
        44.0,
        165.0,
        fill="#EEEEEE",
        outline="")

    difference.create_text(
        0.0,
        10.891815185546875,
        anchor="nw",
        text="0.00",
        fill="#000000",
        font=(cb_font_name, 19 * -1)
    )

    difference.create_text(
        0.0,
        53.690399169921875,
        anchor="nw",
        text="0.00",
        fill="#000000",
        font=(cb_font_name, 19 * -1)
    )

    difference.create_text(
        0.0,
        96.48898315429688,
        anchor="nw",
        text="0.00",
        fill="#000000",
        font=(cb_font_name, 19 * -1)
    )

    difference.create_text(
        0.0,
        139.28756713867188,
        anchor="nw",
        text="0.00",
        fill="#000000",
        font=(cb_font_name, 19 * -1)
    )

    calibrations = Canvas(
        root_cb,
        bg = "#EEEEEE",
        height = 165,
        width = 44,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge"
    )

    calibrations.place(x = 677, y = 200)
    calibrations.create_rectangle(
        0.0,
        0.0,
        44.0,
        165.0,
        fill="#EEEEEE",
        outline="")

    calibrations.create_text(
        0.0,
        10.891815185546875,
        anchor="nw",
        text="0.00",
        fill="#000000",
        font=(cb_font_name, 19 * -1)
    )

    calibrations.create_text(
        0.0,
        53.690399169921875,
        anchor="nw",
        text="0.00",
        fill="#000000",
        font=(cb_font_name, 19 * -1)
    )

    calibrations.create_text(
        0.0,
        96.48898315429688,
        anchor="nw",
        text="0.00",
        fill="#000000",
        font=(cb_font_name, 19 * -1)
    )

    calibrations.create_text(
        0.0,
        139.28756713867188,
        anchor="nw",
        text="0.00",
        fill="#000000",
        font=(cb_font_name, 19 * -1)
    )
    step_view = Canvas(
        root_cb,
        bg = "#EEEEEE",
        height = 55,
        width = 44,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge"
    )

    step_view.place(x = 900, y = 339)
    step_view.create_text(
        1,
        1,
        anchor="nw",
        text="200",
        fill="#000000",
        font=(cb_font_name, 19 * -1)
    )

    step_view.create_text(
        1,
        32,
        anchor="nw",
        text="100",
        fill="#000000",
        font=(cb_font_name, 19 * -1))


    def ftnMove_plus():
        
        global xM
        global yM
        global zM
        global fM
        if xMv.get() != '':
            xM = float(xMv.get())
            x_move(abs(xM))
        if yMv.get() != '':
            yM = float(yMv.get())
            y_move(abs(yM))
        if zMv.get() != '':
            zM = float(zMv.get())
            z_move(abs(zM))
        if fMv.get() != '':
            fM = float(fMv.get())
            f_move(abs(fM))
            
    def ftnMove_minus():
        
        global xM
        global yM
        global zM
        global fM
        if xMv.get() != '':
            xM = float(xMv.get())
            x_move(-abs(xM))
        if yMv.get() != '':
            yM = float(yMv.get())
            y_move(-abs(yM))
        if zMv.get() != '':
            zM = float(zMv.get())
            z_move(-abs(zM))
        if fMv.get() != '':
            fM = float(fMv.get())
            f_move(-abs(fM))

    def ftnM_enter():
        global xM
        global xo 
        global xf
        global yo
        global yf
        global zo
        global zf
        global fo
        global ff
        global yM
        global zM
        global fM
        global x_cf
        global y_cf
        global z_cf
        global f_cf
        global diff
        global CB_num
        global cb_font_name
        if xMv.get() != '':xM = float(xMv.get())
        if xSv.get() != '':xS= float(xSv.get())
        if xov.get()!= '':xo= float(xov.get())
        if xfv.get()!= '':xf= float(xfv.get())
        if yov.get()!= '':yo= float(yov.get())
        if yfv.get()!= '':yf= float(yfv.get())
        if zov.get()!= '':zo= float(zov.get())
        if zfv.get()!= '':zf= float(zfv.get())
        if fov.get()!= '':fo= float(fov.get())
        if ffv.get()!= '':ff= float(ffv.get())
        if yMv.get() != '':yM = float(yMv.get())
        if ySv.get() != '':yS = float(ySv.get())
        if zMv.get() != '':zM = float(zMv.get())
        if fMv.get() != '':fM = float(fMv.get())
        
        
        
        
        #----- display difference canvas ----- 
        difference.delete('all')
        difference.create_text(
            0.0,
            10.891815185546875,
            anchor="nw",
            text=str(abs(xM)- abs(xf-xo)),
            fill="#000000",
            font=(cb_font_name, 19 * -1)
        )

        difference.create_text(
            0.0,
            53.690399169921875,
            anchor="nw",
            text=str(abs(yM)- abs(yf-yo)),
            fill="#000000",
            font=(cb_font_name, 19 * -1)
        )

        difference.create_text(
            0.0,
            96.48898315429688,
            anchor="nw",
            text=str(abs(zM)- abs(zf-zo)),
            fill="#000000",
            font=(cb_font_name, 19 * -1)
        )

        difference.create_text(
            0.0,
            139.28756713867188,
            anchor="nw",
            text=str(abs(fM)- abs(ff-fo)),
            fill="#000000",
            font=(cb_font_name, 19 * -1)
        )
        #-------------------------------------
        x_cf = ((abs(xM)- abs(xf-xo))+diff['X'])/CB_num
        y_cf = ((abs(yM)- abs(yf-yo))+diff['Y'])/CB_num
        z_cf = (abs(zM)- abs(zf-zo)+diff['Z'])/CB_num
        f_cf = ((abs(fM)- abs(ff-fo))+diff['F'])/CB_num
        
        write(x_cf, y_cf, z_cf, f_cf, x_steps, y_steps)
        # ----- calibration canvas-------
        calibrations.delete('all')
        calibrations.create_text(
        0.0,
        10.891815185546875,
        anchor="nw",
        text=str(x_cf),
        fill="#000000",
        font=(cb_font_name, 19 * -1)
        )

        calibrations.create_text(
            0.0,
            53.690399169921875,
            anchor="nw",
            text=str(y_cf),
            fill="#000000",
            font=(cb_font_name, 19 * -1)
        )

        calibrations.create_text(
            0.0,
            96.48898315429688,
            anchor="nw",
            text=str(z_cf),
            fill="#000000",
            font=(cb_font_name, 19 * -1)
        )

        calibrations.create_text(
            0.0,
            139.28756713867188,
            anchor="nw",
            text=str(f_cf),
            fill="#000000",
            font=(cb_font_name, 19 * -1)
        )
        
        #--------------------------------
        
        diff["X"] += abs(xM)- abs(xf-xo)
        diff["Y"] += abs(yM)- abs(yf-yo)
        diff["Z"] += abs(zM)- abs(zf-zo)
        diff["F"] += abs(fM)- abs(ff-fo)
        CB_num += 1
       
    def ftnS_enter():
        global x_steps
        global y_steps
        global xS
        global yS
        if ySv.get() != '':
            yS = float(ySv.get())
            y_steps = yS
        if xSv.get() != '':
            xS = float(xSv.get())
            x_steps = xS
        write(x_cf, y_cf, z_cf, x_steps, y_steps)
        step_view.delete('all')
        step_view.create_text(
            1,
            1,
            anchor="nw",
            text=str(x_steps),
            fill="#000000",
            font=(cb_font_name, 19 * -1)
        )

        step_view.create_text(
            1,
            32,
            anchor="nw",
            text=str(y_steps),
            fill="#000000",
            font=(cb_font_name, 19 * -1))

    def ftnReset():
        global xM
        global xo 
        global xf
        global yo
        global yf
        global zo
        global zf
        global fo
        global ff
        global yM
        global zM
        global fM
        global xS
        global yS
        global x_steps
        global y_steps
        global x_cf
        global y_cf
        global z_cf
        global f_cf
        global diff
        global CB_num
        global xM
        xo = 0.00
        xf = 0.00
        yo = 0.00
        yf = 0.00
        zo = 0.00
        zf = 0.00
        fo = 0.00
        ff = 0.00
        yM = 0.00
        zM = 0.00
        fM = 0.00
        xS = 0
        yS = 0
        x_steps = 200
        y_steps = 100
        x_cf = 0.00
        y_cf = 0.00
        z_cf = 0.00
        f_cf = 0.00
        diff = {'X':0.0, 'Y':0.0, 'Z':0.0, 'F':0.0}
        CB_num = 1
        difference.delete('all')
        difference.create_text(
            0.0,
            10.891815185546875,
            anchor="nw",
            text=str(abs(xM)- abs(xf-xo)),
            fill="#000000",
            font=(cb_font_name, 19 * -1)
        )

        difference.create_text(
            0.0,
            53.690399169921875,
            anchor="nw",
            text=str(abs(yM)- abs(yf-yo)),
            fill="#000000",
            font=(cb_font_name, 19 * -1)
        )

        difference.create_text(
            0.0,
            96.48898315429688,
            anchor="nw",
            text=str(abs(zM)- abs(zf-zo)),
            fill="#000000",
            font=(cb_font_name, 19 * -1)
        )

        difference.create_text(
            0.0,
            139.28756713867188,
            anchor="nw",
            text=str(abs(fM)- abs(ff-fo)),
            fill="#000000",
            font=(cb_font_name, 19 * -1)
        )
        calibrations.delete('all')
        calibrations.create_text(
        0.0,
        10.891815185546875,
        anchor="nw",
        text=str(x_cf),
        fill="#000000",
        font=(cb_font_name, 19 * -1)
        )

        calibrations.create_text(
            0.0,
            53.690399169921875,
            anchor="nw",
            text=str(y_cf),
            fill="#000000",
            font=(cb_font_name, 19 * -1)
        )

        calibrations.create_text(
            0.0,
            96.48898315429688,
            anchor="nw",
            text=str(z_cf),
            fill="#000000",
            font=(cb_font_name, 19 * -1)
        )

        calibrations.create_text(
            0.0,
            139.28756713867188,
            anchor="nw",
            text=str(f_cf),
            fill="#000000",
            font=(cb_font_name, 19 * -1)
        )
        step_view.delete('all')
        step_view.create_text(
            1,
            1,
            anchor="nw",
            text=str(x_steps),
            fill="#000000",
            font=(cb_font_name, 19 * -1)
        )

        step_view.create_text(
            1,
            32,
            anchor="nw",
            text=str(y_steps),
            fill="#000000",
            font=(cb_font_name, 19 * -1))        
        
        
        
        
    button_image_2 = PhotoImage(
        file=relative_to_assets("button_2.png"))
    btnReset = Button(
        root_cb,
        image=button_image_2,
        borderwidth=0,
        highlightthickness=0,
        command= lambda: ftnReset(),
        relief="flat"
    )
    btnReset.place(
        x=875.0,
        y=432.0,
        width=77.8599853515625,
        height=24.44000244140625
    )

    button_image_3 = PhotoImage(
        file=relative_to_assets("button_3.png"))
    btnDone = Button(
        root_cb,
        image=button_image_3,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: root_cb.destroy(),
        relief="flat"
    )
    btnDone.place(
        x=960.0,
        y=432.0,
        width=77.8599853515625,
        height=24.44000244140625
    )

    button_image_4 = PhotoImage(
        file=relative_to_assets("button_4.png"))
    btnMove_minus = Button(
        root_cb,
        image=button_image_4,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: ftnMove_minus(),
        relief="flat"
    )
    btnMove_minus.place(
        x=120.9761962890625,
        y=381.9894104003906,
        width=78.21810913085938,
        height=24.44000244140625
    )

    button_image_5 = PhotoImage(
        file=relative_to_assets("button_5.png"))
    btnM_enter = Button(root_cb,
        image=button_image_5,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: ftnM_enter(),
        relief="flat"
    )
    btnM_enter.place(
        x=278.79150390625,
        y=380.9410400390625,
        width=77.86000061035156,
        height=24.44000244140625
    )

    button_image_6 = PhotoImage(
        file=relative_to_assets("button_6.png"))
    btnS_enter = Button(root_cb,
        image=button_image_6,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: ftnS_enter(),
        relief="flat"
    )
    btnS_enter.place(
        x=895.4881591796875,
        y=283.944580078125,
        width=77.8599853515625,
        height=24.44000244140625
    )

    button_image_7 = PhotoImage(
        file=relative_to_assets("button_7.png"))
    btnMove_plus = Button(root_cb,
        image=button_image_7,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: ftnMove_plus(),
        relief="flat"
    )
    btnMove_plus.place(
        x=28.0,
        y=381.9894104003906,
        width=78.21810913085938,
        height=24.44000244140625
    )

    canvas.create_text(
        56.7783203125,
        204.89181518554688,
        anchor="nw",
        text="X:",
        fill="#000000",
        font=(cb_font_name, 19 * -1)
    )

    canvas.create_text(
        137.94805908203125,
        204.89181518554688,
        anchor="nw",
        text="mm",
        fill="#000000",
        font=(cb_font_name, 19 * -1)
    )


    entry_image_1 = PhotoImage(
        file=relative_to_assets("entry_1.png"))
    entry_bg_1 = canvas.create_image(
        106.58700561523438,
        213.00878620147705,
        image=entry_image_1
    )
    entry_1 = Entry(root_cb,
        bd=0,
        bg="#FFFFFF",
        fg="#000716",
        highlightthickness=0,
        textvariable= xMv
    )
    entry_1.place(
        x=82.60504150390625,
        y=201.940185546875,
        width=47.96392822265625,
        height=20.1372013092041
    )

    canvas.create_text(
        849.7379150390625,
        205.89181518554688,
        anchor="nw",
        text="X:",
        fill="#000000",
        font=(cb_font_name, 19 * -1)
    )

    canvas.create_text(
        930.9076538085938,
        205.89181518554688,
        anchor="nw",
        text="Steps/rev",
        fill="#000000",
        font=(cb_font_name, 19 * -1)
    )

    entry_image_2 = PhotoImage(
        file=relative_to_assets("entry_2.png"))
    entry_bg_2 = canvas.create_image(
        899.5466003417969,
        214.00878620147705,
        image=entry_image_2
    )
    entry_2 = Entry(root_cb,
        bd=0,
        bg="#FFFFFF",
        fg="#000716",
        highlightthickness=0
        ,textvariable= xSv
    )
    entry_2.place(
        x=875.5646362304688,
        y=202.940185546875,
        width=47.96392822265625,
        height=20.1372013092041
    )

    canvas.create_text(
        234.51708984375,
        207.84344482421875,
        anchor="nw",
        text="X:",
        fill="#000000",
        font=(cb_font_name, 19 * -1)
    )

    canvas.create_text(
        378.40887451171875,
        207.84344482421875,
        anchor="nw",
        text="mm",
        fill="#000000",
        font=(cb_font_name, 19 * -1)
    )

    entry_image_3 = PhotoImage(
        file=relative_to_assets("entry_3.png"))
    entry_bg_3 = canvas.create_image(
        288.75323486328125,
        215.96041584014893,
        image=entry_image_3
    )
    entry_3 = Entry(root_cb,
        bd=0,
        bg="#FFFFFF",
        fg="#000716",
        highlightthickness=0,textvariable= xov
    )
    entry_3.place(
        x=264.7712707519531,
        y=204.89181518554688,
        width=47.96392822265625,
        height=20.1372013092041
    )

    entry_image_4 = PhotoImage(
        file=relative_to_assets("entry_4.png"))
    entry_bg_4 = canvas.create_image(
        345.5720520019531,
        215.96041584014893,
        image=entry_image_4
    )
    entry_4 = Entry(root_cb,
        bd=0,
        bg="#FFFFFF",
        fg="#000716",
        highlightthickness=0,textvariable= xfv
    )
    entry_4.place(
        x=321.590087890625,
        y=204.89181518554688,
        width=47.96392822265625,
        height=20.1372013092041
    )

    canvas.create_text(
        234.51708984375,
        250.64202880859375,
        anchor="nw",
        text="Y:",
        fill="#000000",
        font=(cb_font_name, 19 * -1)
    )

    canvas.create_text(
        378.40887451171875,
        250.64202880859375,
        anchor="nw",
        text="mm",
        fill="#000000",
        font=(cb_font_name, 19 * -1)
    )

    entry_image_5 = PhotoImage(
        file=relative_to_assets("entry_5.png"))
    entry_bg_5 = canvas.create_image(
        288.75323486328125,
        258.7589988708496,
        image=entry_image_5
    )
    entry_5 = Entry(root_cb,
        bd=0,
        bg="#FFFFFF",
        fg="#000716",
        highlightthickness=0,textvariable= yov
    )
    entry_5.place(
        x=264.7712707519531,
        y=247.69039916992188,
        width=47.96392822265625,
        height=20.13719940185547
    )

    entry_image_6 = PhotoImage(
        file=relative_to_assets("entry_6.png"))
    entry_bg_6 = canvas.create_image(
        345.5720520019531,
        258.7589988708496,
        image=entry_image_6
    )
    entry_6 = Entry(root_cb,
        bd=0,
        bg="#FFFFFF",
        fg="#000716",
        highlightthickness=0,textvariable= yfv
    )
    entry_6.place(
        x=321.590087890625,
        y=247.69039916992188,
        width=47.96392822265625,
        height=20.13719940185547
    )

    canvas.create_text(
        234.51708984375,
        293.44061279296875,
        anchor="nw",
        text="Z:",
        fill="#000000",
        font=(cb_font_name, 19 * -1)
    )

    canvas.create_text(
        378.40887451171875,
        293.44061279296875,
        anchor="nw",
        text="mm",
        fill="#000000",
        font=(cb_font_name, 19 * -1)
    )

    entry_image_7 = PhotoImage(
        file=relative_to_assets("entry_7.png"))
    entry_bg_7 = canvas.create_image(
        288.75323486328125,
        301.5575828552246,
        image=entry_image_7
    )
    entry_7 = Entry(root_cb,
        bd=0,
        bg="#FFFFFF",
        fg="#000716",
        highlightthickness=0,textvariable= zov
    )
    entry_7.place(
        x=264.7712707519531,
        y=290.4889831542969,
        width=47.96392822265625,
        height=20.13719940185547
    )

    entry_image_8 = PhotoImage(
        file=relative_to_assets("entry_8.png"))
    entry_bg_8 = canvas.create_image(
        345.5720520019531,
        301.5575828552246,
        image=entry_image_8
    )
    entry_8 = Entry(root_cb,
        bd=0,
        bg="#FFFFFF",
        fg="#000716",
        highlightthickness=0,textvariable= zfv
    )
    entry_8.place(
        x=321.590087890625,
        y=290.4889831542969,
        width=47.96392822265625,
        height=20.13719940185547
    )

    canvas.create_text(
        234.51708984375,
        336.23919677734375,
        anchor="nw",
        text="F:",
        fill="#000000",
        font=(cb_font_name, 19 * -1)
    )

    canvas.create_text(
        378.40887451171875,
        336.23919677734375,
        anchor="nw",
        text="mm",
        fill="#000000",
        font=(cb_font_name, 19 * -1)
    )

    entry_image_9 = PhotoImage(
        file=relative_to_assets("entry_9.png"))
    entry_bg_9 = canvas.create_image(
        288.75323486328125,
        344.3561668395996,
        image=entry_image_9
    )
    entry_9 = Entry(root_cb,
        bd=0,
        bg="#FFFFFF",
        fg="#000716",
        highlightthickness=0,textvariable= fov
    )
    entry_9.place(
        x=264.7712707519531,
        y=333.2875671386719,
        width=47.96392822265625,
        height=20.13719940185547
    )

    entry_image_10 = PhotoImage(
        file=relative_to_assets("entry_10.png"))
    entry_bg_10 = canvas.create_image(
        345.5720520019531,
        344.3561668395996,
        image=entry_image_10
    )
    entry_10 = Entry(root_cb,
        bd=0,
        bg="#FFFFFF",
        fg="#000716",
        highlightthickness=0,textvariable= ffv
    )
    entry_10.place(
        x=321.590087890625,
        y=333.2875671386719,
        width=47.96392822265625,
        height=20.13719940185547
    )

    canvas.create_text(
        56.0404052734375,
        247.69039916992188,
        anchor="nw",
        text="Y:",
        fill="#000000",
        font=(cb_font_name, 19 * -1)
    )

    canvas.create_text(
        137.94805908203125,
        247.69039916992188,
        anchor="nw",
        text="mm",
        fill="#000000",
        font=(cb_font_name, 19 * -1)
    )

    entry_image_11 = PhotoImage(
        file=relative_to_assets("entry_11.png"))
    entry_bg_11 = canvas.create_image(
        106.58700561523438,
        255.80736923217773,
        image=entry_image_11
    )
    entry_11 = Entry(root_cb,
        bd=0,
        bg="#FFFFFF",
        fg="#000716",
        highlightthickness=0, textvariable= yMv
    )
    entry_11.place(
        x=82.60504150390625,
        y=244.73876953125,
        width=47.96392822265625,
        height=20.13719940185547
    )

    canvas.create_text(
        849.0,
        237.62179565429688,
        anchor="nw",
        text="Y:",
        fill="#000000",
        font=(cb_font_name, 19 * -1)
    )

    canvas.create_text(
        930.59375,
        238.0,
        anchor="nw",
        text="Steps/ rev",
        fill="#000000",
        font=(cb_font_name, 19 * -1)
    )

    entry_image_12 = PhotoImage(
        file=relative_to_assets("entry_12.png"))
    entry_bg_12 = canvas.create_image(
        899.5466003417969,
        245.73876667022705,
        image=entry_image_12
    )
    entry_12 = Entry(root_cb,
        bd=0,
        bg="#FFFFFF",
        fg="#000716",
        highlightthickness=0,textvariable= ySv
    )
    entry_12.place(
        x=875.5646362304688,
        y=234.670166015625,
        width=47.96392822265625,
        height=20.1372013092041
    )

    canvas.create_text(
        56.7783203125,
        290.4889831542969,
        anchor="nw",
        text="Z:",
        fill="#000000",
        font=(cb_font_name, 19 * -1)
    )

    canvas.create_text(
        137.21014404296875,
        290.4889831542969,
        anchor="nw",
        text="mm",
        fill="#000000",
        font=(cb_font_name, 19 * -1)
    )

    entry_image_13 = PhotoImage(
        file=relative_to_assets("entry_13.png"))
    entry_bg_13 = canvas.create_image(
        105.84912109375,
        298.60595321655273,
        image=entry_image_13
    )
    entry_13 = Entry(root_cb,
        bd=0,
        bg="#FFFFFF",
        fg="#000716",
        highlightthickness=0, textvariable= zMv
    )
    entry_13.place(
        x=81.86715698242188,
        y=287.537353515625,
        width=47.96392822265625,
        height=20.13719940185547
    )

    canvas.create_text(
        56.7783203125,
        333.2875671386719,
        anchor="nw",
        text="F:",
        fill="#000000",
        font=(cb_font_name, 19 * -1)
    )

    canvas.create_text(
        137.21014404296875,
        333.2875671386719,
        anchor="nw",
        text="mm",
        fill="#000000",
        font=(cb_font_name, 19 * -1)
    )

    entry_image_14 = PhotoImage(
        file=relative_to_assets("entry_14.png"))
    entry_bg_14 = canvas.create_image(
        105.84912109375,
        341.40453720092773,
        image=entry_image_14, 
    )
    entry_14 = Entry(root_cb,
        bd=0,
        bg="#FFFFFF",
        fg="#000716",
        highlightthickness=0,textvariable= fMv
    )
    entry_14.place(
        x=81.86715698242188,
        y=330.3359375,
        width=47.96392822265625,
        height=20.13719940185547
    )
    canvas.create_text(
        869.0,
        342.0,
        anchor="nw",
        text="X:",
        fill="#000000",
        font=(cb_font_name, 19 * -1)
    )

    canvas.create_text(
        951.0,
        339.0,
        anchor="nw",
        text="Steps",
        fill="#000000",
        font=(cb_font_name, 19 * -1)
    )

    canvas.create_text(
        869.0,
        373.72998046875,
        anchor="nw",
        text="Y:",
        fill="#000000",
        font=(cb_font_name, 19 * -1)
    )

    canvas.create_text(
        951.0,
        371.0,
        anchor="nw",
        text="Steps",
        fill="#000000",
        font=(cb_font_name, 19 * -1)
    )


    canvas.create_text(
        470.0,
        64.0,
        anchor="nw",
        text="Calibrate",
        fill="#000000",
        font=(cb_font_name, 19 * -1)
    )

    canvas.create_text(
        50.0,
        136.0,
        anchor="nw",
        text="Movement Value:",
        fill="#000000",
        font=(cb_font_name, 19 * -1)
    )

    canvas.create_text(
        890.59375,
        137.0,
        anchor="nw",
        text="Step value",
        fill="#000000",
        font=(cb_font_name, 19 * -1)
    )

    canvas.create_text(
        244.0,
        136.0,
        anchor="nw",
        text="Measured Value",
        fill="#000000",
        font=(cb_font_name, 19 * -1)
    )

    canvas.create_text(
        290.0,
        172.0,
        anchor="nw",
        text="I",
        fill="#000000",
        font=(cb_font_name, 22 * -1)
    )

    canvas.create_text(
        335.0,
        172.0,
        anchor="nw",
        text="F",
        fill="#000000",
        font=(cb_font_name, 22 * -1)
    )

    canvas.create_text(
        649.48193359375,
        210.89181518554688,
        anchor="nw",
        text="X:",
        fill="#000000",
        font=(cb_font_name, 19 * -1)
    )





    canvas.create_text(
        648.7440185546875,
        253.69039916992188,
        anchor="nw",
        text="Y:",
        fill="#000000",
        font=(cb_font_name, 19 * -1)
    )

    canvas.create_text(
        730.6516723632812,
        253.69039916992188,
        anchor="nw",
        text="mm",
        fill="#000000",
        font=(cb_font_name, 19 * -1)
    )
    canvas.create_text(
        730.6516723632812,
        210.89181518554688,
        anchor="nw",
        text="mm",
        fill="#000000",
        font=(cb_font_name, 19 * -1)
    )



    canvas.create_text(
        649.48193359375,
        296.4889831542969,
        anchor="nw",
        text="Z:",
        fill="#000000",
        font=(cb_font_name, 19 * -1)
    )

    canvas.create_text(
        729.9137573242188,
        296.4889831542969,
        anchor="nw",
        text="mm",
        fill="#000000",
        font=(cb_font_name, 19 * -1)
    )



    canvas.create_text(
        649.48193359375,
        339.2875671386719,
        anchor="nw",
        text="F:",
        fill="#000000",
        font=(cb_font_name, 19 * -1)
    )

    canvas.create_text(
        729.9137573242188,
        339.2875671386719,
        anchor="nw",
        text="mm",
        fill="#000000",
        font=(cb_font_name, 19 * -1)
    )



    canvas.create_text(
        630.0,
        134.0,
        anchor="nw",
        text="Calibration Factor",
        fill="#000000",
        font=(cb_font_name, 19 * -1)
    )

    canvas.create_text(
        463.48193359375,
        210.89181518554688,
        anchor="nw",
        text="X:",
        fill="#000000",
        font=(cb_font_name, 19 * -1)
    )

    canvas.create_text(
        544.6516723632812,
        210.89181518554688,
        anchor="nw",
        text="mm",
        fill="#000000",
        font=(cb_font_name, 19 * -1)
    )



    canvas.create_text(
        462.7440185546875,
        253.69039916992188,
        anchor="nw",
        text="Y:",
        fill="#000000",
        font=(cb_font_name, 19 * -1)
    )

    canvas.create_text(
        544.6516723632812,
        253.69039916992188,
        anchor="nw",
        text="mm",
        fill="#000000",
        font=(cb_font_name, 19 * -1)
    )



    canvas.create_text(
        463.48193359375,
        296.4889831542969,
        anchor="nw",
        text="Z:",
        fill="#000000",
        font=(cb_font_name, 19 * -1)
    )

    canvas.create_text(
        543.9137573242188,
        296.4889831542969,
        anchor="nw",
        text="mm",
        fill="#000000",
        font=(cb_font_name, 19 * -1)
    )



    canvas.create_text(
        463.48193359375,
        339.2875671386719,
        anchor="nw",
        text="F:",
        fill="#000000",
        font=(cb_font_name, 19 * -1)
    )

    canvas.create_text(
        543.9137573242188,
        339.2875671386719,
        anchor="nw",
        text="mm",
        fill="#000000",
        font=(cb_font_name, 19 * -1)
    )



    canvas.create_text(
        475.0,
        134.0,
        anchor="nw",
        text="Difference",
        fill="#000000",
        font=(cb_font_name, 19 * -1)
    )

    canvas.create_rectangle(
        822.0,
        125.0,
        823.0,
        421.0,
        fill="#000000",
        outline="")
    root_cb.resizable(False, False)
    root_cb.mainloop()
if __name__ == '__main__':
    cbWindow()