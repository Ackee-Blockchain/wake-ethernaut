from wake.testing import *
from tests.ethernaut_deployer import EthernautDeployer
from pytypes.contracts.lv05_token import Token


@default_chain.connect()
def test_level_05():
    service = EthernautDeployer(default_chain)
    contract = service.deploy_lv05()
    do_level_05_solution(contract, service.other_account)
    service.check_lv05(contract)

def do_level_05_solution(contract: Token, other_account: Account):
    # Problem: overflow of unsigned int
    contract.transfer(other_account, 21)
