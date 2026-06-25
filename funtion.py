# # ------- syntax for funtion --------------
# def mycraft():
#     print('suck game!')

# # ------- Arguments in funtion --------------
# mycraft()

# def mycraft(number):
#     print(number*2)

# mycraft(5)

# # ------- Multiple Arguments in funtion --------------
# def mycraft(number,power):
#     print(number**power)

# mycraft(5,3)

# # ------- Arbritary Arguments in funtion --------------
# def number_args(*number):
#     print(number[4]*number[0])

# number_args(5,6,1,2,8)

# # ------- Arbritary Arguments in funtion with variable --------------
# arg_tuple = (5,6,1,2,8)
# def number_args(*number):
#     print(number[2]*number[0])
# # when you use variable in funtion like this
# # your have to put your need in it.
# number_args(*arg_tuple)


# # ------- Keyword Arguments in funtion --------------
# def mycraft(number,power):
#     print(number**power)

# mycraft(power = 5, number = 3)

# # ------- Arbritary Keyword Arguments in funtion --------------
def number_kwarg(**number):
    print('My number is :' + number['integer'] + ' My other number :' + number ['integers2']
    + ' My other number :' + number ['integers3']
    )
number_kwarg(integer= '500', integers2 = '354',integers = '3532')

