// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import '../lib/openzeppelin/release-v4.0/contracts/token/ERC20/ERC20.sol';

contract DefaultERC20 is ERC20 {

  uint256 public INITIAL_SUPPLY;

  constructor(string memory name, string memory symbol) 
  ERC20(name, symbol) {
    INITIAL_SUPPLY = 100 ether;
    // _totalSupply = INITIAL_SUPPLY;
    // _balances[player] = INITIAL_SUPPLY;
    _mint(msg.sender, INITIAL_SUPPLY);
    emit Transfer(address(0), msg.sender, INITIAL_SUPPLY);
  }
} 