// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract BrokenContract {
    receive() payable external{
        assembly { invalid() } 
    }
    
}