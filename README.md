# Session 5 Assignment 

This repository contains a Python module session5.py that implements several functions for various computations and conversions. Here's an overview of the functions provided:


## Function: `time_it`

**time_it(fn, \*args, repetitions=1,\*\*kwargs)**

This function measures the average execution time of any given function fn over a specified number of repetitions.

```python
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

```

### Tests and Explanation:
To test the `time_it` function, we can time the execution of the `print` or any other function with a simple string and repetitions set to 5:

Example:

```python
time_taken = time_it(print, "Hello, World!", repetitions=5)
print(f"Average time taken: {time_taken} seconds")
```

The `time_it` function measures the average time taken for a function to execute a specified number of times. It uses the `time` module to calculate the elapsed time between function calls.


## Function : squared_power_list

**squared_power_list(number, start=0, end=5)**

This function generates a list of powers of a given number (`number`) from `start` to `end-1`.

```python
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
```

### Parameters:
- `number`: Integer - The base number for which powers are calculated.
- `start`: Integer (default: 0) - Starting exponent (inclusive).
- `end`: Integer (default: 5) - Ending exponent (exclusive).

### Returns:
- List: A list containing `number**start` to `number**(end-1)`.

### Exceptions:
- `TypeError`: Raised if `number` is not an integer.
- `ValueError`: Raised if `start` or `end` is negative, or if `number` is greater than 10.
- `TypeError`: Raised if there are extra positional or keyword arguments.


### Usage Example:

```python
result = squared_power_list(2, start=0, end=5)
print(result)  # Output: [1, 2, 4, 8, 16]
```

---

## Tests for `squared_power_list`

The following tests ensure that the `squared_power_list` function behaves correctly under various conditions:

- **No Arguments Test**:

```python
def test_session5_squared_power_list_no_args():
    with pytest.raises(TypeError, match=r".*required positional argument: 'number'*"):
        session5.squared_power_list()
```

- **Incorrect Positional Arguments Test**:

```python
def test_session5_squared_power_list_incorrect_pos_args():
    with pytest.raises(TypeError, match=r".*Only integer type arguments are allowed*"):
        session5.squared_power_list('sac')
```

- **Invalid Start and End Test**:

```python
def test_session5_squared_power_list_incorrect_start__end():
    with pytest.raises(ValueError, match=r".*Value of start or end can't be negative*"):
        session5.squared_power_list(2, start=-1)
```

- **Number Greater than 10 Test**:

```python
def test_session5_squared_power_list_number_gt_10():
    with pytest.raises(ValueError, match=r".*Value of number should be less than 10*"):
        session5.squared_power_list(15)
```

- **Unwanted Arguments Test**:

```python
def test_session5_squared_power_list_unwanted_args():
    with pytest.raises(TypeError, match=r".*takes maximum 1 positional arguments*"):
        session5.squared_power_list(1, 2, start=1, end=5)
```

- **Output Verification Test**:

```python
def test_session5_squared_power_list_output():
    assert session5.squared_power_list(2, start=1, end=4) == [2, 4, 8]
```

These tests ensure robustness and correctness of the `squared_power_list` function across various edge cases and typical usage scenarios.


## Function: `polygon_area`

**polygon_area(length, \*args, sides=3, \*\*kwargs)**

This function calculates the area of a regular polygon with a specified number of sides (`3` to `6` inclusive).

```python
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
```

### Parameters:
- `length`: Integer - Length of each side of the polygon.
- `*args`: Additional positional arguments (not allowed).
- `sides`: Integer (default: 3) - Number of sides of the polygon (must be between 3 and 6 inclusive).
- `**kwargs`: Additional keyword arguments (not allowed).

### Returns:
- Float: Area of the regular polygon rounded to 2 decimal places.

### Exceptions:
- `TypeError`: Raised if `length` or `sides` is not an integer, or if there are extra positional or keyword arguments.
- `ValueError`: Raised if `length` is negative, or if `sides` is not between 3 and 6 inclusive.

### Usage Example:
```python
result = polygon_area(5, sides=4)
print(result)  # Output: 25.0
```

---

## Tests for `polygon_area`

The following tests ensure that the `polygon_area` function behaves correctly under various conditions:

- **No Arguments Test**:
```python
def test_polygon_area_no_args():
    with pytest.raises(TypeError, match=r".*required positional argument: 'length'*"):
        polygon_area()
```

- **Incorrect Positional Arguments Test**:
```python
def test_polygon_area_incorrect_pos_args():
    with pytest.raises(TypeError, match=r".*polygon_area function takes maximum 1 positional arguments, more provided*"):
        polygon_area(5, 6)
```

- **Invalid Length Test**:
```python
def test_polygon_area_invalid_length():
    with pytest.raises(ValueError, match=r".*Value of length must be greater than 0*"):
        polygon_area(-5)
```

- **Invalid Sides Test**:
```python
def test_polygon_area_invalid_sides():
    with pytest.raises(ValueError, match=r".*Value of sides must be between 3 to 6*"):
        polygon_area(5, sides=7)
```

- **Number Greater than 10 Test**:
```python
def test_polygon_area_number_gt_10():
    with pytest.raises(TypeError, match=r".*Only integer type arguments are allowed for length*"):
        polygon_area('abc')
```

- **Output Verification Test**:
```python
def test_polygon_area_output():
    assert polygon_area(5, sides=4) == 25.0
```

These tests cover various edge cases and typical usage scenarios to ensure the correctness and robustness of the `polygon_area` function.


## Function: `temp_converter`

**temp_converter(temp, \*args, temp_given_in='f', \*\*kwargs)**

This function converts temperature between Celsius (`'c'`) and Fahrenheit (`'f'`).

