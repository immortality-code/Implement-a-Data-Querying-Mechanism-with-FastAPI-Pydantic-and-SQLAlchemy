import requests
import os

BASE_URL = os.getenv("API_BASE_URL", "http://127.0.0.1:8000")

print("\n📘 GET /api/posts?status=draft&include=tags,user")
r = requests.get(f"{BASE_URL}/api/posts", params={"status": "draft", "include": "tags,user"})
print("Status:", r.status_code)
print("Data:", r.json())

print("\n📗 GET /api/posts/1?include=tags,user,comments")
r = requests.get(f"{BASE_URL}/api/posts/1", params={"include": "tags,user,comments"})
print("Status:", r.status_code)
print("Data:", r.json())

print("\n📙 GET /api/users/1?include=posts,comments")
r = requests.get(f"{BASE_URL}/api/users/1", params={"include": "posts,comments"})
print("Status:", r.status_code)
try:
    print("Data:", r.json())
except Exception:
    print("Raw Response:", r.text)
