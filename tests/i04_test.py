from wake.testing import *
from tests.level_service import LevelService
from pytypes.contracts.i04_telephone import Telephone
# TODO You can import your our own smart contract(s) here.

@default_chain.connect()
def test_level_04():
    service = LevelService(default_chain)
    contract = service.deploy_level_04()
    do_level_04_solution(contract)
    service.check_level_04(contract)
    
def do_level_04_solution(contract: Telephone):
    # TODO Claim ownership of the contract.
    # TODO You can deploy your own smart contract(s) here.
    # TODO Code here ...
    pass
