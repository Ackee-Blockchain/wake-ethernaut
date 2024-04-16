from wake.testing import *
from tests.ethernaut_deployer import EthernautDeployer
from pytypes.contracts.lv14_gatekeeper_two import GatekeeperTwo
from pytypes.contracts.attacker.lv14_key_generator_two import GatekeeperTwoHelper

@default_chain.connect()
def test_lv14():
    ethernaut = EthernautDeployer(default_chain)
    contract = ethernaut.deploy_lv14()
    exploit_lv14(contract)
    ethernaut.check_lv14(contract)

def exploit_lv14(contract: GatekeeperTwo):
    # Attack vector - gate 1: tx.origin is not changed in redirect => this gate is the same
    # Attack vector - gate 2: code size must be 0 => the execution must be done before contract is deployed => inside constructor
    # Attack vector - gate 3: using rules for XOR => A xor B = C => A xor C = B
    # Training: know what attacker can have under his controll

    GatekeeperTwoHelper.deploy(victimAddress=contract.address)
