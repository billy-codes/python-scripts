# The following script allows to find the 
# ceiling and floor values of a number
# without using ceil() or floor() functions

x = 10
y = 4

ceil_value = -(-x // y)
floor_value = x // y


print("Ceil Value: {}".format(ceil_value))
print("Floor Value: {}".format(floor_value))