from wake.testing import *
from tests.ethernaut_deployer import EthernautDeployer
from pytypes.contracts.lv16_preservation import Preservation
from pytypes.contracts.attacker.lv16_delegate_call_exploitation import AttackPreservation

@default_chain.connect()
def test_lv16():
    ethernaut = EthernautDeployer(default_chain)
    contract = ethernaut.deploy_lv16()
    exploit_lv16(contract)
    ethernaut.check_lv16(contract)

def exploit_lv16(contract: Preservation):
    # Attack vector:
    # Training:

    exploitContract = AttackPreservation.deploy(victimContract=contract.address)
    exploitContract.exploit()