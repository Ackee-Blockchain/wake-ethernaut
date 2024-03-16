from wake.testing import *
from tests.ethernaut_deployer import EthernautDeployer
from pytypes.contracts.lv03_coinflip import CoinFlip
# TODO You can import your our own smart contract(s) here.

@default_chain.connect()
def test_level_03():
    service = EthernautDeployer(default_chain)
    contract = service.deploy_lv03()
    do_level_03_solution(contract)
    service.check_lv03(contract)

def do_level_03_solution(contract: CoinFlip):
    # TODO Guess the correct outcome 10 times in a row.
    # TODO You can deploy your own smart contract(s) here.
    # TODO Code here ...
    pass
