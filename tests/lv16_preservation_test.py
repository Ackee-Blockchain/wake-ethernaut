from wake.testing import *
from tests.ethernaut_deployer import EthernautDeployer
from pytypes.contracts.lv16_preservation import Preservation
# TODO You can import your our own smart contract(s) here.

@default_chain.connect()
def test_lv16():
    ethernaut = EthernautDeployer(default_chain)
    contract = ethernaut.deploy_lv16()
    exploit_lv16(contract)
    ethernaut.check_lv16(contract)

def exploit_lv16(contract: Preservation):
    # TODO Claim ownership of the contract.
    # TODO You can import your our own smart contract(s) here.
    # TODO Code here ...
    pass
