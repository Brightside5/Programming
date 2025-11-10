"""
Task 2.1: Fetch and Display Posts Using GET Request

Goal: Learn to make GET requests to an API and display the results.

Exercises:
- Fetch and display all posts (first 5)
- Fetch a single post by ID
- Fetch users and display their names
"""

import httpx

# Exercise 1.1: Fetch and display all posts (first 5)
url = "https://jsonplaceholder.typicode.com/posts"
response = httpx.get(url)
posts = response.json()
for post in posts[:5]:
    print(post)

# Exercise 1.2: Fetch a single post by ID
url = "https://jsonplaceholder.typicode.com/posts/1"
response = httpx.get(url)
post = response.json()
print(f"Post ID: {post['id']}\nTitle: {post['title']}\nBody: {post['body']}\n")

# Exercise 1.3: Fetch users and display their names
url = "https://jsonplaceholder.typicode.com/users"
response = httpx.get(url)
users = response.json()
for user in users:
    print(user['name'])
