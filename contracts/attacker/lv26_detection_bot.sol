// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "../lv26_double_entry_point.sol";

contract DetectionBot is IDetectionBot {
    address cv;
    constructor(address cv_addr) {
        cv = cv_addr;
    } 

    function handleTransaction(address user, bytes calldata) external override {
        address origSender;
        assembly {
            origSender := calldataload(0xa8) 
        }
        if(origSender == cv){
            Forta(msg.sender).raiseAlert(user);
        }
    }
}
