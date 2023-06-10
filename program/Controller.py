from time import sleep, monotonic
import ToolpathGenerator as TP
import ChamberStatus as CB
import threading
import LScheck as LS
from PyQt5 import QtGui, QtCore



path = ''
current_position = {"X":0.0, "Y":0.0, "Z":0.0, "F":0.0}
home_position = {'X':0.0, 'Y':0.0, 'Z': 0., 'F':0.0}
x_c = 0
y_c = 0
z_c = 0
f_c = 0
stepsX_c = 200
stepsY_c = 200
speedX = 2
speedY = 2
print_time = []
print_number = 0
res_printLine = 0
print_stat = False
#variables to show if any axis is moving or not 
x_true = None
y_true = None
z_true = None
f_true = None

#------Execution Window-------
stringC = []
stringCount = 0
def printC(str):
    print(str)
    global stringCount
    global stringC
    # if stringCount == 5: 
    #     stringC = []
    #     stringCount = 0
    stringC.append(str)
    stringCount += 1
 


def TPN_backup(n):
    tp = open(f'{path}toolpathnumber.txt','w')
    tp.write(str(n))   
    
def CP_backup(array):
    global path
    cp = open(f'{path}currentposition.txt','w')
    cp.write('X')   
    cp.write(str(array['X']))
    cp.write(' Y')
    cp.write(str(array['Y']))
    cp.write(' Z')
    cp.write(str(array['Z']))
    cp.write(' F')
    cp.write(str(array['F']))

def getCF():
    global x_c 
    global y_c 
    global z_c 
    global f_c 
    global stepsX_c 
    global stepsY_c 
    with open(f'{path}homeposition.txt','r') as cf:
        for line in cf:
            for word in line.split():
                if (word.startswith('X')):
                    x_c = float(word[1:len(word):1])
                if (word.startswith('Y')):
                    y_c = float(word[1:len(word):1])
                if (word.startswith('Z')):
                    f_c = float(word[1:len(word):1])
                if (word.startswith('F')):
                    z_c = float(word[1:len(word):1])
                if (word.startswith('x')):
                    stepsX_c = float(word[1:len(word):1])
                if (word.startswith('y')):
                    stepsY_c = float(word[1:len(word):1])

#------Additional Commands-----

def sleepC(n):
    start_time = monotonic()
    while True:
        current_time = monotonic()
        elapsed_time = current_time - start_time
        if elapsed_time >= n:
            break # delay in seconds
 

def home():
    try:
        xy_move(-900, -900)
        z_move(-340)
        f_move(-340)
        # CB.get_status('Fill Feed')
    except: 
        printC('Clear chamber')
        
def set_home():
    global home_position
    global current_position
    home_position = current_position
    current_position = {"X":0.0, "Y":0.0, "Z":0.0, "F":0.0}
    printC (f'Origin translated by {home_position}')
    hp = open('C:/Users/at339/Desktop/IFproject/BjetController/code/Program/homeposition.txt','w')
    hp.write('X')   
    hp.write(str(home_position['X']))
    hp.write(' Y')
    hp.write(str(home_position['Y']))
    hp.write(' Z')
    hp.write(str(home_position['Z']))
    hp.write(' F')
    hp.write(str(home_position['F']))

def desposit_layer(z):
    global current_position
    temp = current_position['X']
    if z > 0:
        x_move(900)
        f_move(-(z+f_c))
        z_move(z+z_c)
        x_move(-900)
        x_move(temp+x_c)
        CB.Zclear = False
        
    elif z < 0:
        x_move(-900)
        z_move(z+z_c)
        f_move(-(z+f_c))
        x_move(+900)
        x_move(temp+x_c)
        CB.Fclear = False
        
# def clear_chamber(str): 
#     tempx = current_position['X']
#     tempz = current_position['Z']
#     tempf = current_position['F']
#     print('clear chamber is running')
#     printC(f'moving x-axis chamber to clear {str} chamber' )
#     if str == 'Z' and CB.mZ_clear == True:
#         print('Moving X axis to clear Z Chamber')
#         printC('Moving X axis to clear Z Chamber')
#         x_move(900)
#         z_move(-(current_position['Z'] - home_position['Z']+z_c)) #moving z chamber to the edge
#         CB.get_status()
#         clear_chamber(CB.C_move)
#         if CB.Zclear == True:
#             z_move(tempz+z_c)
#             x_move((tempx - 782)+x_c)
#         CB.C_move = ''

