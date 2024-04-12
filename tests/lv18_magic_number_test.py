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
        "602a",  # PUSH1 0x2a --> 0x602a (Push number 0x2a - 42 in decimal)
        "6080",  # PUSH1 0x80 --> 0x6080 (Push an arbitrary selected memory slot 80)
        "52",    # MSTORE     --> 0x52   (Store the value using MSTORE(p, v) - at position p=0x80 store v=0x2a)
        "6020",  # PUSH1 0x20 --> 0x6020 (Push the size of the value - 32 bytes in decimal)
        "6080",  # PUSH1 0x80 --> 0x6080 (Push the location of the value 0x80)
        "f3"     # RETURN     --> 0xf3   (Return the value using RETURN(p, s) - at postion p=0x80 of length s=0x20)
    ]

    initialize_instructions = [
        "600a",  # PUSH1 0x0a --> 0x600a (Push size s=0x0a - 10 bytes in decimal)
        "600c",  # PUSH1 0x0c --> 0x600c (Push current location f=0x0c)
        "6000",  # PUSH1 0x00 --> 0x6000 (Push memory location t=0x00)
        "39",    # CODECOPY   --> 0x39   (Calling CODECOPY(t, f, s) - at destination t=0x00 from current position f=0c of size s=0x0a)
        "600a",  # PUSH1 0x0a --> 0x600a (Push the size of optcode - 10 bytes in decimal)
        "6000",  # PUSH1 0x00 --> 0x6000 (Push the location of the optcode - slot 0x00)
        "f3"     # RETURN     --> 0xf3   (Return the optcode using RETURN(p, s) - at postion p=0x00 of length s=0x0a)
    ]

    final_code = bytes.fromhex( ''.join(initialize_instructions) + ''.join(run_instructions) )
    solver_address = code_deployer.deployCode(final_code).return_value
    contract.setSolver(solver_address)
    