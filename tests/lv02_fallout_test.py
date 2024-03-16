from wake.testing import *
from tests.ethernaut_deployer import EthernautDeployer
from pytypes.contracts.lv02_fallout import Fallout


@default_chain.connect()
def test_level_02():
    service = EthernautDeployer(default_chain)
    contract = service.deploy_lv02()
    do_level_02_solution(contract)
    service.check_lv02(contract)

def do_level_02_solution(contract: Fallout):
    # TODO Claim ownership of the contract.
    # TODO Code here ...
    pass