#     elif str == 'F' and CB.mF_clear == True:
#         print('Moving X axis to clear Z Chamber')
#         printC('Moving X axis to clear Z Chamber')
#         x_move(-900)
#         f_move(-(current_position['F']+f_c))
#         CB.get_status()
#         clear_chamber(CB.C_move)
#         if CB.Fclear == True:
#             f_move(tempf+f_c)
#             x_move(tempx+x_c)
#         CB.C_move = ''
            
                
def start_print(n = 0):
    global print_number
    global print_stat
    print_number = n
    # if n == 0: home()
    
    printC('Starting print from toolpath')
    print_stat = True
    for i in range (n, TP.toolpath_number ):
        xy_move(TP.toolpath[i]['X']+x_c, TP.toolpath[i]['Y']+y_c )
        if i != 0 and TP.toolpath[i]['G'] == 1:
            desposit_layer(TP.toolpath[i]['Z'])
        else:
            z_move(TP.toolpath[i]['Z'])

        print_number += 1
        TPN_backup(i)
    print_stat = False
    printC('Print is complete')

def print_backup():
    global res_printLine
    with open('currentposition.txt','r') as cp:
        for line in cp:
            for word in line.split():
                if (word.startswith('X')):
                    x_value=word[1:len(word):1]
                    current_position['X']=float(x_value)
                if (word.startswith('Y')):
                    y_value=word[1:len(word):1]
                    current_position['Y']=float(y_value)
                if (word.startswith('Z')):
                    z_value=word[1:len(word):1]
                    current_position['Z']=float(z_value)
    with open(f'{path}toolpathnumber.txt','r') as tp:
        n = int(tp.read())
        res_printLine = n
        temp = TP.toolpath[n]['N']
        printC(f'Starting print from line number:{temp}' )
        #start_print(n)
    

def print_timeCalculator(n = 0):
    global print_time
    print_time = []
    total_time = 0.00
    for i in range (n, TP.toolpath_number -1):
        if i == n:
            if TP.toolpath[i]['Y'] == 0 and TP.toolpath[i]['X'] != 0:
                total_time += TP.toolpath[i]['X']/speedX
                
            elif TP.toolpath[i]['Y'] != 0 and TP.toolpath[i]['X'] == 0:
                total_time +=  TP.toolpath[i]['Y']/speedY
                
            elif TP.toolpath[i]['Y'] != 0 and TP.toolpath[i]['X'] != 0:
                if TP.toolpath[i]['X'] >= TP.toolpath[i]['Y']:
                    total_time += TP.toolpath[i]['X']/speedX
                else:
                    total_time += TP.toolpath[i]['Y']/speedY
                    
            if TP.toolpath[i]['Z'] != 0:
                total_time += 2*(TP.toolpath[i]['Z']/10)
            
            
        else:
            if TP.toolpath[i]['Y'] == TP.toolpath[i-1]['Y'] and TP.toolpath[i]['X'] != TP.toolpath[i-1]['X']:
                total_time += TP.toolpath[i]['X']/speedX
                
            elif TP.toolpath[i]['Y'] != TP.toolpath[i-1]['Y'] and TP.toolpath[i]['X'] == TP.toolpath[i-1]['X']:
                total_time += TP.toolpath[i]['Y']/speedY
                
            elif TP.toolpath[i]['Y'] != TP.toolpath[i-1]['Y'] and TP.toolpath[i]['X'] != TP.toolpath[i-1]['X']:
                if TP.toolpath[i]['X'] >= TP.toolpath[i]['Y']:
                    total_time += TP.toolpath[i]['X']/speedX
                else:
                    total_time += TP.toolpath[i]['Y']/speedY
                    
            if TP.toolpath[i]['Z'] !=  TP.toolpath[i-1]['Z']:
                total_time += 2*(TP.toolpath[i]['Z']/10)
            print_time.append(round(total_time/3600,2))
            
                
            
        
        
    
#------Axis Conrollers-----
stop = False

def z_move(z=1):
    getCF()
    try:
        
        
        #if Z chamber is filled and powder surface is 50 mm above surface and print head is present there, raise exception
        if z< 0 and  abs(z)> CB.P_head and (current_position['X'] - home_position['X']) < 340 and CB.Zclear == False:
            raise Exception(printC('warning exception'),CB.get_warning('Z'),)
        
        #if -ive travel of chamber is greater than allowed range of travel, raise exception
        if z < 0 and abs(z)  > CB.P_head +(current_position['Z']-home_position['Z']) and (current_position['X'] - home_position['X']) < 340:
            raise Exception(printC('Printhead over Z chamber'))

        
        global stop
        global z_true 
        z_true = True
        printC(f'Moving Z axis {z}mm')
        
        if stop == False and LS.LS_safety == True: 
            sleep(abs(0.2*z))
            #if z > 0 and LS.lsZ_plusS== False: raise Exception(printC('Check 1Z limit switche'), LS.check() )
            current_position['Z'] += z
            CP_backup(current_position)
        printC(f'Z axis moved {z}mm')
        stop = False
        z_true = False
        return 
    except:
        return

