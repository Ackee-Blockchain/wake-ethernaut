from wake.testing import *
from tests.ethernaut_deployer import EthernautDeployer
from pytypes.contracts.lv04_telephone import Telephone
# TODO You can import your our own smart contract(s) here.

@default_chain.connect()
def test_level_04():
    service = EthernautDeployer(default_chain)
    contract = service.deploy_lv04()
    do_level_04_solution(contract)
    service.check_lv04(contract)
    
def do_level_04_solution(contract: Telephone):
    # TODO Claim ownership of the contract.
    # TODO You can deploy your own smart contract(s) here.
    # TODO Code here ...
    pass
