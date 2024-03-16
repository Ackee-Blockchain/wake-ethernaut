from wake.testing import *
from tests.ethernaut_deployer import EthernautDeployer
from pytypes.contracts.lv01_fallback import Fallback


@default_chain.connect()
def test_level_01():
    ethernaut = EthernautDeployer(default_chain)
    contract = ethernaut.deploy_lv01()
    exploit_level_01(contract)
    ethernaut.check_lv01(contract)

def exploit_level_01(contract: Fallback):
    # TODO Claim ownership of the contract and reduce its balance to 0.
    # TODO Code here ...
    pass
