from wake.testing import *
from tests.ethernaut_deployer import EthernautDeployer
from pytypes.contracts.lv03_coinflip import CoinFlip
# TODO You can import your our own smart contract(s) here.

@default_chain.connect()
def test_lv03():
    ethernaut = EthernautDeployer(default_chain)
    contract = ethernaut.deploy_lv03()
    exploit_lv03(contract)
    ethernaut.check_lv03(contract)

def exploit_lv03(contract: CoinFlip):
    # TODO Guess the correct outcome 10 times in a row.
    # TODO You can deploy your own smart contract(s) here.
    # TODO Code here ...
    pass