from wake.testing import *
from tests.ethernaut_deployer import EthernautDeployer
from pytypes.contracts.lv11_elevator import Elevator
# TODO You can import your our own smart contract(s) here.

@default_chain.connect()
def test_lv11():
    ethernaut = EthernautDeployer(default_chain)
    contract = ethernaut.deploy_lv11()
    exploit_lv11(contract)
    ethernaut.check_lv11(contract)

def exploit_lv11(contract: Elevator):
    # TODO Reach the top with this Elevator.
    # TODO You can import your our own smart contract(s) here.
    # TODO Code here ...
    pass