from wake.testing import *
from tests.level_service import LevelService
from pytypes.contracts.i05_token import Token
# TODO You can import your our own smart contract(s) here.

@default_chain.connect()
def test_level_05():
    service = LevelService(default_chain)
    contract = service.deploy_level_05()
    do_level_05_solution(contract, service.other_account)
    service.check_level_05(contract)

def do_level_05_solution(contract: Token, other_account: Account):
    # TODO Get your hands on any additional tokens, preferably a very large amount of tokens.
    # TODO You can deploy your own smart contract(s) here.
    # TODO Code here ...
    pass