def f_move(f=1):
    getCF()
    try:
        
        #if Z chamber is filled and powder surface is 50 mm above surface and print head is present there, raise exception
        if f< 0 and  abs(f)> CB.P_head and (current_position['X'] - home_position['X']) < 340 and CB.Zclear == False:
            raise Exception(printC('warning exception'),CB.get_warning('Z'))
        
        #if -ive travel of chamber is greater than allowed range of travel, raise exception
        if f < 0 and abs(f)  > CB.P_head +(current_position['F']-home_position['F']) and (current_position['X'] - home_position['X']) < 340:
            raise Exception(printC('Printhead over F chamber'))
        global stop
        global f_true
        f_true = True
        printC(f'Moving F axis {f} mm')
        if stop == False and LS.lsF_plusS == True: 
            sleep(abs(0.2*f))
            #if f > 0 and LS.lsF_plusS== False: raise Exception(printC('Check 1F limit switch'), LS.check() )
            current_position['F'] += f
            CP_backup(current_position)
        printC(f'Feed moved {f}mm')
        stop = False
        f_true = False
        return
    except:
        print()

def x_move(x = 1, fx = 2, stat = True):
    global pulx
    global dirx
    global stop
    global x_true
    
    stop = False
    # getCF()
    try:
    
        # if fx<0.5 or fx>2: raise Exception( printC('Speed out of range'))
        
        sign = 1
        if x > 0: sign = 1
        elif x < 0: sign = -1
        frequency = 0.2/(2*(stepsX_c*fx))
        print(f'x frequency: {frequency}')
        if stat: printC(f'Moving X axis {x} mm')
        
        xtime = 0.0

        i = 0
        x_true = True
        # countdown()
        for i in range (abs(int(x*stepsX_c))):
            #if x > 0 and LS.lsX_plusS== False: raise Exception(printC('Check 1X limit switch'), LS.check() )
            # if stop == False and LS.LS_safety == True:
                #GPIO.output(pulx, GPIO.HIGH)
                sleep(frequency)
                xtime += frequency
                #GPIO.ouput(pulx, GPIO.LOW)
                sleep(frequency)
                xtime += frequency
                #print('X Pulse: ', i)
                current_position['X'] += sign*(1/stepsX_c)
        # CP_backup(current_position)
        print(current_position)
        print(f'XTime = {xtime}')
        if stat: printC(f'X Pulses: { i+1}  X Speed: { fx}' )
        x_true = False
        return 
        
    except: return
        

def y_move(y = 1, fy = 2,stat = True):
    global stop
    global y_true
    stop = False

    # getCF()
    try:
        #if LS.LS_safety == False: raise Exception(printC('Check limit switches') )  
        # if fy<0.5 or fy>2: raise Exception(printC('Speed out of range'))
        sign = 1
        if y > 0: sign = 1
        elif y < 0: sign = -1
        
        frequency = 0.15/(2*(stepsY_c*fy))
        print(f'y frequency: {frequency}')
        
        print('Moving Y axiz ',y,'mm')
        if stat: printC(f'Moving Y axis {y}mm')
        
        temp = 0.0
        i = 0
        y_true = True
        # countdown()
        for i in range (abs(int(y*stepsY_c))):
            # if y > 0 and LS.lsY_plusS== False: raise Exception(printC('Check 1Y limit switch'), LS.check() )
            if stop == False and LS.LS_safety == True:
                #GPIO.ouput(puly, GPIO.HIGH)
                sleep(frequency)
                temp += frequency
                #GPIO.output(puly, GPIO.LOW)
                sleep(frequency)
                temp += frequency
                # print ('Y Pulse: ', i)
                current_position['Y'] += sign*(1/stepsY_c)
    
        
        
        # CP_backup(current_position)
        print(current_position)
        print(f'yTime = {temp}')
        if stat: printC(f'Y Pulses: { i+1}  Y Speed: { fy}' )
        y_true = False
        return
        
    except: return
def freq(x,y): 
    x +=2*y
def countdown():
        print('moving axis in 3 ')
        sleep(1)
        print('2')
        sleep(1)
        print('1')
        sleep(1)
        print('0')

def xy_move(x=2, y=1):
    time = 0
    if x != 0 and y == 0:
        x_move(x)
    elif x == 0 and y != 0:
        y_move(y)
    else:
        if abs(x) > abs(y):
            fx = 2
            time = round(abs(x/fx), 2)
            fy = abs(y/time)
        elif abs(x) < abs(y):
            fy = 2
            time = round(abs(y/fy),2)
            fx = round(abs(x/time),2)
        else: 
            fx = 2
            fy = 2
        # printC (f'Moving')
        printC (f'xspeed: {fx}, yspeed: {fy}')
        printC(f'Moving X:{x}, Y:{y}')
        # threading.Thread(target = y_move, args= (y, fy, False)).start()
        threading.Thread(target = x_move, args= (x, fx, False)).start()
        # x_move(x,fx, False)
        y_move(y,fy, False)
    return
    
#xy_move()    
if __name__ == '__main__':
    # xy_move(100,50)
    y_move(20)