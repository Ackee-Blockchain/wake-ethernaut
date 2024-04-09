from wake.testing import *
from tests.ethernaut_deployer import EthernautDeployer
from pytypes.contracts.lv14_gatekeeper_two import GatekeeperTwo
# TODO You can import your our own smart contract(s) here.

@default_chain.connect()
def test_lv29():
    ethernaut = EthernautDeployer(default_chain)
    contract = ethernaut.deploy_lv29()
    exploit_lv29(contract)
    ethernaut.check_lv29(contract)

def exploit_lv29(contract: GatekeeperTwo):
    # TODO ?
    # TODO You can import your our own smart contract(s) here.
    # TODO Code here ...
    pass
