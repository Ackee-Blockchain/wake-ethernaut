from wake.testing import *
from tests.ethernaut_deployer import EthernautDeployer
from pytypes.contracts.lv30_higher_order import HigherOrder
# TODO You can import your our own smart contract(s) here.

@default_chain.connect()
def test_lv30():
    ethernaut = EthernautDeployer(default_chain)
    contract = ethernaut.deploy_lv30()
    exploit_lv30(contract)
    ethernaut.check_lv30(contract)

def exploit_lv30(contract: HigherOrder):
    # TODO Become the Commander of the Higher Order!
    # TODO You can import your our own smart contract(s) here.
    # TODO Code here ...
    pass
