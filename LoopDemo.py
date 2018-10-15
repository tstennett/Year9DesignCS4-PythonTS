#A loop is a programming structure that can repeat a section of code
#A loop can run through the same code exactly over and over or with some thought, it can generate a pattern

#There are two broad catagories of loops
# Conditional loops(while): these loop as long as a condition is true

# Counted loops(for) : these loop using a counter to keep track of how many times the loop has run

#You can use any loop in any situation, but usually, from a design perspective, 
#there is a better loop in terms of coding

#If you know in advance how many times a loop should run, a COUNTED LOOP is usually the better choice

#If you don't know how many times a loop should run, a CONDITIONAL LOOP is usually the better choice

print("*********************************************************************")
#Taking Inputs
word = ""
#A while loop evaluates a condition when it is first reached
#If the condition is true then it enters the loop block

#for word.isalpha() == False, you can short hand it to be: not(word.isalpha())
while (len(word) < 6 or word.isalpha() == False):
	#loop block
	word = input("Please input a word larger than 5 letters: ")
	#print(word.isalpha())
	if(word.isalpha() == False)
		print("Come on bruh, you gotta use letters from the alphabet ONLY!")
	if(len(word) < 6):
		print("Come on bruh, I said more than 5 letters!")


print(word+" is seriously long!")
	#When we reach the bottom of the loop block we check the condition again. If it is true, we go back
	#and run it again








