from wake.testing import *
from tests.ethernaut_deployer import EthernautDeployer
from pytypes.contracts.lv26_double_entry_point import DoubleEntryPoint

from pytypes.contracts.attacker.lv26_detection_bot import DetectionBot

@default_chain.connect()
def test_lv26():
    ethernaut = EthernautDeployer(default_chain)
    contract = ethernaut.deploy_lv26()
    exploit_lv26(contract)
    ethernaut.check_lv26(contract)

def exploit_lv26(contract: DoubleEntryPoint):
    detection_bot = DetectionBot.deploy(contract.cryptoVault())
    contract.forta().setDetectionBot(detection_bot.address)
