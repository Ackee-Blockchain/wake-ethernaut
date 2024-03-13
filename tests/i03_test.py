from wake.testing import *
from tests.level_service import LevelService
from pytypes.contracts.i03_coinflip import CoinFlip
from pytypes.contracts.attacker.i03_coinflip_solver import CoinFlipSolver

@default_chain.connect()
def test_level_03():
    service = LevelService(default_chain)
    contract = service.deploy_level_03()
    do_level_03_solution(contract)
    service.check_level_03(contract)

def do_level_03_solution(contract: CoinFlip):
    # Problem: any calculations can be done by deployed helper contract, which than calls the original contract
    solver = CoinFlipSolver.deploy()

    for i in range(11):
        tx = solver.solveFlip(contract.address)
        side, result = tx.return_value
        assert True == result
        print(f"In block#{tx.block_number} you guessed {side} and you were right!")
