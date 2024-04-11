from wake.testing import *
from tests.ethernaut_deployer import EthernautDeployer
from pytypes.contracts.lv18_magic_number import MagicNum
from pytypes.contracts.helper.Deployer import Deployer

@default_chain.connect()
def test_lv18():
    ethernaut = EthernautDeployer(default_chain)
    contract = ethernaut.deploy_lv18()
    exploit_lv18(contract)
    ethernaut.check_lv18(contract)

def exploit_lv18(contract: MagicNum):
    # Attack vector:
    # Training:
    
    code_deployer = Deployer.deploy()
    
    run_instructions = [
        "602a",  # PUSH1 0x2a
        "6080",  # PUSH1 0x80
        "52",    # MSTORE
        "6020",  # PUSH1 0x20
        "6080",  # PUSH1 0x80
        "f3"     # RETURN
    ]

    initialize_instructions = [
        "600a",  # PUSH1 0x0a
        "600c",  # PUSH1 0x0c
        "6000",  # PUSH1 0x00
        "39",    # CODECOPY
        "600a",  # push 0x0a
        "6000",  # push 0x00
        "f3"     # RETURN
    ]

    final_code = bytes.fromhex( ''.join(initialize_instructions) + ''.join(run_instructions) )
    solver_address = code_deployer.deployCode(final_code).return_value
    contract.setSolver(solver_address)
    