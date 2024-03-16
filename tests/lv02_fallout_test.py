from wake.testing import *
from tests.ethernaut_deployer import EthernautDeployer
from pytypes.contracts.lv02_fallout import Fallout


@default_chain.connect()
def test_lv02():
    ethernaut = EthernautDeployer(default_chain)
    contract = ethernaut.deploy_lv02()
    exploit_lv02(contract)
    ethernaut.check_lv02(contract)

def exploit_lv02(contract: Fallout):
    # Attack vector: unsecured construction method
    contract.Fal1out()
