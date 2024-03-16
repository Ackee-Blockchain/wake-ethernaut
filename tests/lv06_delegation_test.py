from wake.testing import *
from tests.ethernaut_deployer import EthernautDeployer
from pytypes.contracts.lv06_delegation import Delegate, Delegation
# TODO You can import your our own smart contract(s) here.

@default_chain.connect()
def test_level_06():
    service = EthernautDeployer(default_chain)
    contract = service.deploy_lv06()
    do_level_06_solution(contract)
    service.check_lv06(contract)

def do_level_06_solution(contract: Delegation):
    # TODO Claim ownership of the contract.
    # TODO You can deploy your own smart contract(s) here.
    # TODO Code here ...
    pass
