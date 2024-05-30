from wake.testing import *
from tests.ethernaut_deployer import EthernautDeployer
from pytypes.contracts.lv20_denial import Denial
# TODO You can import your our own smart contract(s) here.

@default_chain.connect()
def test_lv20():
    ethernaut = EthernautDeployer(default_chain)
    contract = ethernaut.deploy_lv20()
    exploit_lv20(contract)
    ethernaut.check_lv20(contract)
    
def exploit_lv20(contract: Denial):
    # TODO Deny the owner from withdrawing funds.
    # TODO You can import your our own smart contract(s) here.
    # TODO Code here ...
    pass
