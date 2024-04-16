// SPDX-License-Identifier: MIT
pragma solidity ^0.8.2;

contract Destructor {
    function killed() external {
        selfdestruct(payable(msg.sender));
    }
}
