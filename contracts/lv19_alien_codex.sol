// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;
// wake only supports version ^0.6.2 - this file acts only as interface
// the real instance is deployed from binary and compiled with the solc version 0.5.0

import "./lib/openzeppelin/release-v4.0/contracts/access/Ownable.sol";

contract AlienCodex is Ownable {
    bool public contact;
    bytes32[] public codex;

    modifier contacted() {
        assert(contact);
        _;
    }

    function makeContact() public {
        contact = true;
    }

    function record(bytes32 _content) public contacted {
        codex.push(_content);
    }

    function retract() public contacted {
        // this is ilegal in this version
        // codex.length--;
    }

    function revise(uint256 i, bytes32 _content) public contacted {
        codex[i] = _content;
    }
}