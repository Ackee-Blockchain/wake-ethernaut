from wake.testing import *
from tests.level_service import LevelService
from pytypes.contracts.i00_hello import Tutorial


@default_chain.connect()
def test_level_00():
    service = LevelService(default_chain)
    contract = service.deploy_level_00()
    do_level_00_solution(contract)
    service.check_level_00(contract)

def do_level_00_solution(contract: Tutorial):
    # TODO Run this test to know, what to do next.
    print(contract.info())
    # TODO Code here ...
    pass
