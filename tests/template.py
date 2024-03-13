from wake.testing import *
from tests.level_service import LevelService
from pytypes.contracts.i00_hello import Tutorial
# TODO You can import your our own smart contract(s) here.

@default_chain.connect()
def _level_00():
    service = LevelService(default_chain)
    contract = service.deploy_level_00()
    do_level_00_solution(contract)
    service.check_level_00(contract)

def do_level_00_solution(contract: Tutorial):
    # TODO ?
    # TODO You can import your our own smart contract(s) here.
    # TODO Code here ...
    pass
