##################
# print 20 stars #
##################
print('*' * 20)

###############################################################
# write a lotto generator which take 6 from the range 1 to 49 #
###############################################################

# good answer
import random
lottonumbers = random.sample(range(1, 50), 6)
lottonumbers.sort()

# bad (but better than no answer)
lottonumbers = []
while len(lottonumbers) < 6:
    num = random.randint(1, 50)
    while num in lottonumbers:
        num = random.randint(1, 50)
    lottonumbers.append(num)
lottonumbers.sort()
print(lottonumbers)

#######################################
# how to sort a list of dictionaries? #
#######################################
# sort the dictionaries by timestamp
my_data = [
    {"timestamp": 1.02, "info": "Order data Received", "price": 20},
    {"timestamp": 2, "info": "Order Data Received", "price": 30},
    {"timestamp": 1.01, "info": "Trade Received", "price": 10},
    {"timestamp": 1, "info": "Order Data Received", "price": 10}
]

my_data.sort(key=lambda x: x["timestamp"])

###############################################################
# Can we update class fields like this, what will be printed? #
###############################################################
class A(object):
    a = 10
    b = 20


a = dict(A.__dict__)
a.update({"b": 30})
print(A.__dict__)
print(a)

# yes we can!