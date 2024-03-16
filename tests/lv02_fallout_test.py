from wake.testing import *
from tests.ethernaut_deployer import EthernautDeployer
from pytypes.contracts.lv02_fallout import Fallout


@default_chain.connect()
def test_level_02():
    ethernaut = EthernautDeployer(default_chain)
    contract = ethernaut.deploy_lv02()
    exploit_level_02(contract)
    ethernaut.check_lv02(contract)

def exploit_level_02(contract: Fallout):
    # TODO Claim ownership of the contract.
    # TODO Code here ...
    pass
