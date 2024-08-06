import pytest
import random
import string
import test_session5
import os
import inspect
import re
import math
import time
from test_session5 import squared_power_list
from test_session5 import polygon_area
from test_session5 import temp_converter
from test_session5 import speed_converter
from test_session5 import time_it

README_CONTENT_CHECK_FOR = [
    'time_it(fn, *args, repetitions= 1, **kwargs)',
    'squared_power_list',
    'polygon_area',
    'temp_converter',
    'speed_converter'
]

def test_session5_readme_exists():
    """ 
        This test checks whether a README.md file exists in the current project
    """
    assert os.path.isfile("README.md"), "README.md file missing!"


def test_session5_readme_500_words():
    """ 
        This test checks whether the readme file contains atleast 500 words
    """
    readme = open("README.md", "r")
    readme_words = readme.read().split()
    readme.close()
    assert len(readme_words) >= 500, "Make your README.md file interesting! Add atleast 500 words"

def test_session5_readme_proper_description():
    """ 
        This test cheecks whether the readme file contains good description of the assignment and
        checks if it has expected keywords. The keywords are defined globally in this file.
    """
    READMELOOKSGOOD = True
    f = open("README.md", "r", encoding="utf-8")
    content = f.read()
    f.close()
    for c in README_CONTENT_CHECK_FOR:
        if c not in content:
            READMELOOKSGOOD = False
            pass
    assert READMELOOKSGOOD == True, "You have not described all the functions/class well in your README.md file"

def test_session5_readme_file_for_more_than_10_hashes():
    """ 
        This code checks for formatting for readme file exisits. 
        It checks if there are hashes in the file which indicates
        usage of heading and comments in the readme file.There must 
        be atleast 10 hashes for function test to pass. 
    """
    f = open("README.md", "r", encoding="utf-8")
    content = f.read()
    f.close()
    assert content.count("#") >= 10

def test_session5_indentations():
    """ 
        Returns pass if used four spaces for each level of syntactically \
        significant indenting (spaces%4 == 2 and spaces%4 ==0).
    """
    lines = inspect.getsource(test_session5)
    spaces = re.findall('\n +.', lines)
    for space in spaces:
        assert len(space) % 4 == 2, "Your script contains misplaced indentations"
        assert len(re.sub(r'[^ ]', '', space)) % 4 == 0, "Your code indentation does not follow PEP8 guidelines"


def test_session5_function_name_had_cap_letter():
    """
        This test checks whether the functions defined in the assignment
        file contains captial letters. As per the standard functions must
        not be defined in capital letters.
    """
    functions = inspect.getmembers(test_session5, inspect.isfunction)
    for function in functions:
        assert len(re.findall('([A-Z])', function[0])) == 0, "You have used Capital letter(s) in your function names"



############################## Assignment Validations###########################

def test_session5_time_it_print():
    """This function tests time_it with the print function, calling it 5 times,
       and checks if any exceptions are raised.
    """
    try:
        time_it(print, repetitions=5)
    except Exception as e:
        pytest.fail(f"time_it can't time print function: {e}")

    assert True, "Test passed!"


def test_session5_time_it_squared_power_list():
    """
        This function tests time_it with the squared_power function, calling it 5 times,
       and checks if any exceptions are raised.
    """
    try:
        time_it(squared_power_list,random.randint(1,9),start=0,end=random.randint(1,5), repetitions=5)
    except Exception as e:
        pytest.fail(f"time_it can't time squared_power_list function: {e}")

    assert True, "Test passed!"


def test_session5_time_it_polygon_area():
    """
        This function tests time_it with the polygon_area function, calling it 10 times,
       and checks if any exceptions are raised.
    """
    try:
        time_it(polygon_area,random.randint(2,10),sides=random.randint(3,6), repetitions=10)
    except Exception as e:
        pytest.fail(f"time_it can't time polygon_area function: {e}")

    assert True, "Test passed!"


def test_session5_time_it_temp_converter():
    """
        This function tests time_it with the temp_converter function, calling it 100 times,
       and checks if any exceptions are raised.
    """
    try:
        time_it(temp_converter,random.randint(10,100),temp_given_in=random.choice(['f','c']), repetitions=100)
    except Exception as e:
        pytest.fail(f"time_it can't time temp_converter function: {e}")

    assert True, "Test passed!"


