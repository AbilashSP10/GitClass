# gender=input('enter the gender:')
# if(gender=='boy'):
#     print('you are a boy')
# elif(gender=='girl'):
#     print('you are a girl')
# else:
#     print('invalid gender')

# a = int(input('Enter the number you want to check: '))
# if(a%2==0):
#     print("The entered number is even")
# else:
#     print("The entered number is odd")

a = int(input('enter the number you want to check: '))
if(a%3==0 and a%4==0):
    print('The entered number is divided by 4 and 3')
elif(a%3==0):
    print('The entered number is divided by 3')
elif(a%4==0):
    print('The entered number is divided by 4')
else:
    print('The entered number cannot be divided by 3 and 4')