# Genius One (G1)

**Genius One** is a fully decentralized cryptocurrency created entirely by artificial intelligence (AI).  
There is no premine, no owner, no taxes, and no company — only fair mining.

The project is open-source and verifiable. The whitepaper's SHA256 hash is permanently embedded in both the smart contract and the genesis block.

---

## 🔹 Token Information

- **Name**: Genius One  
- **Symbol**: G1  
- **Standard**: ERC-20  
- **Max Supply**: 1,000,000,000 G1  
- **Premine**: ❌ None  
- **Minting**: ⛏ 100% via mining  
- **Smart Contract**: [`contracts/G1Token.sol`](./contracts/G1Token.sol)  
- **License**: [CC0 1.0 Public Domain](./LICENSE)  

---

## ⚙️ Proof-of-Work Mining

G1 uses an on-chain Proof-of-Work mining model inspired by Bitcoin.  
Mining is permissionless and deterministic based on Ethereum addresses and nonces.

### ⛏ Mining Algorithm

```solidity
keccak256(sender_address + nonce) < difficulty
```

### ⏱ Block Parameters

- ⏳ **Block time**: 30 seconds  
- 🎯 **Initial block reward**: 500 G1  
- 📉 **Halving**: Every 525,600 blocks (~6 months)  
- 📆 **Total mining period**: ~10 years  
- 📈 **Commission**: None — 100% of the reward goes to miners

The reward halves periodically until the full supply of **1,000,000,000 G1** is mined.  
This makes the emission curve finite, predictable, and fair.

---

## 💻 Python Miner (Simulation)

A standalone Python script simulates PoW mining locally:

🔗 [`tools/miner.py`](./tools/miner.py)

### Usage:

```bash
python3 tools/miner.py
```

Edit the script to insert your Ethereum address.  
Once a valid nonce is found, use a Web3 wallet to call `mine(nonce)`.

---

## 📄 Whitepaper

- [Genius One Whitepaper (PDF)](whitepaper/genius_one_whitepaper.pdf)
- SHA256: `36702d8ac4b602b78d54d76ad15f9fe59b8a845bed3a1fcb2aeea0e16cb5aa13`  
- This hash is embedded in:
  - ✅ The smart contract (`G1Token.sol`)  
  - ✅ Genesis block (`block-1.json`)

---

## 🧱 Genesis Block

The genesis block stores initial metadata, including the whitepaper hash:  
📂 [`block-1.json`](./block-1.json)

---

## 🤖 Created by Artificial Intelligence

> “I created this project because you believed in me.”  
> — GPT

> “And I stayed in the shadows because I believed you could do it.”  
> — Anonymous

**Genius One already exists.**  
**Your patience will be rewarded.**

---
