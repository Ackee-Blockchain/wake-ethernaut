from wake.testing import *
from tests.ethernaut_deployer import EthernautDeployer
from pytypes.contracts.lv00_hello import Tutorial


@default_chain.connect()
def test_level_00():
    service = EthernautDeployer(default_chain)
    contract = service.deploy_lv00()
    do_level_00_solution(contract)
    service.check_lv00(contract)

def do_level_00_solution(contract: Tutorial):
    # TODO Run this test to know, what to do next.
    print(contract.info())
    # TODO Code here ...
    pass
