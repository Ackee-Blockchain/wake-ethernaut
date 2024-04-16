// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract Deployer {
    function deployCode(bytes memory bytecode) public returns (address instance) {
      // create(v, p, n)
      // create new contract with code mem[p...(p+n)) and send v wei and return the new addresss
      assembly {
        instance := create(0, add(bytecode,0x20), mload(bytecode))
      }
    }
}