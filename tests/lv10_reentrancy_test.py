from wake.testing import *
from tests.ethernaut_deployer import EthernautDeployer
from pytypes.contracts.lv10_reentrancy import Reentrance
# TODO You can import your our own smart contract(s) here.

@default_chain.connect()
def test_lv10():
    ethernaut = EthernautDeployer(default_chain)
    contract = ethernaut.deploy_lv10()
    exploit_lv10(contract)
    ethernaut.check_lv10(contract)

def exploit_lv10(contract: Reentrance):
    # TODO Steal all the funds from the contract.
    # TODO You can import your our own smart contract(s) here.
    # TODO Code here ...
    pass
