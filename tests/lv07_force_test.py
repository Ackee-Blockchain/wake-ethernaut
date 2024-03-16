from wake.testing import *
from tests.ethernaut_deployer import EthernautDeployer
from pytypes.contracts.lv07_force import Force
# TODO You can import your our own smart contract(s) here.

@default_chain.connect()
def test_level_07():
    service = EthernautDeployer(default_chain)
    contract = service.deploy_lv07()
    do_level_07_solution(contract)
    service.check_lv07(contract)

def do_level_07_solution(contract: Force):
    # TODO Force this contract to take some Ether.
    # TODO You can import your our own smart contract(s) here.
    # TODO Code here ...
    pass
