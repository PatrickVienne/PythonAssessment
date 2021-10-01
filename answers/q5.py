#############################
# whats the difference (1)? #
#############################
a = (1, 2, 3, "12")  # tuple, immutable, can have duplicates
b = [1, 2, 3, "12"]  # list, mutable, can have duplicates
c = {1, 2, 3, "12"}  # set, mutable, cannot have duplicates

#############################
# whats the difference (2)? #
#############################

d = (a for a in range(10) if a % 2 == 0)  # generator
e = [a for a in range(10) if a % 2 == 0]  # generator


#############################
# whats the difference (3)? #
#############################
def get_lines_f():
    with open(__file__, "r") as f:
        for line in f:
            yield line


f = get_lines_f()  # generator iterates line by line and stops with StopIteration if next(f) is called but f ends


def get_lines_g():
    with open(__file__, "r") as f:
        return f.readlines()


g = get_lines_g()  # list of strings


#############################
# whats the difference (4)? #
#############################
h = raw_input()
i = input()

'''
In Python 2x hat input die Eingabe mit einem eval()-Statement
direkt ausgewertet, raw_input allerdings nicht.
In Python 3x, wurde raw_input zu input umbenannt.
'''


#############################
# whats the difference (5)? #
#############################
j = range(10)
k = xrange(10)

'''
In Python2, wird mit xrange ein Iterator erzeugt, mit welchem über den Parameter
iteriert werden kann. Das ist sehr effizient. range erzeugt eine Liste mit den Werten, über welche
iteriert werden soll.
In Python2, gibt es kein xrange mehr.
'''

#############################
# whats the difference (6)? #
#############################
my_list = [1, 10, 2, 20, 5, 40]

l = sorted(my_list)  # saves the sorted copy into a new list, and thus slower
# or
my_list.sort()  # inplace operation. no copy, thus faster
k = my_list



#############################
# whats the difference (7)? #
#############################
# whats the difference of an array and a list?

"""
- array: single type
- array: broadcasting
- array: fixed length
...
"""
