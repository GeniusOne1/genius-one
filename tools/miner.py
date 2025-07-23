import hashlib
import time
import json
from datetime import datetime

# Load configuration
with open("tools/miner_config.json", "r") as f:
    config = json.load(f)

CHAIN_FILE = "tools/chain.json"

# Load existing chain or create a new one
try:
    with open(CHAIN_FILE, "r") as f:
        chain = json.load(f)
except FileNotFoundError:
    chain = []

# Get last block info
last_block_time = datetime.strptime(chain[-1]["timestamp"], "%Y-%m-%d %H:%M:%S") if chain else datetime.now()
last_block_hash = chain[-1]["hash"] if chain else "0" * 64
block_number = len(chain) + 1

# Reward calculation with halving
def calculate_reward(height, base_reward, halving_interval):
    halvings = height // halving_interval
    reward = base_reward // (2 ** halvings)
    return max(reward, 0)

# Parameters from config
difficulty_prefix = config["initial_difficulty_prefix"]
base_reward = config["base_reward"]
halving_interval = config["halving_interval"]
total_supply = config["total_supply"]
interval = config["mining_interval_seconds"]

# Mining loop
while True:
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    reward = calculate_reward(block_number, base_reward, halving_interval)
    block = {
        "number": block_number,
        "timestamp": timestamp,
        "previous_hash": last_block_hash,
        "reward": reward,
    }

    nonce = 0
    while True:
        block["nonce"] = nonce
        block_string = json.dumps(block, sort_keys=True).encode()
        block_hash = hashlib.sha256(block_string).hexdigest()
        if block_hash.startswith(difficulty_prefix):
            block["hash"] = block_hash
            break
        nonce += 1

    chain.append(block)

    # Save the updated chain
    with open(CHAIN_FILE, "w") as f:
        json.dump(chain, f, indent=4)

    print(f"Block {block_number} mined with hash: {block['hash']}, reward: {reward}")

    # Update for next block
    last_block_hash = block["hash"]
    block_number += 1

    # Respect mining interval
    time.sleep(interval)
