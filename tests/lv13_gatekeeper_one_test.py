from wake.testing import *
from tests.ethernaut_deployer import EthernautDeployer
from pytypes.contracts.lv13_gatekeeper_one import GatekeeperOne
# TODO You can import your our own smart contract(s) here.

@default_chain.connect()
def test_lv13():
    ethernaut = EthernautDeployer(default_chain)
    contract = ethernaut.deploy_lv13()
    exploit_lv13(contract, ethernaut.attacker)
    ethernaut.check_lv13(contract)

def exploit_lv13(contract: GatekeeperOne, attacker: Account):
    # TODO Make it past the gatekeeper and register as an entrant to pass this level.
    # TODO You can import your our own smart contract(s) here.
    # TODO Code here ...
    pass