# Algunos ejemplos de errores para capturar en excepciones:
# ZeroDivisionError: division by zero, ej: x/0
# NameError: name 'spam' is not defined, ej: spam no fue declarada
# TypeError: can only concatenate str (not "int") to str, ej: "2" + 2
#

'''def main():
    try:
        configuration = open('config.txt')
    except FileNotFoundError as err:
        print("got a problem trying to read the file:", err)
    except IsADirectoryError:
        print("Found config.txt but it is a directory, couldn't read it")
    except (BlockingIOError, TimeoutError):
        print("Filesystem under heavy load, can't complete reading configuration file")

if __name__ == '__main__':
    main()'''

def water_left(astronauts, water_left, days_left):
    daily_usage = astronauts * 11
    total_usage = daily_usage * days_left
    total_water_left = water_left - total_usage
    if total_water_left < 0:
        raise RuntimeError(f"There is not enough water for {astronauts} astronauts after {days_left} days!")
    return f"Total water left after {days_left} days is: {total_water_left} liters"

try:
    water_left(5, 100, 2)
except RuntimeError as err:
    print("ALERT!: ",err)