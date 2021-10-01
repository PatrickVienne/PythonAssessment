import logging
import sys
import traceback
# find the errors, what could be improved?

try:
    _input = int(input("Select a number between 1 and 100: "))  # do not overwrite input, # parse the input, # rename veriable
    for num in range(1, _input+1):
        if num % 3 == 0 and num % 5 == 0:  # do not use "=" for comparison but "=="
            print("fizzbuzz")
        elif num % 3 == 0:  # ":" character was forgotten
            print("fizz")
        elif num % 5 == 0:  # "==0" was forgotten
            print("buzz")
        else:
            print(num)
except Exception as e:  # do not use umbrella exception, but at least except Exception
    logging.exception("That wasn't a number. You killed it. Nice work.")  # use log.exception or print_exception to not swaller traceback
    #traceback.print_exception(*sys.exc_info())  # for also printing the traceback
