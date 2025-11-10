"""
Task 2.2: Send Data Using POST Requests

Goal: Learn to send data to an API using POST requests.

Exercises:
- Create a new post
- Add a new comment to a post
- Create a new user
"""

import httpx

# Exercise 2.1: Create a new post
url = "https://jsonplaceholder.typicode.com/posts"
data = {"title": "New Post", "body": "This is a new post", "userId": 1}
response = httpx.post(url, json=data)
print(response.json())

# Exercise 2.2: Add a new comment to a post
url = "https://jsonplaceholder.typicode.com/comments"
data = {"postId": 1, "name": "New Comment", "email": "user@example.com", "body": "This is a new comment"}
response = httpx.post(url, json=data)
print(response.json())

# Exercise 2.3: Create a new user
url = "https://jsonplaceholder.typicode.com/users"
data = {"name": "New User", "username": "newuser", "email": "newuser@example.com"}
response = httpx.post(url, json=data)
print(response.json())
