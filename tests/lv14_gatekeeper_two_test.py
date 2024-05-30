from wake.testing import *
from tests.ethernaut_deployer import EthernautDeployer
from pytypes.contracts.lv14_gatekeeper_two import GatekeeperTwo
# TODO You can import your our own smart contract(s) here.

@default_chain.connect()
def test_lv14():
    ethernaut = EthernautDeployer(default_chain)
    contract = ethernaut.deploy_lv14()
    exploit_lv14(contract)
    ethernaut.check_lv14(contract)

def exploit_lv14(contract: GatekeeperTwo):
    # TODO Make it past the gatekeeper and register as an entrant to pass this level.
    # TODO You can import your our own smart contract(s) here.
    # TODO Code here ...
    pass
