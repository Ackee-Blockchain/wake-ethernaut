from wake.testing import *
from tests.ethernaut_deployer import EthernautDeployer
from pytypes.contracts.lv25_motorbike import Motorbike, Engine
# TODO You can import your our own smart contract(s) here.

@default_chain.connect()
def test_lv25():
    ethernaut = EthernautDeployer(default_chain)
    contract = ethernaut.deploy_lv25()
    exploit_lv25(contract)
    ethernaut.check_lv25(contract)

def exploit_lv25(contract: Motorbike):
    # TODO Selfdestruct the motorbike's engine and take all it's Ether gas.
    # TODO You can import your our own smart contract(s) here.
    # TODO Code here ...
    pass
