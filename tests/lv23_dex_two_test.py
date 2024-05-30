from wake.testing import *
from tests.ethernaut_deployer import EthernautDeployer
from pytypes.contracts.lv23_dex_two import DexTwo, SwappableTokenTwo
# TODO You can import your our own smart contract(s) here.

@default_chain.connect()
def test_lv23():
    ethernaut = EthernautDeployer(default_chain)
    contract = ethernaut.deploy_lv23()
    exploit_lv23(contract, ethernaut.attacker)
    ethernaut.check_lv23(contract)

def exploit_lv23(contract: DexTwo, attacker: Account):
    # TODO Drain all the tokens from the dex.
    # TODO You can import your our own smart contract(s) here.
    # TODO Code here ...
    pass
