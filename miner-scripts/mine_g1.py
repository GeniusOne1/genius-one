import hashlib

target = "00000fffffffffffffffffffffffffffffffffffffffffffffffffffffffffff"

def mine(address):
 nonce = 0
 while True:
 data = f"{address}{nonce}".encode()
 hash_result = hashlib.sha256(data).hexdigest()
 if hash_result < target:
 print(f" Success! Nonce: {nonce} | Hash: {hash_result}")
 break
 nonce += 1

wallet = input("Enter your wallet address: ")
mine(wallet)
