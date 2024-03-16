from wake.testing import *
from tests.ethernaut_deployer import EthernautDeployer
from pytypes.contracts.lv00_hello import Tutorial
# TODO You can import your our own smart contract(s) here.

@default_chain.connect()
def _level_00():
    service = EthernautDeployer(default_chain)
    contract = service.deploy_lv00()
    do_level_00_solution(contract)
    service.check_lv00(contract)

def do_level_00_solution(contract: Tutorial):
    # TODO ?
    # TODO You can import your our own smart contract(s) here.
    # TODO Code here ...
    pass
