import math
from PIL import Image, ImageDraw

path = ''
current_positionT = {"X":0.0, "Y":0.0, "Z":0.0} 
home_positionT = {"X":10.0, "Y":20.0, "Z":0.0}
target_position = {"X":0.0, "Y":0.0, "Z":0.0}

abs = True
offset = {"X":0.0, "Y":0.0, "Z":0.0} 
toolpath = []
layer_value = []
toolpath.append({'N':0, 'X':0.0, 'Y':0.0, 'Z':0.0, 'G':0, 'M':0, 'LN': 0})
arc_end = {"X":0.0, "Y":0.0, "Z":0.0}
arc={"I":0.0,"J":0.0}
line_number = 0
toolpath_number = 0
layer_number = 1
status = False
gcode_line= []
color = ''

def get_homePosition():
    with open('C:/Users/at339/Desktop/IFproject/BjetController/code/Program/homeposition.txt','r') as hp:
        for line in hp:
            for word in line.split():
                if (word.startswith('X')):
                    x_valueB=word[1:len(word):1]
                    home_positionT['X']=float(x_valueB)
                if (word.startswith('Y')):
                    y_valueB=word[1:len(word):1]
                    home_positionT['Y']=float(y_valueB)
                if (word.startswith('Z')):
                    z_valueB=word[1:len(word):1]
                    home_positionT['Z']=float(z_valueB)
                if (word.startswith('F')):
                    z_valueB=word[1:len(word):1]
                    home_positionT['F']=float(z_valueB)
