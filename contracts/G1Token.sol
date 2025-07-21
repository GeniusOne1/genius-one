// SPDX-License-Identifier: CC0-1.0
pragma solidity ^0.8.20;

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";

contract G1Token is ERC20 {
 uint256 public constant INITIAL_SUPPLY = 100_000_000 * 10 ** 18;

 constructor() ERC20("Genius One", "G1") {
 _mint(msg.sender, INITIAL_SUPPLY);
 }
}
