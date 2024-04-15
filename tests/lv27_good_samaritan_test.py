from wake.testing import *
from tests.ethernaut_deployer import EthernautDeployer
from pytypes.contracts.lv27_good_samaritan import GoodSamaritan
from pytypes.contracts.attacker.lv27_good_samaritan import Attacker

@default_chain.connect()
def test_lv27():
    ethernaut = EthernautDeployer(default_chain)
    contract = ethernaut.deploy_lv27()
    exploit_lv27(contract)
    ethernaut.check_lv27(contract)

def exploit_lv27(contract: GoodSamaritan):
    attacker_contract = Attacker.deploy(contract.address)
    attacker_contract.attack()
