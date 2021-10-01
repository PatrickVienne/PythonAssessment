##################
# print 20 stars #
##################


###############################################################
# write a lotto generator which take 6 from the range 1 to 49 #
###############################################################


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
