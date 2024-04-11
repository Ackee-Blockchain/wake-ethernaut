// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;


contract CheckSizeContract {
  function checkSize(address solver) view public returns(uint256 size) {
    assembly {
        size := extcodesize(solver)
    }
  }
}