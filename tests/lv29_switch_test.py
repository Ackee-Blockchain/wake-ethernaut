from wake.testing import *
from tests.ethernaut_deployer import EthernautDeployer
from pytypes.contracts.lv29_switch import Switch
# TODO You can import your our own smart contract(s) here.

@default_chain.connect()
def test_lv29():
    ethernaut = EthernautDeployer(default_chain)
    contract = ethernaut.deploy_lv29()
    exploit_lv29(contract)
    ethernaut.check_lv29(contract)

def exploit_lv29(contract: Switch):
    # TODO Flip the switch. Can't be that hard, right?
    # TODO You can import your our own smart contract(s) here.
    # TODO Code here ...
    pass