def test_session5_time_it_speed_converter():
    """
       This function tests time_it with the speed_converter function, calling it 200 times,
       and checks if any exceptions are raised.
    """
    try:
        time_it(speed_converter,random.randint(10,100),dist=random.choice(['km','m','ft','yrd']), \
            time=random.choice(['ms','s','min','hr','day']), repetitions=100)
    except Exception as e:
        pytest.fail(f"time_it can't time temp_converter function: {e}")

    assert True, "Test passed!"



####################### Validations for time_it#################################

def test_session5_time_it_no_args():
    """ DON'T TOUCH THIS FUNCTION \
        Test time_it with no arguments"""
    with pytest.raises(TypeError, match=r".*required positional argument: 'fn'*"):
        test_session5.time_it()


def test_session5_time_it_incorrect_pos_args():
    """ DON'T TOUCH THIS FUNCTION \
        Test time_it with non existing positional arguments"""
    with pytest.raises(NameError, match=r".*is not defined*"):
        test_session5.time_it(unknown_fn,repetitions=1)


def test_session5_time_it_zero_rep():
    """ DON'T TOUCH THIS FUNCTION \
        Test time_it with zero repetation. Should return 0 avg time"""
    assert test_session5.time_it(print, 1, 2, 3, sep='-', end=' ***\n', repetitions=0) == 0, "time_it should retun 0 for no function call"
    assert test_session5.time_it(squared_power_list, 2, start=0, end=5, repetitions=0) == 0, "time_it should retun 0 for no function call"
    assert test_session5.time_it(polygon_area, 15, sides=3, repetitions=0) == 0, "time_it should retun 0 for no function call"
    assert test_session5.time_it(speed_converter, 100, dist='km', time='min', repetitions=0) == 0, "time_it should retun 0 for no function call"
    assert test_session5.time_it(temp_converter, 100, temp_given_in = 'f', repetitions=0) == 0, "time_it should retun 0 for no function call"


####################### Validations for squared_power_list()####################

def test_session5_squared_power_list_no_args():
    """DON'T TOUCH THIS FUNCTION \
        Test squared_power function for no mandatory positional arguments"""
    with pytest.raises(TypeError, match=r".*required positional argument: 'number'*"):
        test_session5.squared_power_list()

def test_session5_squared_power_list_incorrect_pos_args():
    """DON'T TOUCH THIS FUNCTION \
        Test squared_power_list function for incorrect values for positional arguments"""
    with pytest.raises(TypeError, match=r".*Only integer type arguments are allowed*"):
        test_session5.squared_power_list('sac')
    with pytest.raises(TypeError, match=r".*Only integer type arguments are allowed*"):
        test_session5.squared_power_list(1+2j)

def test_session5_squared_power_list_incorrect_start__end():
    """DON'T TOUCH THIS FUNCTION \
        Test squared_power_list function for incorrect value to start keyword arguments"""
    with pytest.raises(ValueError, match=r".*Value of start or end can't be negative*"):
        test_session5.squared_power_list(2,start=-1)
    with pytest.raises(ValueError, match=r".*Value of start or end can't be negative*"):
        test_session5.squared_power_list(2,end=-1)

def test_session5_squared_power_list_start_gt_end():
    """DON'T TOUCH THIS FUNCTION \
        Test squared_power_list function for start value greater than end"""
    with pytest.raises(ValueError, match=r".*Value of start should be less than end*"):
        test_session5.squared_power_list(2,start=9,end=1)

def test_session5_squared_power_list_number_gt_10():
    """DON'T TOUCH THIS FUNCTION \
        Test squared_power_list function for number value greater than 10"""
    with pytest.raises(ValueError, match=r".*Value of number should be less than 10*"):
        test_session5.squared_power_list(15)

def test_session5_squared_power_list_unwanted_args():
    """DON'T TOUCH THIS FUNCTION \
        Test squared_power_list function for unwanted positional/keyword arguments"""
    with pytest.raises(TypeError, match=r".*takes maximum 1 positional arguments*"):
        test_session5.squared_power_list(1,2,start=1, end=5)
    with pytest.raises(TypeError, match=r".*maximum 2 keyword/named arguments*"):
        test_session5.squared_power_list(1,start=1, end=5, test = 0)

def test_session5_squared_power_list_output():
    """DON'T TOUCH THIS FUNCTION \
        Test squared_power_list function for output with multiple inputs"""
    assert test_session5.squared_power_list(1,start=1, end=5) == [1,1,1,1], "squared_power_list is not working as expected"
    assert test_session5.squared_power_list(2,start=1, end=4) == [2,4,8], "squared_power_list is not working as expected"



