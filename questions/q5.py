#############################
# whats the difference (1)? #
#############################
a = (1, 2, 3, "12")
b = [1, 2, 3, "12"]
c = {1, 2, 3, "12"}

#############################
# whats the difference (2)? #
#############################

d = (a for a in range(10) if a % 2 == 0)
e = [a for a in range(10) if a % 2 == 0]


#############################
# whats the difference (3)? #
#############################
def get_lines_f():
    with open(__file__, "r") as f:
        for line in f:
            yield line


f = get_lines_f()


def get_lines_g():
    with open(__file__, "r") as f:
        return f.readlines()


g = get_lines_g()

#############################
# whats the difference (4)? #
#############################
h = raw_input()
i = input()



#############################
# whats the difference (5)? #
#############################
j = range(10)
k = xrange(10)


#############################
# whats the difference (6)? #
#############################
my_list = [1, 10, 2, 20, 5, 40]

l = sorted(my_list)
# or
my_list.sort()
k = my_list



#############################
# whats the difference (7)? #
#############################
# whats the difference of an array and a list?

