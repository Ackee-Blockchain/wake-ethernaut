from wake.testing import *
from tests.ethernaut_deployer import EthernautDeployer
from pytypes.contracts.lv07_force import Force
from pytypes.contracts.attacker.lv07_transfer import ForceTransfer

@default_chain.connect()
def test_lv07():
    ethernaut = EthernautDeployer(default_chain)
    contract = ethernaut.deploy_lv07()
    exploit_lv07(contract)
    ethernaut.check_lv07(contract)

def exploit_lv07(contract: Force):
    # Attack vector: selfdestruct and minting transfer Ether directly -> no recive/fallback function is invoked
    # Training: know how to force transfer Ether

    ForceTransfer.deploy(contract, value=100)
