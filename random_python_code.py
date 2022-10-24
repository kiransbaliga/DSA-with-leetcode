# Python program to swap two variables

x = 5
y = 10

# To take inputs from the user
#x = input('Enter value of x: ')
#y = input('Enter value of y: ')

# create a temporary variable and swap the values
temp = x
x = y
y = temp

print('The value of x after swapping: {}'.format(x))
print('The value of y after swapping: {}'.format(y))


# New temporary code
def fact_rec(n):
	if n < 0:
		return
	elif n <= 1:
		return 1
	else:
		return n*fact_rec(n-1)

answer = fact_rec(4)
if answer == None: 
	print("Cannot calculate factorial of a negative value")
else:
	print(answer)  # 24 = 4x3x2x1 = 4! 
