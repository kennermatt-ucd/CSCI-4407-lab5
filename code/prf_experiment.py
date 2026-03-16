import hashlib

# PRF-based authentication function
# Implements F_K(M) = H(K || M) using SHA-256
# The key K and message M are concatenated before hashing,
# so the output is uniquely determined by both inputs.

def prf_authenticate(key: bytes, message: bytes) -> str:
    """
    Compute a PRF-based authentication tag for a message.

    F_K(M) = SHA-256(K || M)

    Parameters:
        key     -- secret key as bytes
        message -- input message as bytes

    Returns:
        Authentication tag as a hex string
    """
    combined = key + message
    digest = hashlib.sha256(combined).hexdigest()
    return digest


def run_experiment(secret_key: bytes, messages: list):
    print(f"Secret Key: {secret_key.decode()}")
    print("=" * 60)
    for msg in messages:
        tag = prf_authenticate(secret_key, msg.encode())
        print(f"Message : {msg}")
        print(f"Auth Tag: {tag}")
        print("-" * 60)
    print()


# --- Experiment 1: Tags for three different messages ---
print("=== Experiment 1: Three Messages, Same Key ===")
key1 = b"myGroupKey789"
messages = [
    "Transfer 100 dollars to Bob",
    "Transfer 500 dollars to Alice",
    "Authorize access to server room",
]
run_experiment(key1, messages)

# --- Experiment 2: Modify one message, observe tag change ---
print("=== Experiment 2: Modified Message ===")
modified_messages = [
    "Transfer 100 dollars to Bob",       # original
    "Transfer 999 dollars to Bob",       # modified amount
    "Authorize access to server room",
]
run_experiment(key1, modified_messages)

# --- Experiment 3: Change the secret key, same messages ---
print("=== Experiment 3: Different Key, Same Messages ===")
key2 = b"differentKey321"
run_experiment(key2, messages)
