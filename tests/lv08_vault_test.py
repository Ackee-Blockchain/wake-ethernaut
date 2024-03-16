from wake.testing import *
from tests.ethernaut_deployer import EthernautDeployer
from pytypes.contracts.lv08_vault import Vault
# TODO You can import your our own smart contract(s) here.

@default_chain.connect()
def test_level_08():
    service = EthernautDeployer(default_chain)
    contract = service.deploy_lv08()
    do_level_08_solution(contract, default_chain)
    service.check_lv08(contract)

def do_level_08_solution(contract: Vault, blockchain: Chain):
    # TODO Unlock the vault.
    # TODO You can import your our own smart contract(s) here.
    # TODO Code here ...
    pass
