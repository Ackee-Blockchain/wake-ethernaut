from wake.testing import *
from tests.level_service import LevelService
from pytypes.contracts.i07_force import Force
# TODO You can import your our own smart contract(s) here.

@default_chain.connect()
def test_level_07():
    service = LevelService(default_chain)
    contract = service.deploy_level_07()
    do_level_07_solution(contract)
    service.check_level_07(contract)

def do_level_07_solution(contract: Force):
    # TODO Force this contract to take some Ether.
    # TODO You can import your our own smart contract(s) here.
    # TODO Code here ...
    pass