#for absolute positionining, store toolpath number where command was given; loop at the end of the line with if else with range(temp, toopath number) and modify array
def GCODE():
    global color
    global abs
    global line_number
    global toolpath_number
    global toolpath
    global layer_number
    global offset
    global gcode_line
    gcode_line = []
    line_number = 0
    layer_number = 1
    toolpath_number = 0
    gcode_line = []
    rapid=True
    linear = False
    circular = False 
    toolpath = []
    startG90 = []
    stopG90 = []
    toolpath.append({'N':0, 'X':0.0, 'Y':0.0, 'Z':0.0, 'G':0, 'M':0, 'LN': 0})
    with open(f'{path}gcode.txt','r') as file:
        status = True
        tempZ = 0.0
        temptp = 0
        angle_range = 0.0
        steps = 0.0
        for line in file:
            gcode_line.append(line)
            #toolpath.append({'N':0, 'X':0.0, 'Y':0.0, 'Z':0.0, 'G':0, 'M':0, 'LN':0})
            toolpath[toolpath_number]['N'] = line_number
            for word in line.split():
                if(word=='G01'):
                    rapid = True
                    linear = False
                    circular = False
                    
                    
                # if(word=='G01'):
                #     linear = True
                #     rapid = False
                #     circular = False
                    
                    
                if (word == "G02" or word == "G03"):
                    circular = True
                    rapid = False
                    linear = False
                    if(word=="G02"):
                        Direction="CW"
                    if(word=="G03"):
                        Direction="CCW"
                        
                        
                if(word=='G28'):
                    toolpath[toolpath_number]['G'] = 28
                    
                if(word == 'G90'):
                    startG90.append(toolpath_number)
                    abs = True
                if (word == 'G91'):
                    abs = False
                    stopG90.append(toolpath_number)
                
                
                    
                if(word.startswith('M')):
                    toolpath[toolpath_number]['M'] = int(word[1:len(word):1])
                
                
                if(word.startswith('Z')):
                    if float(word[1:len(word):1]) > tempZ : layer_number += 1
                    toolpath[toolpath_number]['LN'] = layer_number   
                    
                    
                if(rapid):
                    # toolpath[toolpath_number]['M'] = 101
                    toolpath[toolpath_number]['G'] = 1
                    if (word.startswith('X')):
                        x_value=word[1:len(word):1]
                        x_value=float(x_value)
                        current_positionT['X'] += x_value
                        toolpath[toolpath_number]['X'] = x_value
                    
                    if (word.startswith('Y')):
                        y_value=word[1:len(word):1]
                        y_value=float(y_value)
                        current_positionT['Y'] += y_value
                        toolpath[toolpath_number]['Y'] = y_value
        
                    if (word.startswith('Z')):
                        z_value=word[1:len(word):1]
                        z_value=float(z_value)
                        tempZ = z_value
                        current_positionT['Z'] += z_value
                        z_value -= offset['Z']
                        toolpath[toolpath_number]['Z'] = z_value
    

                if(linear):
                    if (word.startswith('X')):
                        x_value=word[1:len(word):1]
                        target_position["X"]=float(x_value)
                    if (word.startswith('Y')):
                        y_value=word[1:len(word):1]
                        target_position["Y"]=float(y_value)
                    # Calculate toolpath using parametric equation of straight line
                    dx = target_position["X"]-current_positionT["X"]
                    dy = target_position["Y"]-current_positionT["Y"]
                    dz = target_position["Z"]-current_positionT["Z"]
                    steps = int(max(abs(dx), abs(dy), abs(dz)))
   
                    for i in range(steps):
                        toolpath[toolpath_number]['X'] = (i/steps)*dx-offset['X']
                        toolpath[toolpath_number]['Y'] = (i/steps)*dy-offset['Y']
                        toolpath[toolpath_number]['Z'] = (i/steps)*dz-offset['Z']
                        toolpath[toolpath_number]['M'] = 101
                        toolpath[toolpath_number]['G'] = 1
                        current_positionT['X'] += (i/steps)*dx
                        current_positionT['Y'] += (i/steps)*dy
                        current_positionT['Z'] += (i/steps)*dz
                        if i != steps-1:
                            toolpath.append({'N':0, 'X':0.0, 'Y':0.0, 'Z':0.0, 'G':0, 'M':0, 'LN': layer_number})
                            toolpath_number += 1

                
                if(circular == True):
                    # if(word=="G02"):
                    #     Direction="CW"
                    # if(word=="G03"):
                    #     Direction="CCW"
                    if (word.startswith('X')):
                        x_value=word[1:len(word):1]
                        arc_end["X"]=float(x_value)
                    if (word.startswith('Y')):
                        y_value=word[1:len(word):1]
                        arc_end["Y"]=float(y_value)
                    if (word.startswith('I')):
                        i_value=word[1:len(word):1]
                        arc["I"]=float(i_value)
                    if (word.startswith('J')):
                        j_value=word[1:len(word):1]
                        arc["J"]=float(j_value)
                    center={"X":arc["I"]+current_positionT["X"],"Y":arc["J"]+current_positionT["Y"], "Z":
                    current_positionT["Z"]}
                    radius=((arc["I"]**2)+(arc["J"]**2))**0.5
                    start_angle=math.atan2(current_positionT["Y"]-center["Y"],current_positionT["X"]-center["X"])
                    end_angle=math.atan2(arc_end["Y"]-center["Y"],arc_end["X"]-center["X"])
                    if Direction=="CW":
                        if end_angle>=start_angle:
                            end_angle-=2*math.pi
                    else:
                        if end_angle<=start_angle:
                            end_angle+=2*math.pi
                    angle_range=end_angle-start_angle
                    steps=int((angle_range*radius)/3.0)
                    for i in range(steps):
                        angle=start_angle+i*angle_range/steps
                        x=center["X"]+radius*math.cos(angle)
                        y=center["Y"]+radius*math.sin(angle)
                        
                        print (round(x,2), round(y,2))
                        
                        toolpath[toolpath_number]['X'] = round(x,2)
                        toolpath[toolpath_number]['Y'] = round(y,2)
                        toolpath[toolpath_number]['M'] = 101
                        toolpath[toolpath_number]['G'] = 3
                        if i != steps-1:
                            toolpath.append({'N':line_number, 'X':0.0, 'Y':0.0, 'Z':0.0, 'G':0, 'M':0, 'LN': layer_number})
                            toolpath_number += 1
            
            
            
            line_number += 1
            toolpath.append({'N':line_number, 'X':0.0, 'Y':0.0, 'Z':0.0, 'G':0, 'M':0, 'LN': layer_number})
            toolpath_number += 1
        if (len(stopG90) !=  len(startG90)):
            stopG90.append(toolpath_number)
    
        tempx = []
        tempy = []
        tempz = []
        for i in range (0, toolpath_number):
            tempx.append(toolpath[i]['X'])
            tempy.append(toolpath[i]['Y'])
            tempz.append(toolpath[i]['Z'])

        # print('----------')
        for i in range (0, len(startG90)):
            print ('for loop running')
            for j in range (startG90[i], stopG90[i]-1):
            # print('for loop is running')
                if toolpath[j+1]['X'] != 0 and toolpath[j+1]['Y'] != 0 and toolpath[j+1]['Z'] != 0:
                    print('if statement working')
                    toolpath[j+1]['X'] -= tempx[j]
                    toolpath[j+1]['Y'] -= tempy[j]
                    toolpath[j+1]['Z'] -= tempz[j]
        
    
    for i in range(0, toolpath_number+1):
        print(toolpath[i])
    # print (len(toolpath))
    print (toolpath_number)
    # print(line_number)
    # print(layer_number)
            
