from wake.testing import *
from tests.ethernaut_deployer import EthernautDeployer
from pytypes.contracts.lv14_gatekeeper_two import GatekeeperTwo
from pytypes.contracts.attacker.lv14_gatekeeper_two import AttackGatekeeperTwo


@default_chain.connect()
def test_lv14():
    ethernaut = EthernautDeployer(default_chain)
    contract = ethernaut.deploy_lv14()
    exploit_lv14(contract, ethernaut.attacker)
    ethernaut.check_lv14(contract)

def exploit_lv14(contract: GatekeeperTwo, attacker: Account):
    exploitContract = AttackGatekeeperTwo.deploy(victimAddress=contract.address, from_=attacker.address)