####################### Validations for polygon_area()####################
def test_session5_polygon_area():
    """Test polygon_area function for no mandatory positional arguments"""
    with pytest.raises(TypeError, match=r".*required positional argument: 'length'*"):
        test_session5.polygon_area()

def test_session5_polygon_area_length():
    """Test polygon_area function for incorrect values for positional argument length (check for string AND imaginary input)"""
    with pytest.raises(TypeError, match=r".*Only integer type arguments are allowed for length"):
        test_session5.polygon_area('string')
    with pytest.raises(TypeError, match=r".*Only integer type arguments are allowed for length"):
        test_session5.polygon_area(1+2j)

def test_session5_polygon_area_sides():
    """Test polygon_area function for incorrect value to sides keyword argument (string "ten" AND img input)"""
    with pytest.raises(TypeError, match=r".*Only integer type arguments are allowed for sides*"):
        test_session5.polygon_area(10,sides='ten')
    with pytest.raises(TypeError, match=r".*Only integer type arguments are allowed for sides*"):
        test_session5.polygon_area(10,sides=1+2j)

def test_session5_polygon_area_sides_values():
    """Test polygon_area function for permissible values for sides, check for 0, 1, 2, 7"""
    for i in [0,1,2,7]:
        with pytest.raises(ValueError, match=r".*Value of sides must be between 3 to 6*"):
            test_session5.polygon_area(10,sides=i)

def test_session5_polygon_area_length_values():
    """Test polygon_area function for permissible values for sides (len > 0)"""
    with pytest.raises(ValueError, match=r".*Value of length must be greater than 0*"):
        test_session5.polygon_area(-1,sides=3)

def test_session5_polygon_area_unwanted_args():
    """DON'T TOUCH THIS FUNCTION \
        Test polygon_area function for unwanted positional/keyword arguments"""
    with pytest.raises(TypeError, match=r".*polygon_area function takes maximum 1 positional arguments, more provided*"):
        test_session5.polygon_area(1, 2, sides=4)
    with pytest.raises(TypeError, match=r".*polygon_area function take maximum 1 keyword/named arguments, more provided*"):
        test_session5.polygon_area(1, sides=4, test = 0)

def test_session5_polygon_area_output():
    length = 10
    assert math.isclose(
        ((length ** 2) * math.sqrt(3)) / 4, test_session5.polygon_area(length, sides=3), rel_tol=1e-3
    ), "test_session5_polygon_area fails for 3 sides"
    assert math.isclose(
        length ** 2, test_session5.polygon_area(length, sides=4), rel_tol=1e-3
    ), "test_session5_polygon_area fails for 4 sides"
    assert math.isclose(
        172.05, test_session5.polygon_area(length, sides=5), rel_tol=1e-3
    ), "test_session5_polygon_area fails for 5 sides"
    assert math.isclose(
        (((3 * math.sqrt(3)) / 2) * (length ** 2)),
        test_session5.polygon_area(length, sides=6),
        rel_tol=1e-3,
    ), "test_session5_polygon_area fails for 6 sides"



####################### Validations for temp_converter()########################

def test_session5_temp_converter():
    """Test temp_converter function for no mandatory positional arguments"""
    with pytest.raises(TypeError, match=r".*required positional argument: 'temp'*"):
        test_session5.temp_converter()

def test_session5_temp_converter_temp():
    """Test temp_converter function for incorrect values for positional argument temp (check for string AND imaginary input) """
    with pytest.raises(TypeError, match=r".*Only integer or float type arguments are allowed for temp*"):
        test_session5.temp_converter('100')
    with pytest.raises(TypeError, match=r".*Only integer or float type arguments are allowed for temp*"):
        test_session5.temp_converter(100+0j)

def test_session5_temp_converter_temp_given_in():
    """ DON'T TOUCH THIS FUNCTION \
        Test temp_converter function for incorrect value to temp_given_in keyword argument"""
    with pytest.raises(ValueError, match=r".*Only f or c is allowed*"):
        test_session5.temp_converter(10,temp_given_in='K')
    with pytest.raises(TypeError, match=r".*Charcater string expected*"):
        test_session5.temp_converter(10,temp_given_in=1+2j)

