"""
Task 2.3: Handle Errors in API Requests

Goal: Learn to handle common API errors including 404s, timeouts, and invalid JSON.

Exercises:
- Handle 404 errors
- Handle timeout errors
- Handle invalid JSON responses
"""

import httpx

# Exercise 3.1: Handle 404 errors
url = "https://jsonplaceholder.typicode.com/posts/9999"
try:
    response = httpx.get(url)
    response.raise_for_status()
    print(response.json())
except httpx.HTTPStatusError as e:
    if e.response.status_code == 404:
        print("404 Error: Post not found")

# Exercise 3.2: Handle timeout errors
url = "https://jsonplaceholder.typicode.com/posts"
try:
    response = httpx.get(url, timeout=0.001)
    print(response.json())
except httpx.TimeoutException:
    print("Timeout Error: Request timed out")

# Exercise 3.3: Handle invalid JSON responses
url = "https://jsonplaceholder.typicode.com/posts"
try:
    response = httpx.get(url)
    data = response.json()
    print(data)
except ValueError:
    print("Invalid JSON Error: Could not parse JSON")
