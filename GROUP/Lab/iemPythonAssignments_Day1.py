# Assignment 1
print("Assignment 1")
n=int(input("Enter number: "))
rev=0
while(n>0):
    dig=n%10
    rev=rev*10+dig
    n=n//10
print("Reverse of the number:",rev)

# Assignment 2
print("Assignment 2");
def getLargestPermutationNumber(num):
    res = 0
    for i in range(9, -1, -1):
        n = num
        while(n > 0):
            r = n % 10
            n = n // 10;
            if r == i:
                res = res * 10 + r
    return res;
n=int(input("Enter number: "))
print("Largest Permutation Number = ", getLargestPermutationNumber(n))
 
# Assignment 3
print("Assignment 3"); 
n = int(input('Enter n: '))
count = 0
while n:
    n &= n - 1
    count += 1


print('Number of set bits:', count)

# Assignment 4a
print("Assignment 4a"); 
def pypart2(n): 
	
	# number of spaces 
	k = 2*n - 2

	# outer loop to handle number of rows 
	for i in range(0, n): 
	
		# inner loop to handle number spaces 
		# values changing acc. to requirement 
		for j in range(0, k): 
			print(end=" ") 
	
		# decrementing k after each loop 
		k = k - 2
	
		# inner loop to handle number of columns 
		# values changing acc. to outer loop 
		for j in range(0, i+1): 
		
			# printing stars 
			print("* ", end="") 
	
		# ending line after each row 
		print("\r") 

# Driver Code 
n = 5
pypart2(n) 

# Assignment 4b
print("Assignment 4b"); 
# Function to demonstrate printing pattern triangle 
def triangle(n): 
	
	# number of spaces 
	k = 2*n - 2

	# outer loop to handle number of rows 
	for i in range(0, n): 
	
		# inner loop to handle number spaces 
		# values changing acc. to requirement 
		for j in range(0, k): 
			print(end=" ") 
	
		# decrementing k after each loop 
		k = k - 1
	
		# inner loop to handle number of columns 
		# values changing acc. to outer loop 
		for j in range(0, i+1): 
		
			# printing stars 
			print("* ", end="") 
	
		# ending line after each row 
		print("\r") 

# Driver Code 
n = 5
triangle(n) 

# Assignment 4c
print("Assignment 4c"); 

# Function to demonstrate printing pattern of alphabets 
def alphapat(n): 
	
	# initializing value corresponding to 'A' 
	# ASCII value 
	num = 65

	# outer loop to handle number of rows 
	# 5 in this case 
	for i in range(0, n): 
	
		# inner loop to handle number of columns 
		# values changing acc. to outer loop 
		for j in range(0, i+1): 
		
			# explicitely converting to char 
			ch = chr(num) 
		
			# printing char value 
			print(ch, end=" ") 
	
		# incrementing number 
		num = num + 1
	
		# ending line after each row 
		print("\r") 

# Driver Code 
n = 5
alphapat(n) 

# Assignment 5
print("Assignment 5"); 
#(220, 284) ia a pair of amicable numbers.
#They are amicable because the proper divisors
#of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55
#and 110, of which the sum is 284; and the proper
#divisors of 284 are 1, 2, 4, 71 and 142,
#of which the sum is 220.

x=int(input('Enter number 1: '))
y=int(input('Enter number 2: '))
sum1=0
sum2=0
for i in range(1,x):
    if x%i==0:
        sum1+=i
for j in range(1,y):
    if y%j==0:
        sum2+=j
if(sum1==y and sum2==x):
    print('Amicable!')
else:
    print('Not Amicable!')