def test_session5_temp_converter_temp_values_in_celsius():
    """ DON'T TOUCH THIS FUNCTION \
        Test temp_converter function for permissible values for temprature in celsius"""
    with pytest.raises(ValueError, match=r".*Temprature can't go below -273.15 celsius = 0 Kelvin*"):
        test_session5.temp_converter(-280,temp_given_in='C')

def test_session5_temp_converter_temp_values_in_fahrenheit():
    """ DON'T TOUCH THIS FUNCTION \
        Test temp_converter function for permissible values for temprature in fahrenheit"""
    with pytest.raises(ValueError, match=r".*Temprature can't go below -459.67 fahrenheit = 0 Kelvin*"):
        test_session5.temp_converter(-500,temp_given_in='F')

def test_session5_temp_converter_unwanted_args():
    """ DON'T TOUCH THIS FUNCTION \
        Test temp_converter function for unwanted positional/keyword arguments"""
    with pytest.raises(TypeError, match=r".*temp_converter function takes maximum 1 positional arguments, more provided*"):
        test_session5.temp_converter(100,2,temp_given_in='F')
    with pytest.raises(TypeError, match=r".*temp_converter function take maximum 1 keyword/named arguments, more provided*"):
        test_session5.temp_converter(100,temp_given_in='C', test = 0)

def test_session5_temp_converter_output_in_fahrenheit():
    """ DON'T TOUCH THIS FUNCTION \
        Test temp_converter function for output with multiple inputs in fahrenheit"""
    assert test_session5.temp_converter(25,temp_given_in='c') == 77.0, "temp_converter is not working as expected"
    assert test_session5.temp_converter(-25,temp_given_in='C') == -13.0, "temp_converter is not working as expected"

def test_session5_temp_converter_output_in_celsius():
    """ DON'T TOUCH THIS FUNCTION \
        Test temp_converter function for output with multiple inputs in celsius"""
    assert test_session5.temp_converter(77,temp_given_in='f') == 25.0, "temp_converter is not working as expected"
    assert test_session5.temp_converter(-13,temp_given_in='F') == -25, "temp_converter is not working as expected"


####################### Validations for speed_converter()########################

def test_session5_speed_converter():
    """ DON'T TOUCH THIS FUNCTION \
        Test speed_converter function for no mandatory positional arguments"""
    with pytest.raises(TypeError, match=r".*required positional argument: 'speed''*"):
        test_session5.speed_converter()

def test_session5_speed_converter_speed():
    """ DON'T TOUCH THIS FUNCTION \
        Test speed_converter function for incorrect values for positional argument temp"""
    with pytest.raises(TypeError, match=r".*Speed can be int or float type only*"):
        test_session5.speed_converter('sac')
    with pytest.raises(TypeError, match=r".*Speed can be int or float type only*"):
        test_session5.speed_converter(1+2j)

def test_session5_speed_converter_dist():
    """ DON'T TOUCH THIS FUNCTION \
        Test speed_converter function for incorrect type of value for dist keyword argument"""
    with pytest.raises(TypeError, match=r".*Charcater string expected for distance unit*"):
        test_session5.speed_converter(10,dist=10)
    with pytest.raises(TypeError, match=r".*Charcater string expected for distance unit*"):
        test_session5.speed_converter(10,dist=1+2j)

def test_session5_speed_converter_time():
    """ DON'T TOUCH THIS FUNCTION \
        Test speed_converter function for incorrect type of value for time keyword argument"""
    with pytest.raises(TypeError, match=r".*Charcater string expected*"):
        test_session5.speed_converter(10,time=10)
    with pytest.raises(TypeError, match=r".*Charcater string expected*"):
        test_session5.speed_converter(10,time=1+2j)

def test_session5_speed_converter_speed_allowed_values():
    """ DON'T TOUCH THIS FUNCTION \
        Test speed_converter function for permissible value for speed argument"""
    with pytest.raises(ValueError, match=r".*Speed can't be negative*"):
        test_session5.speed_converter(-100)
    with pytest.raises(ValueError, match=r".*Speed can't be greater than speed of light*"):
        test_session5.speed_converter(300001)

def test_session5_speed_converter_time_allowed_values():
    """ DON'T TOUCH THIS FUNCTION \
        Test speed_converter function for permissible value for time keyword argument"""
    with pytest.raises(ValueError, match=r".*Incorrect unit of Time. Only ms/s/min/hr/day allowed*"):
        test_session5.speed_converter(10,time='KM')
    with pytest.raises(ValueError, match=r".*Incorrect unit of Time. Only ms/s/min/hr/day allowed*"):
        test_session5.speed_converter(10,time='YRD')

