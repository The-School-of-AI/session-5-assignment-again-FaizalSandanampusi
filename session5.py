"""WRITE PROPER ASSINGMENT DESCIPTION HERE AND DELETE THIS MESSAGE"""

import time
from math import pow,tan,pi

def time_it(fn, *args, repetitions= 1, **kwargs):
    """This is a genralized function to call any function
    user specified number of times and return the average
    time taken for calls"""

    filtered_kwargs = {k: v for k, v in kwargs.items() if k != 'repetitions'}

    # Repetition should be positive number
    if fn is None:
        raise TypeError("missing required positional argument: 'fn'")
    if repetitions<0:
        raise Exception("repetitions must be greater than 0")
    elif repetitions ==0:
        return 0
    else:
        start = time.perf_counter()
        for _ in range(repetitions):
            fn(*args, **filtered_kwargs)
        end = time.perf_counter()
        elapsed_time = end - start
        print(f"Function executed {repetitions} times in: {elapsed_time:.6f} seconds")


def squared_power_list(number,*args, start=0, end=5,**kwargs):
    """Retruns list by raising number to power from start to end
    -> number**start to number**end. Default start is 0 and end is 5"""

    # Validations "if" block
    if not isinstance(number,int):
        raise TypeError("Only integer type arguments are allowed")
    if start<0 or end<0:
        raise ValueError("Value of start or end can't be negative")
    if end<start:
        raise ValueError("Value of start should be less than end")
    if number>10:
        raise ValueError("Value of number should be less than 10")
    if len(args)>0:
        raise TypeError("The function squared_power_list takes maximum 1 positional arguments")
    if len(kwargs)>0:
        raise TypeError("The function squared_power_list takes maximum 2 keyword/named arguments")
    return [number**i for i in range(start,end)]


def polygon_area(length, *args, sides = 3, **kwargs):
    """Returns area of a regular polygon with number of sides between
    3 to 6 both inclusive"""
    # Validations
    if not isinstance(length,int):
        raise TypeError("Only integer type arguments are allowed for length")
    if not isinstance(sides,int):
        raise TypeError("Only integer type arguments are allowed for sides")
    if length<0:
        raise ValueError("Value of length must be greater than 0")
    if sides<3 or sides>6:
        raise ValueError("Value of sides must be between 3 to 6")
    if len(args)>0:
        raise TypeError("polygon_area function takes maximum 1 positional arguments, more provided")
    if len(kwargs)>0:
        raise TypeError("polygon_area function take maximum 1 keyword/named arguments, more provided")
    return round((1/4)*sides*pow(length,2)*1/tan(pi/sides),2)

def temp_converter(temp, *args, temp_given_in = 'f', **kwargs):
    """Converts temprature from celsius 'c' to fahrenheit 'f' or
    fahrenheit to celsius"""

    # Validations
    if (not isinstance(temp,int)) and (not isinstance(temp,float)):
        raise TypeError("Only integer or float type arguments are allowed for temp")
    if not isinstance(temp_given_in,str):
        raise TypeError("Charcater string expected")
    if temp_given_in.strip().lower() not in ('f','c'):
        raise ValueError("Only f or c is allowed for temperature units") 
    if len(args)>0:
        raise TypeError("temp_converter function takes maximum 1 positional arguments, more provided")
    if len(kwargs)>0:
        raise TypeError("temp_converter function take maximum 1 keyword/named arguments, more provided")

    # Return the converted temprature
    if temp_given_in.strip().lower()=='f':
        if temp<-459.67:
            raise ValueError("Temprature can't go below -459.67 fahrenheit = 0 Kelvin")
        else:
            return 5/9*(temp-32)
    if temp_given_in.strip().lower()=='c':
        if temp<-273.15:
            raise ValueError("Temprature can't go below -273.15 celsius = 0 Kelvin")
        else:
            return 9/5*temp+32



def speed_converter(speed, *args, dist='km', time='min', **kwargs):
    """Converts speed from kmph (provided by user as input) to different units
    dist can be km/m/ft/yrd time can be ms/s/min/hr/day """

    # Validations
    if (not isinstance(speed,int)) and (not isinstance(speed,float)):
        raise TypeError("Speed can be int or float type only")
    if not isinstance(dist,str):
        raise TypeError("Charcater string expected for distance unit")
    if not isinstance(time,str):
        raise TypeError("Charcater string expected")
    if speed<0:
        raise ValueError("Speed can't be negative")
    if speed>300000:
        raise ValueError("Speed can't be greater than speed of light")
    if time.strip().lower() not in ('ms','s','min','hr','day'):
        raise ValueError("Incorrect unit of Time. Only ms/s/min/hr/day allowed")
    if dist.strip().lower() not in ('km','m','ft','yrd'):
        raise ValueError("Incorrect unit of distance. Only km/m/ft/yrd allowed")
    if len(args)>0:
        raise TypeError("speed_converter function takes maximum 1 positional arguments, more provided")
    if len(kwargs)>0:
        raise TypeError("speed_converter function take maximum 2 keyword/named arguments, more provided")

    time_unit={'ms':3.6e+6,'s':3600,'min':60,'hr':1,'day':1/24}
    dist_unit={'km':1,'m':1000,'ft':3280.8373,'yrd':1093.609}

    time=time.strip().lower()
    dist=dist.strip().lower()

    return round(speed*(dist_unit[dist]/time_unit[time]))