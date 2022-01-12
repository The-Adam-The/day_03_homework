
months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]


def return_10():
    return 10

def add(x, y):
    result = x + y
    return result

def subtract(x, y):
    result = x - y
    return result

def multiply(x, y):
    result = x * y
    return result

def divide(x, y):
    result = x / y
    return result

def length_of_string(input_string):
    string_length = len(input_string)
    return string_length

def join_string(string_1, string_2):
    new_string = string_1 + string_2
    return new_string

def add_string_as_number(string_1, string_2):
    result = int(string_1) + int(string_2)
    return result

def number_to_full_month_name(month_n):
    return months[month_n - 1]

def number_to_short_month_name(month_n):
    return months[month_n - 1][:3]

def calculate_volume_of_cube(length):
    return length ** 3

def reverse_string(input_string):
    
    return input_string[::-1]

def fahrenheit_to_celsius(fahrenheit):
    return round((fahrenheit - 32) * 0.5556, 1)