from wake.testing import *
from tests.ethernaut_deployer import EthernautDeployer
from pytypes.contracts.lv00_hello import Tutorial


@default_chain.connect()
def test_level_00():
    ethernaut = EthernautDeployer(default_chain)
    contract = ethernaut.deploy_lv00()
    exploit_level_00(contract)
    ethernaut.check_lv00(contract)

def exploit_level_00(contract: Tutorial):
    # TODO Run this test to know, what to do next.
    print(contract.info())
    # TODO Code here ...
    pass
