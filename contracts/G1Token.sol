// SPDX-License-Identifier: CC0-1.0
pragma solidity ^0.8.20;

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";

contract G1Token is ERC20 {
 // SHA256 hash of the official whitepaper (v4 G1)
 string public constant WHITEPAPER_SHA256 = "33da6b9fdc1609d74bd39af741efe4f5ea57c04e5e24b4c129ee206b5902678c";

 // Maximum total supply of G1 tokens
 uint256 public constant MAX_SUPPLY = 1_000_000_000 * 10 ** 18;

 // Total amount mined so far
 uint256 public minedSupply;

 // Reward per successful mining attempt (default: 1 G1)
 uint256 public reward = 1 * 10 ** 18;

 // Difficulty threshold: lower = harder to mine
 uint256 public difficulty = 2 ** 240;

 // Nonce tracking per address
 mapping(address => uint256) public nonces;

 // Events
 event WhitepaperHash(string hash);
 event Mined(address indexed miner, uint256 amount);

 constructor() ERC20("Genius One", "G1") {
 emit WhitepaperHash(WHITEPAPER_SHA256);
 }

 function mine(uint256 nonce) public {
 require(minedSupply + reward <= MAX_SUPPLY, "Max supply reached");

 // Simulated PoW: hash(sender + nonce) must be below difficulty
 bytes32 hash = keccak256(abi.encodePacked(msg.sender, nonce));
 require(uint256(hash) < difficulty, "Invalid nonce");

 _mint(msg.sender, reward);
 minedSupply += reward;
 nonces[msg.sender]++;
 emit Mined(msg.sender, reward);
 }
}
