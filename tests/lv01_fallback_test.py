from wake.testing import *
from tests.ethernaut_deployer import EthernautDeployer
from pytypes.contracts.lv01_fallback import Fallback


@default_chain.connect()
def test_level_01():
    service = EthernautDeployer(default_chain)
    contract = service.deploy_lv01()
    do_level_01_solution(contract)
    service.check_lv01(contract)

def do_level_01_solution(contract: Fallback):
    # TODO Claim ownership of the contract and reduce its balance to 0.
    # TODO Code here ...
    pass
