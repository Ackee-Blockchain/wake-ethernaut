from wake.testing import *
from tests.ethernaut_deployer import EthernautDeployer
from pytypes.contracts.lv28_gatekeeper_three import GatekeeperThree
# TODO You can import your our own smart contract(s) here.

@default_chain.connect()
def test_lv28():
    ethernaut = EthernautDeployer(default_chain)
    contract = ethernaut.deploy_lv28()
    exploit_lv28(contract)
    ethernaut.check_lv28(contract)

def exploit_lv28(contract: GatekeeperThree):
    # TODO Make it past the gatekeeper and register as an entrant to pass this level.
    # TODO You can import your our own smart contract(s) here.
    # TODO Code here ...
    pass
