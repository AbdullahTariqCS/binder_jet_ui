from time import sleep
import RPi.GPIO as GPIO
import threading
import LScheck as L
import ChamberStatus as C
import math


pulx=20
puly=19
dirx=16
diry=26

f_minus=27
f_plus=17
z_minus=23
z_plus=18
pump=24

LS1X=13
LS2X=12
LS3Y=4
LS4Y=6
LS5Z = 13 #connect limit switch to any empty port
LS6Z = 14
LS7F = 15
LS8F = 21

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(pulx,GPIO.OUT)
GPIO.setup(puly,GPIO.OUT)
GPIO.setup(dirx,GPIO.OUT)
GPIO.setup(diry,GPIO.OUT)


GPIO.setup(f_minus,GPIO.OUT)
GPIO.setup(f_plus,GPIO.OUT)
GPIO.setup(z_minus,GPIO.OUT)
GPIO.setup(z_plus,GPIO.OUT)
GPIO.setup(pump,GPIO.OUT)
z_minusP= GPIO.PWM(z_minus, 100)
z_plusP= GPIO.PWM(z_plus, 100)
f_minusP= GPIO.PWM(f_minus, 100)
f_plusP= GPIO.PWM(f_plus, 100)


GPIO.setup(LS1X,GPIO.IN)
GPIO.setup(LS2X,GPIO.IN)
GPIO.setup(LS3Y,GPIO.IN)
GPIO.setup(LS4Y,GPIO.IN)
GPIO.setup(LS5Z,GPIO.IN)
GPIO.setup(LS6Z,GPIO.IN)
GPIO.setup(LS7F,GPIO.IN)
GPIO.setup(LS8F,GPIO.IN)

current_position = {"X":0.0, "Y":0.0, "Z":0.0}

#------Axis Controllers-----
stop = False

def z_move(z=1):
    global z_plus
    global z_minus
    global LS5Z
    global LS6Z
    global stop
    print('Moving Z axis ',z,'mm')
    if z > 0:
        GPIO.output(z_plus, GPIO.HIGH)
        if GPIO.input(LS5Z) == True and stop == False: 
            sleep(abs(0.1*z))
            GPIO.output(z_plus, GPIO.LOW)
            sleep(abs(0.1*z))
            current_position['Z'] += z
        
    elif z < 0:
        GPIO.output(z_minus, GPIO.HIGH)
        if GPIO.input(LS6Z) == True and stop == False: 
            sleep(abs(0.1*z))
            GPIO.output(z_minus, GPIO.LOW)
            sleep(abs(0.1*z))
            current_position['Z'] += z
    stop = False

def f_move(f=1):
    global f_plus
    global f_minus
    global LS7F
    global LS8F
    global stop
    print('Moving feed ',f,'mm')
    if f > 0:
        GPIO.output(z_plus, GPIO.HIGH)
        if GPIO.input(LS7F) == True and stop == False: 
            sleep(abs(0.1*f))
            GPIO.output(z_plus, GPIO.LOW)
            sleep(abs(0.1*f))
            current_position['Z'] += f
        
    elif f < 0:
        GPIO.output(f_minus, GPIO.HIGH)
        if GPIO.input(LS8F) == True and stop == False: 
            sleep(abs(0.1*f))
            GPIO.output(f_minus, GPIO.LOW)
            sleep(abs(0.1*f))
            current_position['Z'] += f
    stop = False

def x_move(x=1, fx = 2):
    global pulx
    global dirx
    global stop
    
    try:
        if fx<0.5 or fx>2: raise Exception
        
        if x > 0: GPIO.output(dirx, GPIO.LOW)
        elif x < 0: GPIO.output(dirx, GPIO.HIGH)
        
        frequency = 1/(400*fx)
        
        print('Moving X axis ',x,'mm')
        i = 0
        for i in range (abs(int(x*200))):
            if GPIO.input(LS2X)  and GPIO.input(LS1X) and stop == False:
                GPIO.output(pulx, GPIO.HIGH)
                sleep(frequency)
                GPIO.output(pulx, GPIO.LOW)
                sleep(frequency)
            current_position['X'] += 1/200
        print('Pulses: ', i, ' Speed: ', fx )
        
        stop = False
    except:
        print('Speed out of range')

def y_move(y=1, fy = 2):
    global puly
    global diry
    global stop
    
    try:
        if fy<0.5 or fy>2: raise Exception
        
        if y > 0: GPIO.output(diry, GPIO.LOW)
        elif y < 0: GPIO.output(diry, GPIO.HIGH)
        
        frequency = 1/(200*fy)
        
        print('Moving Y axis ',y,'mm')
        i = 0
        for i in range (abs(int(y*100))):
            if GPIO.input(LS3Y) and GPIO.input(LS4Y) and stop == False:
                GPIO.output(puly, GPIO.HIGH)
                sleep(frequency)
                GPIO.output(puly, GPIO.LOW)
                sleep(frequency)
        current_position['Y'] += y
        print('Pulses: ', i, ' Speed: ', fy )
        stop = False
        return
        
    except: 
        print('Speed out of range')
        return

def xy_move(x=1, y=1):
    time = 0
    if x > y:
        fx = 2
        time = abs(x/fx)
        fy = abs(y/time)
    elif x < y:
        fy = 2
        time = abs(y/fy)
        fx = abs(x/time)
    else: 
        fx = 2
        fy = 2
    t = threading.Thread(target = y_move, args= (y, fy))
    t.start()
    x_move(x,fx)
    
    
def main(): 
    while True:
        print('1-X\n2-Y\n3-XY\n4-Z\n5-F')
        option = input('Enter your option: ')
        value = input ('Enter your value: ')
        speed = input ('Enter your speed: ')
        if option == 1 : 
            x_move(value,speed)
        elif option == 2 : 
            y_move(value,speed)
        elif option == 3: 
            yvalue = input ('Enter the value of y axis: ')
            xy_move(value,yvalue)
        elif option == 4: 
            z_move(value,speed)
        elif option == 5: 
            f_move(value,speed)
        else: 
            break
    x_move(3)
    y_move(3)
    xy_move(3, 3)

if __name__ == '__main__':
    main()