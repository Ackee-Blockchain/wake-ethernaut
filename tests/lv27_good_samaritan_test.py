from wake.testing import *
from tests.ethernaut_deployer import EthernautDeployer
from pytypes.contracts.lv27_good_samaritan import GoodSamaritan, Coin, Wallet, INotifyable

from pytypes.contracts.attacker.lv27_good_samaritan import Attacker


@default_chain.connect()
def test_lv27():
    ethernaut = EthernautDeployer(default_chain)
    contract = ethernaut.deploy_lv27()
    exploit_lv27(ethernaut, contract)
    ethernaut.check_lv27(contract)

def exploit_lv27(ethernaut, contract: GoodSamaritan):
    wallet:Wallet = contract.wallet()
    coin:Coin = contract.coin()

    attacker_contract = Attacker.deploy(contract.address, from_ = ethernaut.attacker)
    attacker_contract.attack(from_ = ethernaut.attacker)
    
