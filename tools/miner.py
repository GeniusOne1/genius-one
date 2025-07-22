import hashlib
import time
import json
from datetime import datetime

# Load configuration
with open("tools/miner_config.json", "r") as f:
config = json.load(f)

CHAIN_FILE = "tools/chain.json"

# Load blockchain
try:
with open(CHAIN_FILE, "r") as f:
chain = json.load(f)
except FileNotFoundError:
chain = []

# Get last block data
last_block_time = datetime.strptime(chain[-1]["timestamp"], "%Y-%m-%d %H:%M:%S") if chain else datetime.utcnow()
last_block_hash = chain[-1]["hash"] if chain else "0" * 64
block_height = len(chain)

def calculate_reward(height, base_reward, halving_interval):
halvings = height // halving_interval
reward = base_reward // (2 ** halvings)
return max(reward, 0)

def is_valid_hash(h, prefix):
return h.startswith(prefix)

while True:
now = datetime.utcnow()
time_diff = (now - last_block_time).total_seconds()
if time_diff < config["minimum_block_time_seconds"]:
time.sleep(1)
continue

reward = calculate_reward(
block_height,
config["initial_block_reward"],
config["halving_interval_blocks"]
)

if reward == 0 or sum(b["reward"] for b in chain) >= config["total_supply"]:
print("Mining complete. Total supply reached.")
break

nonce = 0
while True:
data = f"{last_block_hash}{block_height}{now}{nonce}".encode()
h = hashlib.sha256(data).hexdigest()
if is_valid_hash(h, config["initial_difficulty_prefix"]):
break
nonce += 1

block = {
"height": block_height,
"timestamp": now.strftime("%Y-%m-%d %H:%M:%S"),
"previous_hash": last_block_hash,
"hash": h,
"nonce": nonce,
"reward": reward
}

chain.append(block)
with open(CHAIN_FILE, "w") as f:
json.dump(chain, f, indent=4)

print(f"Mined block #{block_height} | Reward: {reward} G1 | Hash: {h}")
block_height += 1
last_block_time = now
last_block_hash = h
break # Run once
