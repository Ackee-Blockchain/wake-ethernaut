// SPDX-License-Identifier: MIT
pragma solidity ^0.8.2;

contract UnderflowCalculator {
    function calculateTheZeroIndex() pure public returns(uint256 index){
        index = (2 ** 256 - 1) - uint256(keccak256(abi.encode(1))) + 1; 
    }
    function calculateMyAddressInBytes() view public returns(bytes32) {
        return bytes32(uint256(uint160(msg.sender)));
    }
}