from wake.testing import *
from tests.ethernaut_deployer import EthernautDeployer
from pytypes.contracts.lv26_double_entry_point import DoubleEntryPoint
# TODO You can import your our own smart contract(s) here.

@default_chain.connect()
def test_lv26():
    ethernaut = EthernautDeployer(default_chain)
    contract = ethernaut.deploy_lv26()
    exploit_lv26(contract)
    ethernaut.check_lv26(contract)

def exploit_lv26(contract: DoubleEntryPoint):
    # TODO Protect the CryptoVault from being drained out of tokens.
    # TODO You can import your our own smart contract(s) here.
    # TODO Code here ...
    pass
