print("*******************************")
print("Counted Loops: For")

print("0")
print("1")
print("2")
print("3")

#When we think of a for loop, I want you to think about
# Count: The variable that holds the current count
# Check: The check that is done each time the loop runs
# Change: The change applied to the count each time the loop runs

#Challenge with python is the check is assumed for you. Meaning <initial value> is less than your <check value>

#for <count var> in range(<initial value>, <check value>, <change>)
print("********************")
#i = 0, 0 < 4, True RUN LOOP
#i = 1, 1 < 4, True RUN LOOP
#i = 2, 2 < 4, True RUN LOOP
#i = 3, 3 < 4, True RUN LOOP
#i = 4, 4 < 4, False EXIT AND CONTINUE
for i in range(0,4,1):
	print(i)

print("***********************")
#Change the loop parameters so it prints -44 to 136

for i in range(-44,136,1):

#% gives remainder of division
#for example, 5%2 is 1, because 5/2 has a remainder of 1
	if (i % 2==0):
		print(str(i)+" is even")
	else: 
		print(str(i)+" is odd")