// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "wake/console.sol";

contract AttackMagicNum {
  function whatIsTheMeaningOfLife() pure public returns(uint256) {
    return 42;
  }
  fallback(bytes calldata) external payable returns(bytes memory) {
    return abi.encode(42);
  }
}

contract AttackMagicNumDeployer {
    function deployFromBytecode(bytes memory bytecode) public returns (address instance) {
      // create(v, p, n)
      // create new contract with code mem[p...(p+n)) and send v wei and return the new addresss
      assembly {
        instance := create(0, add(bytecode,0x20), mload(bytecode))
      }
    }
}