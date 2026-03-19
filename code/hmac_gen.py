import hmac
import hashlib
import sys
import os

key = b"secretkey123"

script_dir = os.path.dirname(os.path.abspath(__file__))
messages_dir = os.path.join(script_dir, "..", "messages")

filename = input("Enter message filename (e.g. message1.txt): ").strip()
filepath = os.path.join(messages_dir, filename)

with open(filepath, "rb") as f:
    message = f.read()

tag = hmac.new(key, message, hashlib.sha256).hexdigest()

print("Message:", message.decode())
print("HMAC Tag:", tag)
