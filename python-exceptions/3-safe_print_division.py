#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        result = a / b
        print("Inside result: {}".format(result))
    except:
        print("Inside result: {}".format(None))
        result = None
    finally:
        return(result)