def tp_visualizer():
    global color
    global toolpath
    global toolpath_number
    global layer_number
    current_positionT = {"X":0.0, "Y":0.0, "Z":0.0}
    SF = 1.28888888889
    get_homePosition()
    for i in range (1, layer_number+1):
        toolpath_visual = Image.new(mode = 'RGB', size=(600,464), color = "white" ) #cartesian size: 340 by 340
        plot = ImageDraw.Draw(toolpath_visual)
        
        for k in range (0, 24):
            # num = str(k*20)
            # plot.text(xy= (1, 340 - (k*20) ), text = f'{num}', fill= 'black', align='right', size= 0.5)
            plot.line(xy = (0, 1.288*((340- (k*20))), 600, 1.288*(340-(k*20))), fill = '#D6D6D6', width = 1  )
            #if k != 0:
                # plot.text(xy= ((k*20), 342 ), text = f'{num}', fill= 'black', align='left', size= 0.5)
            plot.line(xy = (1.288*(20+(k*20)), 0, 1.288*(20+(k*20)), 1.288*360), fill = '#D6D6D6', width = 1  )
        plot.line(xy = (1.288*(60.0+home_positionT['Y']), 1.288*(340-home_positionT['X']), 1.288*(60.0+340), 1.288*(340-home_positionT['X']) ), fill = 'black', width = 2 ) #down-axis
        plot.line(xy = (1.288*(60.0+home_positionT['Y']), 1.288*(340-home_positionT['X']), 1.288*(60.0+home_positionT['Y']), 1.288*20), fill = 'black', width = 2 ) #upaxis
        plot.line(xy = (1.288*(60.0+home_positionT['Y']), 1.288*(19-home_positionT['X']), 1.288*(60.0+340), 1.288*(20-home_positionT['X']) ), fill = 'black', width = 2 ) #down-axis
        plot.line(xy = (1.288*(60.0+340+home_positionT['Y']), 1.288*(340-home_positionT['X']), 1.288*(60.0+340+home_positionT['Y']), 1.288*20), fill = 'black', width = 2 ) #upaxis
        
        
                
        
        for j in range(0, toolpath_number):
            if toolpath[j]['LN'] == i:
                temp = toolpath[j]['M']
                print(f'Toolpath {j}: {temp}')
                if toolpath[j]['M'] == 101: color = 'orange'
                elif toolpath[j]['M'] == 103: color = 'red'
                else: color = 'orange'
                    
                 
                plot.line(
                xy=(1.288*(60.0+(current_positionT['Y'])+home_positionT['Y']),
                    1.288*(340-(current_positionT['X'])-home_positionT['X']), 
                    1.288*(60.0+(toolpath[j]['Y']+current_positionT['Y'])+home_positionT['Y']), 
                    1.288*(340-(toolpath[j]['X']+current_positionT['X'])-home_positionT['X'])), 
                 
                
                
                fill = color, width=2) #xy = (yi, 340-xi, 340-yf, 340-xf)
                current_positionT['X'] += toolpath[j]['X']
                current_positionT['Y'] += toolpath[j]['Y']
        
        
        name = str(i)
        if __name__ == '__main__': toolpath_visual.show()
        toolpath_visual.save(f'assets/frame0/layer_{name}.png')
        # toolpath_visual.save(f'assets/frame0/layer_500.png')
    print('toolpath is generated')
    
def Feed_height():
    return toolpath[toolpath_number]['Z']

def get_gcodeLine():
    return gcode_line
    

if __name__ == '__main__':
    GCODE()
    tp_visualizer() 
    print(gcode_line)


