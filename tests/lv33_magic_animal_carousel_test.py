from wake.testing import *
from tests.ethernaut_deployer import EthernautDeployer
from pytypes.contracts.lv33_magic_animal_carousel import MagicAnimalCarousel
# TODO You can import your our own smart contract(s) here.

@default_chain.connect()
def test_lv33():
    ethernaut = EthernautDeployer(default_chain)
    contract = ethernaut.deploy_lv33()
    exploit_lv33(contract)
    ethernaut.check_lv33(contract)

def exploit_lv33(contract: MagicAnimalCarousel):
    # TODO ?
    # TODO You can import your our own smart contract(s) here.
    # TODO Code here ...
    pass
