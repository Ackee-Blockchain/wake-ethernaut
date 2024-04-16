// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

interface HasEnter {
  function enter(bytes8 _gateKey) external returns (bool);
}

contract GatekeeperOneHelper {

  function getGateThreeKey() public view returns (bytes memory result) {

    // uint32(key) must be equal to uint16(address)
    // uint64(key) must be not equal to uint32(key)
    uint64 key_uint = type(uint64).max - type(uint32).max + uint16(uint160(tx.origin));
    result = abi.encodePacked(key_uint);
  }

  function testGateThree(bytes8 _gateKey) public view {
      require(uint32(uint64(_gateKey)) == uint16(uint64(_gateKey)), "GatekeeperOne: invalid gateThree part one");
      require(uint32(uint64(_gateKey)) != uint64(_gateKey), "GatekeeperOne: invalid gateThree part two");
      require(uint32(uint64(_gateKey)) == uint16(uint160(tx.origin)), "GatekeeperOne: invalid gateThree part three");
  }

  function getGasReminder() public view returns (uint256) {
    return gasleft() % 8191;
  }

  function callEnterOn(address target, bytes8 _gateKey) public returns (bool result) {
    HasEnter gatekeeper = HasEnter(target);
    result = gatekeeper.enter(_gateKey);
  }
}
