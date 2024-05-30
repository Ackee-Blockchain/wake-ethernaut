from wake.testing import *
from tests.ethernaut_deployer import EthernautDeployer
from pytypes.contracts.lv04_telephone import Telephone
# TODO You can import your our own smart contract(s) here.

@default_chain.connect()
def test_lv04():
    ethernaut = EthernautDeployer(default_chain)
    contract = ethernaut.deploy_lv04()
    exploit_lv04(contract)
    ethernaut.check_lv04(contract)
    
def exploit_lv04(contract: Telephone):
    # TODO Claim ownership of the contract.
    # TODO You can deploy your own smart contract(s) here.
    # TODO Code here ...
    pass