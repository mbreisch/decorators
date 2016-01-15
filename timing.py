import time


def timing_function(some_function):

    def wrapper():
        t1 = time.time()
        some_function()
        t2 = time.time()
        return "Time it took to run the function: {}\n".format(t2 - t1)
    return wrapper

@timing_function
def my_function():
    num_list=[]
    for num in range(0,10000):
        num_list.append(num)
    print "Sum of all numbers is {}".format(sum(num_list))

print my_function()

