from wake.testing import *
from tests.level_service import LevelService
from pytypes.contracts.i01_fallback import Fallback


@default_chain.connect()
def test_level_01():
    service = LevelService(default_chain)
    contract = service.deploy_level_01()
    do_level_01_solution(contract)
    service.check_level_01(contract)

def do_level_01_solution(contract: Fallback):
    # Training: payable methods, default recieve method
    with must_revert(): # contribution too big, not allowed
        contract.contribute(value=1*10**15) # send 0.001 Eth = 1 * 10^15 Wei (10^18 = 1 ETH)
    
    contract.contribute(value=1) # send just 1 Wei
    contract.transact(value=1) # default recieve 1 Wei
    contract.withdraw()
