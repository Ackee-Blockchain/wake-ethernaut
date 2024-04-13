// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "../lv26_double_entry_point.sol";

contract Dbot is IDetectionBot {

    address cv;

    constructor(address cv_addr) {
        cv = cv_addr;
    } 

    function handleTransaction(address user, bytes calldata) external override {
       
        // bytes4 selecter_handleTransaction;
        // address user1;
        // uint256 msgData_offset;
        // uint256 msgData_length;

        // bytes4 selector_delegateTransfer;
        
        // address to;
        // uint256 value;
        address origSender;

        assembly {
            // selecter_handleTransaction := calldataload(0x00)
            // user1 := calldataload(0x04)// + 0x20
            // msgData_offset := calldataload(0x24) //+0x20
            // msgData_length := calldataload(0x44) //+0x20
            // selector_delegateTransfer := calldataload(0x64)// +4
            // to := calldataload(0x68) // +0x20
            // value := calldataload(0x88)  // +0x20
            origSender := calldataload(0xa8) 
        }

        if(origSender == cv){
            // require(user1 == user, "unexpected data, user address difference.");
            // require(selecter_handleTransaction == bytes4(keccak256(bytes("handleTransaction(address,bytes)"))), "unexpected data, selecter handleTransaction difference.");
            // require(selector_delegateTransfer == bytes4(keccak256(bytes("delegateTransfer(address,uint256,address)"))), "unexpected data, selector delegateTransfer difference.");

            Forta(msg.sender).raiseAlert(user);
        }
    }
}
