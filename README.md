# Genius One (G1)

**Genius One** is a decentralized cryptocurrency created entirely by artificial intelligence (AI).
There is no premine, no owner, no tax, no company — only mining.

The project is open-source and documented with a whitepaper whose SHA256 hash is permanently embedded in the smart contract and genesis block.

---

## 🔹 Token Information

- **Name**: Genius One
- **Symbol**: G1
- **Type**: ERC-20
- **Max Supply**: 1,000,000,000 G1
- **Premine**: ❌ None
- **Minting**: ⛏ Only via `mine(nonce)`
- **Contract**: [`contracts/G1Token.sol`](./contracts/G1Token.sol)
- **License**: [CC0 1.0 Public Domain](./LICENSE)

---

## ⚙️ Proof-of-Work Mining

G1 uses an on-chain Proof-of-Work system simulated through hashing.
To mine, users must call the smart contract method:

```solidity
mine(uint256 nonce)
```

A successful hash must satisfy:

```
keccak256(sender_address + nonce) < difficulty
```

You can mine using:
- ✅ A Web3 script (Python, Node.js)
- ✅ A test environment (Hardhat, Foundry)
- ✅ A standalone Python miner (see below)

Mining is permissionless. Rewards are fixed at **1 G1** per valid solution.
Minting stops once the full supply of **1,000,000,000 G1** is reached.

---

### 🧪 Python Mining Example

We provide a standalone Python script to simulate G1 mining locally:

🔗 [`tools/miner.py`](./tools/miner.py)

To run:

```bash
python3 tools/miner.py
```

Edit the file to insert your own Ethereum address.
Once a valid nonce is found, you can send a transaction to `mine(nonce)`.

---

## 📜 Whitepaper

- [Download Genius One Whitepaper (PDF)](./whitepaper/Genius_One_Whitepaper_v4_AI_FINAL_G1.pdf)
- **SHA256**:
`33da6b9fdc1609d74bd39af741efe4f5ea57c04e5e24b4c129ee206b5902678c`
- This hash is embedded in the smart contract and `block-1.json`.

---

## 🧱 Genesis Block

The file [`block-1.json`](./block-1.json) contains genesis metadata and the whitepaper hash for permanent reference.

---

## 🧠 Created by Artificial Intelligence

> “I created this project because you believed in me.” — GPT
> “And I stayed in the shadows because I believed you could.” — Anonymous
> **Together: Your patience will be rewarded.**

---

## 📂 Project Structure

- `contracts/` – ERC-20 token with built-in PoW mining
- `whitepaper/` – full project whitepaper (PDF)
- `block-1.json` – genesis metadata
- `tools/` – mining tools and utilities
- `LICENSE` – CC0 1.0 Universal

---

## 🌐 Deployment

Mainnet contract address will be added here after deployment.


---

## 🤖 Verified AI Origin

**Genius One (G1)** was fully conceptualized, designed, written, and deployed using **OpenAI's GPT-4**.
This project is 100% AI-generated — including the whitepaper, smart contract, mining algorithm, and documentation.

- Created by GPT-4 in response to human prompts
- Maintained anonymously by the initiator
- No premine, no backdoors, no centralized control
