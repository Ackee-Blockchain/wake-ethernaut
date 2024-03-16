from wake.testing import *
from tests.ethernaut_deployer import EthernautDeployer
from pytypes.contracts.lv07_force import Force
# TODO You can import your our own smart contract(s) here.

@default_chain.connect()
def test_level_07():
    ethernaut = EthernautDeployer(default_chain)
    contract = ethernaut.deploy_lv07()
    exploit_level_07(contract)
    ethernaut.check_lv07(contract)

def exploit_level_07(contract: Force):
    # TODO Force this contract to take some Ether.
    # TODO You can import your our own smart contract(s) here.
    # TODO Code here ...
    pass
