# Step 1: Prompt the user for their name, age, and favorite color.

# Step 2: Open a file called 'user_info.txt'

# Step 3: Write each piece of information to the file, each on a new line.

# hint: think about what mode to open in!
# hint: remember to add \n for new lines when writing to files
# hint: if you want multiple people to add info without overwriting, consider append mode 'a'

# you could extend this by using a loop to allow multiple people to enter their info in a row

# 补全代码：添加循环以允许多人输入
while True:
    name = input("Enter your name: ")
    age = input("Enter your age: ")
    color = input("Enter your favorite color: ")
    
    with open('user_info.txt', 'a') as file:
        file.write(name + ',')
        file.write(age + ',')
        file.write(color + '\n')
    
    more = input("Do you want to add another person? (yes/no): ")
    if more.lower() != 'yes':
        break