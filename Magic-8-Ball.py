#Magic 8-Ball

"""Allow the user to enter their question
Display an in progress message
Create 20 responses, and show a random response
Allow the user to ask another question or quit
Bonus Using whatever module you like, add a gui. Your gui must have:
A box for users to enter the question
At least 4 buttons: Ask , clear(the text box), play again and quit(this must close the window)"""

print ("Welcome to Magic 8-Ball")
print("")
quit = ("yes")
while quit == ("yes"):
	print ("Ask a question!")
	question = input()
	print ("")

	import random
	move = ["Reply hazy try again" , "yes" , "no ", "Outlook not so good", "Without a doubt", "Don't count on it", "It is decidedly so" , "My sources say no" , "As I see it yes" , "Concentrate and ask again" , "Outlook good" , "It is certain" , "Ask again later" , "Yes definitely" , "You may rely on it" , "Most likely" , "Signs point to yes" , "Better not tell you now" , "Cannot predict now" , "Very doubtful",]

	reply = random.choice(move)		
	print (("Magic 8-Ball says: ") + (reply) + ("!"))
	print ("")
	print ("Do you have another question?")
	print ("yes or no")
	quit = input()
	yes = "yes"
