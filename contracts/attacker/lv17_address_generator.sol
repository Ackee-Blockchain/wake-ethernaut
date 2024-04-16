// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

interface IRecovery{
    function destroy(address payable _to) external; 
}

contract AddressGenerator {

  // see: https://ethereum.stackexchange.com/questions/760/how-is-the-address-of-an-ethereum-contract-computed
  function generateAddress(address addressOfCreator) pure public returns(address) {
    return address(uint160(uint256(keccak256(abi.encodePacked(bytes1(0xd6), bytes1(0x94),addressOfCreator, bytes1(0x01))))));
  }

  function destroyContract(address addressToDestroy) public {
    IRecovery(addressToDestroy).destroy(payable(addressToDestroy));
  }
}
