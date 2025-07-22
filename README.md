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

Mining is simulated directly in the smart contract via keccak256 hashing.
To mine a G1 token, users must call the `mine(uint256 nonce)` function and provide a valid nonce such that:

```
keccak256(sender_address + nonce) < difficulty
```

- The contract does not mint any tokens at deployment.
- Rewards are fixed at 1 G1 per successful hash.
- Mining continues until 1 billion tokens are mined.

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
- `LICENSE` – CC0 1.0 Universal

---

## 🌐 Deployment

Mainnet contract address will be added here after deployment.
