from wake.testing import *
from tests.ethernaut_deployer import EthernautDeployer
from pytypes.contracts.lv24_puzzle_wallet import PuzzleWallet, PuzzleProxy
# TODO You can import your our own smart contract(s) here.

@default_chain.connect()
def test_lv24():
    ethernaut = EthernautDeployer(default_chain)
    contract = ethernaut.deploy_lv24()
    exploit_lv24(contract, ethernaut.attacker)
    ethernaut.check_lv24(contract)

def exploit_lv24(contract: PuzzleProxy, attacker: Account):
    # TODO Become the admin of the wallet and drain all it's funds.
    # TODO You can import your our own smart contract(s) here.
    # TODO Code here ...
    pass
