from wake.testing import *
from tests.ethernaut_deployer import EthernautDeployer
from pytypes.contracts.lv19_alien_codex import AlienCodex
# TODO You can import your our own smart contract(s) here.

@default_chain.connect()
def test_lv19():
    ethernaut = EthernautDeployer(default_chain)
    contract = ethernaut.deploy_lv19()
    exploit_lv19(contract)
    ethernaut.check_lv19(contract)

def exploit_lv19(contract: AlienCodex):
    # TODO Claim ownership of the contract.
    # TODO You can import your our own smart contract(s) here.
    # TODO Code here ...
    pass
