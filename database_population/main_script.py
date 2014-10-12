__author__ = 'lora'

from server_connector import UGRacingSQLServerConnector as sq
import time
import random

flag = 0

def GEAR(GEAR, RPM):
     global flag
     if(RPM <800):
         return 1
     else:
         if(flag == 0):
             GEAR = GEAR + 1
         if(flag == 1 ):
             GEAR = GEAR - 1
         if(GEAR >= 5):
             flag = 1
         if(GEAR <= 1):
              flag = 0

     return GEAR

flag2 = 0
def randomize(i):
    global flag2
    if(flag2 == 0):
        return round(i+random.uniform(1,4),3)
        flag2 = 1
    else:
        return round(i-random.uniform(1,4),3)
        flag2 = 0

def WHEEL_Temperature(SPEED):
    return SPEED*2.3

def SPEED(RPM):
    return RPM/100

def BRAKE(RPM_reference,RPM_current):
    if(RPM_reference-RPM_current < 0):
        r =  abs( RPM_reference - RPM_current)/2000

        if(r > 1):
            return 1
        else:
            return round(r, 3)

    return 0

def normalise_THROTTLE(value):
    if (float(value[4]) < 10):
        if (float(value[4]) < 0):
            value[4] = float(value[4]) * -9
        else:
            value[4] = float(value[4]) * 9
    return value



def main():

    connection = sq('http://127.0.0.1:8000/telemetry-api/add-values/', 'root', 'Ellsolan', 'Hackathon')
    max   =  0
    RPM_current = 0
    RPM_comparison = 0
    f = open('engine_log.txt', 'r')
    value_position = {2:'RPM', 3:'MAP',4: 'THROTTLE', 5: 'O2', 6: 'MAT', 7: 'Coolant_T', 29:'Battery'}
    non_engine_sensors = {'SPEED': 0, 'GEAR': 0, 'BRAKE' : 0 , 'Wheel_V': 0, 'WHEEL_T': 0, 'FUEL': 0.8}
    WHEEL_Temperature_array = [0,0,0,0]
    wheel_SPEED_array = [0,0,0,0]

    lines = f.readlines()
    counter_BRAKE = 0
    counter_GEAR = 0
    while (True):

        for line in lines:
            start = time.time()
            print 'in for loop'
            counter_GEAR = counter_GEAR + 1
            values = line.split('\t')
            RPM_current = float(values[2])
            values = normalise_THROTTLE(values)

            non_engine_sensors['SPEED'] = SPEED(RPM_current)
            non_engine_sensors['Wheel_V'] = 1.76*non_engine_sensors['SPEED']
            non_engine_sensors['WHEEL_T'] = WHEEL_Temperature(non_engine_sensors['SPEED'])

            if(counter_GEAR == 10 ):
                counter_GEAR = 0
                non_engine_sensors['GEAR'] = GEAR(non_engine_sensors['GEAR'], RPM_current)

            for i in range(0,4,1):
                WHEEL_Temperature_array[i] = randomize(non_engine_sensors['WHEEL_T'])
                wheel_SPEED_array[i] = randomize(non_engine_sensors['Wheel_V'])

            counter_BRAKE = counter_BRAKE + 1

            if(counter_BRAKE == 4) :
                counter_BRAKE = 0

                if(float(values[0])<3370):
                    reference_line = lines[lines.index(line)+4].split('\t')

                RPM_reference = int(reference_line[2])
                non_engine_sensors['BRAKE']= BRAKE(RPM_reference, RPM_current)

                connection.write_tag('SPEED', float(non_engine_sensors['SPEED']))

                i = 0
                for wheel in wheel_SPEED_array:
                    connection.write_tag('WHEEL_V_' + str(i+1), float(wheel_SPEED_array[i]))
                    i = i + 1

                i = 0
                for wheel in wheel_SPEED_array:
                    connection.write_tag('WHEEL_T_' + str(i+1), float(WHEEL_Temperature_array[i]))
                    i = i + 1

                connection.write_tag('BRAKE', float(non_engine_sensors['BRAKE']))
                connection.write_tag('GEAR', float(non_engine_sensors['GEAR']))
                connection.write_tag('FUEL', float(non_engine_sensors['FUEL']))

            for i in range(0,len(values), 1):
                if(i in value_position.keys()):
                    connection.write_tag(value_position[i], float(values[i]))

 
            connection.commit()
            end = time.time()
            
            while ((end-start) < 0.2):
                 time.sleep(0.1)
                 end = time.time()

            end = time.time()
            
            print 'time taken is ' + str(end - start)


main()
