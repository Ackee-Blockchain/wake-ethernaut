from wake.testing import *
from tests.ethernaut_deployer import EthernautDeployer
from pytypes.contracts.lv08_vault import Vault
# TODO You can import your our own smart contract(s) here.

@default_chain.connect()
def test_lv08():
    ethernaut = EthernautDeployer(default_chain)
    contract = ethernaut.deploy_lv08()
    exploit_lv08(contract, default_chain)
    ethernaut.check_lv08(contract)

def exploit_lv08(contract: Vault, blockchain: Chain):
    # TODO Unlock the vault.
    # TODO You can import your our own smart contract(s) here.
    # TODO Code here ...
    pass