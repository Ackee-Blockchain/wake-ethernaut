// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract ForceTransfer {
  address public owner;

  constructor() {
    owner = msg.sender;
  }

  modifier onlyOwner {
    require(msg.sender == owner,"caller is not the owner");
    _;
  }

  function push(address payable beneficiary) onlyOwner external payable {
    selfdestruct(beneficiary);
  }
}

contract FasterForceTransfer {
    constructor(address payable beneficiary) payable {
        selfdestruct(beneficiary);
    }
}