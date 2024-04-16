// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract ForceTransfer {
    constructor(address payable beneficiary) payable {
        selfdestruct(beneficiary);
    }
}