```python
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
```


### Parameters:
- `temp`: Integer or Float - Temperature value to be converted.
- `*args`: Additional positional arguments (not allowed).
- `temp_given_in`: String (default: 'f') - Unit of the temperature provided (`'f'` for Fahrenheit or `'c'` for Celsius).
- `**kwargs`: Additional keyword arguments (not allowed).

### Returns:
- Float: Converted temperature value in the opposite unit.

### Exceptions:
- `TypeError`: Raised if `temp` is not an integer or float, or if `temp_given_in` is not a string.
- `ValueError`: Raised if `temp_given_in` is not `'f'` or `'c'`, or if the temperature falls below absolute zero (-459.67°F or -273.15°C).

### Usage Example:
```
result = temp_converter(32, temp_given_in='f')
print(result)  # Output: 0.0
```

---

## Tests for `temp_converter`

The following tests ensure that the `temp_converter` function behaves correctly under various conditions:

- **No Arguments Test**:
```python
def test_temp_converter_no_args():
    with pytest.raises(TypeError, match=r".*required positional argument: 'temp'*"):
        temp_converter()
```

- **Incorrect Positional Arguments Test**:
```python
def test_temp_converter_incorrect_pos_args():
    with pytest.raises(TypeError, match=r".*temp_converter function takes maximum 1 positional arguments, more provided*"):
        temp_converter(32, 45)
```

- **Invalid Temperature Type Test**:
```python
def test_temp_converter_invalid_temp_type():
    with pytest.raises(TypeError, match=r".*Only integer or float type arguments are allowed for temp*"):
        temp_converter('abc', temp_given_in='f')
```

- **Invalid Temperature Unit Test**:
```python
def test_temp_converter_invalid_temp_unit():
    with pytest.raises(ValueError, match=r".*Only f or c is allowed for temperature units*"):
        temp_converter(32, temp_given_in='k')
```

- **Temperature Below Absolute Zero Test**:
```python
def test_temp_converter_below_absolute_zero():
    with pytest.raises(ValueError, match=r".*Temprature can't go below -459.67 fahrenheit = 0 Kelvin*"):
        temp_converter(-500, temp_given_in='f')
```

- **Output Verification Test**:
```python
def test_temp_converter_output():
    assert temp_converter(32, temp_given_in='f') == 0.0
    assert temp_converter(0, temp_given_in='c') == 32.0
```

These tests cover various edge cases and typical usage scenarios to ensure the correctness and robustness of the `temp_converter` function.


## Function: `speed_converter`


**speed_converter(speed, \*args, dist='km', time='min', \*\*kwargs)**

This function converts speed from kmph to different units of distance (`dist`) and time (`time`).

```python

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

```

### Parameters:
- `speed`: Integer or Float - Speed in kilometers per hour (kmph) to be converted.
- `*args`: Additional positional arguments (not allowed).
- `dist`: String (default: 'km') - Unit of distance to convert to (`'km'`, `'m'`, `'ft'`, `'yrd'`).
- `time`: String (default: 'min') - Unit of time to convert to (`'ms'`, `'s'`, `'min'`, `'hr'`, `'day'`).
- `**kwargs`: Additional keyword arguments (not allowed).

### Returns:
- Integer: Converted speed value in the specified units of distance per unit of time.

### Exceptions:
- `TypeError`: Raised if `speed` is not an integer or float, or if `dist` or `time` are not strings.
- `ValueError`: Raised if `speed` is negative or exceeds the speed of light (300,000 km/s), or if `dist` or `time` units are incorrect.

### Usage Example:
```python
result = speed_converter(100, dist='m', time='s')
print(result)  # Output: 27
```

---

## Tests for `speed_converter`

The following tests ensure that the `speed_converter` function behaves correctly under various conditions:

### No Arguments Test:
```python
def test_speed_converter_no_args():
    with pytest.raises(TypeError, match=r".*required positional argument: 'speed'*"):
        speed_converter()
```

### Incorrect Positional Arguments Test:
```python
def test_speed_converter_incorrect_pos_args():
    with pytest.raises(TypeError, match=r".*speed_converter function takes maximum 1 positional arguments, more provided*"):
        speed_converter(100, 200)
```

### Invalid Speed Type Test:
```python
def test_speed_converter_invalid_speed_type():
    with pytest.raises(TypeError, match=r".*Speed can be int or float type only*"):
        speed_converter('abc', dist='m', time='s')
```

### Invalid Distance Unit Test:
```python
def test_speed_converter_invalid_dist_unit():
    with pytest.raises(ValueError, match=r".*Incorrect unit of distance. Only km/m/ft/yrd allowed*"):
        speed_converter(100, dist='kmph', time='s')
```

### Invalid Time Unit Test:
```python
def test_speed_converter_invalid_time_unit():
    with pytest.raises(ValueError, match=r".*Incorrect unit of Time. Only ms/s/min/hr/day allowed*"):
        speed_converter(100, dist='m', time='hour')
```

### Speed Below Zero Test:
```python
def test_speed_converter_below_zero():
    with pytest.raises(ValueError, match=r".*Speed can't be negative*"):
        speed_converter(-100, dist='m', time='s')
```

### Speed Exceeds Limit Test:
```python
def test_speed_converter_exceeds_limit():
    with pytest.raises(ValueError, match=r".*Speed can't be greater than speed of light*"):
        speed_converter(500000, dist='m', time='s')
```

### Output Verification Test:
```python
def test_speed_converter_output():
    assert speed_converter(100, dist='m', time='s') == 27
    assert speed_converter(120, dist='ft', time='min') == 21168
```

These tests cover various edge cases and typical usage scenarios to ensure the correctness and robustness of the `speed_converter` function.