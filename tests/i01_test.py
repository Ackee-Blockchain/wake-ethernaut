from wake.testing import *
from tests.level_service import LevelService
from pytypes.contracts.i01_fallback import Fallback


@default_chain.connect()
def test_level_01():
    service = LevelService(default_chain)
    contract = service.deploy_level_01()
    do_level_01_solution(contract)
    service.check_level_01(contract)

def do_level_01_solution(contract: Fallback):
    # TODO Claim ownership of the contract and reduce its balance to 0.
    # TODO Code here ...
    pass
