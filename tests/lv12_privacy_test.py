from wake.testing import *
from tests.ethernaut_deployer import EthernautDeployer
from pytypes.contracts.lv12_privacy import Privacy
# TODO You can import your our own smart contract(s) here.

@default_chain.connect()
def test_lv12():
    ethernaut = EthernautDeployer(default_chain)
    contract = ethernaut.deploy_lv12()
    exploit_lv12(contract)
    ethernaut.check_lv12(contract)

def exploit_lv12(contract: Privacy):
    # TODO Unlock the contract.
    # TODO You can import your our own smart contract(s) here.
    # TODO Code here ...
    pass
