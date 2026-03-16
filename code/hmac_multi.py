import hmac
import hashlib

key = b"secretkey123"
files = ["message1.txt", "message2.txt", "message3.txt"]

for filename in files:
    with open(filename, "rb") as f:
        message = f.read()

    tag = hmac.new(key, message, hashlib.sha256).hexdigest()

    print("File:", filename)
    print("Message:", message.decode())
    print("HMAC Tag:", tag)
    print("-" * 60)