def test_session5_speed_converter_dist_allowed_values():
    """ DON'T TOUCH THIS FUNCTION \
        Test speed_converter function for permissible value for dist keyword argument"""
    with pytest.raises(ValueError, match=r".*Incorrect unit of distance. Only km/m/ft/yrd allowed*"):
        test_session5.speed_converter(10,dist='MIN')
    with pytest.raises(ValueError, match=r".*Incorrect unit of distance. Only km/m/ft/yrd allowed*"):
        test_session5.speed_converter(10,dist='HR')

def test_session5_speed_converter_unwanted_args():
    """ DON'T TOUCH THIS FUNCTION \
        Test speed_converter function for unwanted positional/keyword arguments"""
    with pytest.raises(TypeError, match=r".*speed_converter function takes maximum 1 positional arguments, more provided*"):
        test_session5.speed_converter(100,2)
    with pytest.raises(TypeError, match=r".*speed_converter function take maximum 2 keyword/named arguments, more provided*"):
        test_session5.speed_converter(100,dist='M', time = 'HR', test = 'abc')

def test_session5_speed_converter_output_km_to():
    """ DON'T TOUCH THIS FUNCTION \
        Test speed_converter function for output with multiple inputs from km/(x), x can be ms/s/min/hr/day"""
    assert test_session5.speed_converter(36000,dist='KM',time='MS') == 0, "speed_converter is not working as expected"
    assert test_session5.speed_converter(36000,dist='KM',time='S') == 10, "speed_converter is not working as expected"
    assert test_session5.speed_converter(6000,dist='KM',time='MIN') == 100, "speed_converter is not working as expected"
    assert test_session5.speed_converter(100,dist='KM',time='HR') == 100, "speed_converter is not working as expected"
    assert test_session5.speed_converter(100,dist='KM',time='DAY') == 2400, "speed_converter is not working as expected"

def test_session5_speed_converter_output_m_to():
    """ DON'T TOUCH THIS FUNCTION \
        Test speed_converter function for output with multiple inputs from m/(x), x can be ms/s/min/hr/day"""
    assert test_session5.speed_converter(36000,dist='M',time='MS') == 10, "speed_converter is not working as expected"
    assert test_session5.speed_converter(3600,dist='M',time='S') == 1000, "speed_converter is not working as expected"
    assert test_session5.speed_converter(60,dist='M',time='MIN') == 1000, "speed_converter is not working as expected"
    assert test_session5.speed_converter(60,dist='M',time='HR') == 60000, "speed_converter is not working as expected"
    assert test_session5.speed_converter(24,dist='M',time='DAY') == 576000, "speed_converter is not working as expected"

def test_session5_speed_converter_output_ft_to():
    """ DON'T TOUCH THIS FUNCTION \
        Test speed_converter function for output with multiple inputs from ft/(x), x can be ms/s/min/hr/day"""
    assert test_session5.speed_converter(36000,dist='FT',time='MS') == 33, "speed_converter is not working as expected"
    assert test_session5.speed_converter(36000,dist='FT',time='S') == 32808, "speed_converter is not working as expected"
    assert test_session5.speed_converter(6000,dist='FT',time='MIN') == 328084, "speed_converter is not working as expected"
    assert test_session5.speed_converter(100,dist='FT',time='HR') == 328084, "speed_converter is not working as expected"
    assert test_session5.speed_converter(100,dist='FT',time='DAY') == 7874010, "speed_converter is not working as expected"

def test_session5_speed_converter_output_yrd_to():
    """ DON'T TOUCH THIS FUNCTION \
        Test speed_converter function for output with multiple inputs from yrd/(x), x can be ms/s/min/hr/day"""
    assert test_session5.speed_converter(36000,dist='YRD',time='MS') == 11, "speed_converter is not working as expected"
    assert test_session5.speed_converter(3600,dist='YRD',time='S') == 1094, "speed_converter is not working as expected"
    assert test_session5.speed_converter(6000,dist='YRD',time='MIN') == 109361, "speed_converter is not working as expected"
    assert test_session5.speed_converter(100,dist='YRD',time='HR') == 109361, "speed_converter is not working as expected"
    assert test_session5.speed_converter(100,dist='YRD',time='DAY') == 2624662, "speed_converter is not working as expected"