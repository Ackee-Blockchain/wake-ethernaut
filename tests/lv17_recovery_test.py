from wake.testing import *
from tests.ethernaut_deployer import EthernautDeployer
from pytypes.contracts.lv17_recovery import Recovery
# TODO You can import your our own smart contract(s) here.

@default_chain.connect()
def test_lv17():
    ethernaut = EthernautDeployer(default_chain)
    contract = ethernaut.deploy_lv17()
    foundContract = exploit_lv17(contract)
    ethernaut.check_lv17(contract,  foundContract)

def exploit_lv17(contract: Recovery) -> Address:
    # TODO Find the lost address of deployed contract.
    # TODO You can import your our own smart contract(s) here.
    # TODO Code here ...
    pass
