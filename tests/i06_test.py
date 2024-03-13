from wake.testing import *
from tests.level_service import LevelService
from pytypes.contracts.i06_delegation import Delegate, Delegation
# TODO You can import your our own smart contract(s) here.

@default_chain.connect()
def test_level_06():
    service = LevelService(default_chain)
    contract = service.deploy_level_06()
    do_level_06_solution(contract)
    service.check_level_06(contract)

def do_level_06_solution(contract: Delegation):
    # TODO Claim ownership of the contract.
    # TODO You can deploy your own smart contract(s) here.
    # TODO Code here ...
    pass
