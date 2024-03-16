from wake.testing import *
from tests.ethernaut_deployer import EthernautDeployer
from pytypes.contracts.lv00_hello import Tutorial
# TODO You can import your our own smart contract(s) here.

@default_chain.connect()
def _level_00():
    ethernaut = EthernautDeployer(default_chain)
    contract = ethernaut.deploy_lv00()
    exploit_level_00(contract)
    ethernaut.check_lv00(contract)

def exploit_level_00(contract: Tutorial):
    # TODO ?
    # TODO You can import your our own smart contract(s) here.
    # TODO Code here ...
    pass
