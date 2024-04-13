from wake.testing import *
from tests.ethernaut_deployer import EthernautDeployer
from pytypes.contracts.lv26_double_entry_point import Forta, CryptoVault, LegacyToken, DoubleEntryPoint

from pytypes.contracts.attacker.lv26_double_entry_point import Dbot
# TODO You can import your our own smart contract(s) here.

@default_chain.connect()
def test_lv26():
    ethernaut = EthernautDeployer(default_chain)
    contract = ethernaut.deploy_lv26()
    exploit_lv26(ethernaut, contract)
    ethernaut.check_lv26(contract)

def exploit_lv26(ethernaut, contract: DoubleEntryPoint):
    crypto_vault_address: Address = contract.cryptoVault()
    forta_address: Address = contract.forta()
    crypto_vault = CryptoVault(crypto_vault_address)

    detection_bot = Dbot.deploy(crypto_vault.address, from_=ethernaut.attacker)
    Forta(forta_address).setDetectionBot(detection_bot.address, from_=ethernaut.attacker)
