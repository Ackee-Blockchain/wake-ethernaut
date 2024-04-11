from wake.testing import *
from tests.ethernaut_deployer import EthernautDeployer
from pytypes.contracts.lv22_dex import Dex
# TODO You can import your our own smart contract(s) here.

@default_chain.connect()
def test_lv22():
    ethernaut = EthernautDeployer(default_chain)
    contract = ethernaut.deploy_lv22()
    exploit_lv22(contract)
    ethernaut.check_lv22(contract)

def exploit_lv22(contract: Dex):
    # TODO ?
    # TODO You can import your our own smart contract(s) here.
    # TODO Code here ...
    pass
