// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import '../lv11_elevator.sol';

contract SmartBuilding is Building {
  uint public callCounter;

  function isLastFloor(uint /*floor*/) external returns (bool) {
    return (callCounter++ % 2 == 1);
  }

  function goToWith(uint floor, address elevatorAddr) external {
    Elevator elevator = Elevator(elevatorAddr);
    elevator.goTo(floor);
  }
}
