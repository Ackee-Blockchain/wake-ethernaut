from wake.testing import *
from tests.ethernaut_deployer import EthernautDeployer
from pytypes.contracts.lv15_naught_coin import NaughtCoin
# TODO You can import your our own smart contract(s) here.

@default_chain.connect()
def test_lv15():
    ethernaut = EthernautDeployer(default_chain)
    contract = ethernaut.deploy_lv15()
    exploit_lv15(contract)
    ethernaut.check_lv15(contract)

def exploit_lv15(contract: NaughtCoin):
    # TODO Your goal is to withdraw all you "freezed" assets to another account
    # TODO You can import your our own smart contract(s) here.
    # TODO Code here ...
    pass
