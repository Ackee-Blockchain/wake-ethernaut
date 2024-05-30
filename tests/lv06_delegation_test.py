from wake.testing import *
from tests.ethernaut_deployer import EthernautDeployer
from pytypes.contracts.lv06_delegation import Delegate, Delegation
# TODO You can import your our own smart contract(s) here.

@default_chain.connect()
def test_lv06():
    ethernaut = EthernautDeployer(default_chain)
    contract = ethernaut.deploy_lv06()
    exploit_lv06(contract)
    ethernaut.check_lv06(contract)

def exploit_lv06(contract: Delegation):
    # TODO Claim ownership of the contract.
    # TODO You can deploy your own smart contract(s) here.
    # TODO Code here ...
    pass