from wake.testing import *
from tests.ethernaut_deployer import EthernautDeployer
from pytypes.contracts.lv27_good_samaritan import GoodSamaritan
# TODO You can import your our own smart contract(s) here.

@default_chain.connect()
def test_lv27():
    ethernaut = EthernautDeployer(default_chain)
    contract = ethernaut.deploy_lv27()
    exploit_lv27(contract)
    ethernaut.check_lv27(contract)

def exploit_lv27(contract: GoodSamaritan):
    # TODO Drain all the funds of Good Samaritan.
    # TODO You can import your our own smart contract(s) here.
    # TODO Code here ...
    pass
