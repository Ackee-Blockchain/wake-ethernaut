from wake.testing import *
from tests.ethernaut_deployer import EthernautDeployer
from pytypes.contracts.lv18_magic_num import MagicNum
from pytypes.contracts.attacker.lv18_magic_num import AttackMagicNum, AttackMagicNumDeployer

@default_chain.connect()
def test_lv18():
    ethernaut = EthernautDeployer(default_chain)
    contract = ethernaut.deploy_lv18()
    exploit_lv18(contract)
    ethernaut.check_lv18(contract)

def exploit_lv18(contract: MagicNum):
    exploitAddress = AttackMagicNum.deploy()
    deployedForCreationOfContract = AttackMagicNumDeployer.deploy()
    
    # Run code:
    run_piece1 = "602a" # push1 0x2a
    run_piece2 = "6080" # push1 0x80
    run_piece3 = "52" # mstore
    run_piece4 = "6020" # push1 0x20
    run_piece5 = "6080" # push1 0x80
    run_piece6 = "f3" # return
    runCode = run_piece1 + run_piece2 + run_piece3 + run_piece4 + run_piece5 + run_piece6 

    # Initialization code:
    initialize_piece1 = "600a" # push1 0x0a --- size of the code
    initialize_piece2 = "600c" # push1 0x0c --- current position of runtime opcodes
    initialize_piece3 = "6000" # push1 0x00  --- the destination position in the code memory
    initialize_piece4 = "39"   # CODECOPY
    initialize_piece5 = "600a" # push 0x0a
    initialize_piece6 = "6000" # push 0x00
    initialize_piece7 = "f3"   # return
    initializeCode = initialize_piece1 + initialize_piece2 + initialize_piece3 + initialize_piece4 + initialize_piece5 + initialize_piece6 + initialize_piece7
    combinedEncodedCode = (initializeCode + runCode) 
    
    addressOfSolver = deployedForCreationOfContract.deployFromBytecode(bytes.fromhex(combinedEncodedCode)).return_value
    contract.setSolver(addressOfSolver)
    