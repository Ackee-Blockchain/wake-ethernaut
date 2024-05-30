from wake.testing import *
from tests.ethernaut_deployer import EthernautDeployer
from pytypes.contracts.lv21_shop import Shop
# TODO You can import your our own smart contract(s) here.

@default_chain.connect()
def test_lv21():
    ethernaut = EthernautDeployer(default_chain)
    contract = ethernaut.deploy_lv21()
    exploit_lv21(contract)
    ethernaut.check_lv21(contract)

def exploit_lv21(contract: Shop):
    # TODO Try some shoplifting.
    # TODO You can import your our own smart contract(s) here.
    # TODO Code here ...
    pass
