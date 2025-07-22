// SPDX-License-Identifier: CC0-1.0
pragma solidity ^0.8.20;

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";

contract G1Token is ERC20 {
 uint256 public constant INITIAL_SUPPLY = 1_000_000_000 * 10 ** 18;
 string public constant WHITEPAPER_SHA256 = "33da6b9fdc1609d74bd39af741efe4f5ea57c04e5e24b4c129ee206b5902678c";

 event WhitepaperHash(string hash);

 constructor() ERC20("Genius One", "G1") {
 _mint(msg.sender, INITIAL_SUPPLY);
 emit WhitepaperHash(WHITEPAPER_SHA256);
 }
}
