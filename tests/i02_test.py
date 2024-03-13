from wake.testing import *
from tests.level_service import LevelService
from pytypes.contracts.i02_fallout import Fallout


@default_chain.connect()
def test_level_02():
    service = LevelService(default_chain)
    contract = service.deploy_level_02()
    do_level_02_solution(contract)
    service.check_level_02(contract)

def do_level_02_solution(contract: Fallout):
    # Problem: unsecured construction method
    contract.Fal1out()
