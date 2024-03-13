from wake.testing import *
from tests.level_service import LevelService
from pytypes.contracts.i05_token import Token


@default_chain.connect()
def test_level_05():
    service = LevelService(default_chain)
    contract = service.deploy_level_05()
    do_level_05_solution(contract, service.other_account)
    service.check_level_05(contract)

def do_level_05_solution(contract: Token, other_account: Account):
    # Problem: overflow of unsigned int
    contract.transfer(other_account, 21)
