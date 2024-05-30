from wake.testing import *
from tests.ethernaut_deployer import EthernautDeployer
from pytypes.contracts.lv18_magic_number import MagicNum
# TODO You can import your our own smart contract(s) here.

@default_chain.connect()
def test_lv18():
    ethernaut = EthernautDeployer(default_chain)
    contract = ethernaut.deploy_lv18()
    exploit_lv18(contract)
    ethernaut.check_lv18(contract)

def exploit_lv18(contract: MagicNum):
    # TODO Provide solver, that can answer the question "What is the meaning of life?".
    # TODO You can import your our own smart contract(s) here.
    # TODO Code here ...
    pass
