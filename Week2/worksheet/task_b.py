#task_b

#Get the title
title = input()

#turn to lowercase
lowercase_title = title.lower()

word_list = lowercase_title.split()

slug_list = []
#exclude a and the
for word in word_list:
    if word not in ["a","the"]:
        slug_list.append(word)

#Connect the words
connected_slug = "-".join(slug_list)

#Restrict to 25 characters
slug = connected_slug[:25]

print(f"Slug = {slug}")