from wake.testing import *
from tests.level_service import LevelService
from pytypes.contracts.i08_vault import Vault
# TODO You can import your our own smart contract(s) here.

@default_chain.connect()
def test_level_08():
    service = LevelService(default_chain)
    contract = service.deploy_level_08()
    do_level_08_solution(contract, default_chain)
    service.check_level_08(contract)

def do_level_08_solution(contract: Vault, blockchain: Chain):
    # TODO Unlock the vault.
    # TODO You can import your our own smart contract(s) here.
    # TODO Code here ...
    pass
