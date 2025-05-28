from wake.testing import *
from tests.ethernaut_deployer import EthernautDeployer
from pytypes.contracts.lv32_impersonator import Impersonator, ECLocker
# TODO You can import your our own smart contract(s) here.

@default_chain.connect()
def test_lv32():
    ethernaut = EthernautDeployer(default_chain)
    contract = ethernaut.deploy_lv32()
    exploit_lv32(contract)
    ethernaut.check_lv32(contract)

def exploit_lv32(contract: Impersonator):
    # TODO ?
    # TODO You can import your our own smart contract(s) here.
    # TODO Code here ...
    pass