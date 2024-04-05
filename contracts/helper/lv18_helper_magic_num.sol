// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;


contract HelperMagicNum {
  function checkSize(address solver) view public returns(bool) {
    uint256 size;
    assembly {
        size := extcodesize(solver)
    }
    if (size > 10) return false;
    else return true;

  }
}