from wake.testing import *
from tests.ethernaut_deployer import EthernautDeployer
from pytypes.contracts.lv09_king import King
# TODO You can import your our own smart contract(s) here.

@default_chain.connect()
def test_lv09():
    ethernaut = EthernautDeployer(default_chain)
    contract = ethernaut.deploy_lv09()
    newOwner = exploit_lv09(contract, ethernaut.attacker)
    ethernaut.check_lv09(contract, newOwner)

def exploit_lv09(contract: King, attacker: Account) -> Address:
    # TODO Became the new king and break the game - no one can claim the kingship from you.
    # TODO Return the address of the new king.
    # TODO You can import your our own smart contract(s) here.
    # TODO Code here ...
    return attacker.address