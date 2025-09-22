
fruit = [ 'apple','pear','banana','orange' ]

while fruit :
	print( fruit.pop() )
	if not fruit:
		print("The list is now empty")
		break
    
# Add an else clause with a message that the list is now empty