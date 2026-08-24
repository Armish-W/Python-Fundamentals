# # type casting
# x= float(2)
# y=float(30.0)
# z=float("20")
# print(x)
# print(y)
# print(z)

# # sum two numbers using typecast
# num_int= 123
# num_str="456"
# print("Data type of num_int:",type(num_int))
# print("Data type of num_str before Type Casting:",type(num_str))
# num_str= int(num_str)
# print("Data type of num_str after Type Casting:",type(num_str))
# num_sum= num_int + num_str
# print ("Sum of num_int and num_str:",num_sum)
# print ("Data type of the sum:", type(num_sum))

# # operators precedence
# print(True or False and False or True)
# print(True or False) and (False or True)

# print(max(7,9))
# print(max(2+25,9))

# #if-else
# name='Alice'
# if name=="Alice":
#     print('Hi,Alice.')

# name= input("Enter your name:")
# print(f"Hi, Lovely {name} <3 ")

# # if-else
# name='Bob'
# if name=="Alice":
#     print('Hi, Alice')
# else:
#     print('Hi, Stranger, 67')

# # if-elif condition

# # while loop

# #functions
# def hello(name):
#     print('Hello{}'.format(name))
#     print(f'Hello{name}')
# hello('Alice')
# hello('Bob')

# import random 
# def getAnswer(answerNumber):
#     if answerNumber==1:
#         return 'It is certain'
#     elif answerNumber==2:
#         return 'It is ok'
#     elif answerNumber==3:
#         return 'It is okayy!!'
#     elif answerNumber==4:
#         return 'It is fantastic'
#     elif answerNumber==5:
#         return 'It is not ok'

# r= random.randint(1,5)
# fortune= getAnswer(r)
# print(fortune)

# #built-in function
# # abs integer number
# num=-5
# print(f'Absolute number of -5 is {abs(num)}')

# # max function
# number=[3,2,4,6,7,100]
# largest_number=max(number)
# print('Largest number is', largest_number)

# # sep
# print('Hands','toe','lab', sep='\n')

# #sum function'
# my_list= [1,2,3,4,5]
# print('The sum of my_list is', sum(my_list))

# power of 3
def ispowerofthree(n:int) -> bool:
    if n<=0:
        return False
    while n%3==0:
        n//3==0
    return n==1
print(ispowerofthree(9))