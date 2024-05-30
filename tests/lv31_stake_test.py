from wake.testing import *
from tests.ethernaut_deployer import EthernautDeployer
from pytypes.contracts.lv31_stake import Stake
# TODO You can import your our own smart contract(s) here.

@default_chain.connect()
def test_lv31():
    ethernaut = EthernautDeployer(default_chain)
    contract = ethernaut.deploy_lv31()
    exploit_lv31(contract, ethernaut.attacker, ethernaut.other_account)
    ethernaut.check_lv31(contract)

def exploit_lv31(contract: Stake, attacker: Account, other_account: Account):
    # TODO Drain some ether from the Stake contract.
    # TODO You can import your our own smart contract(s) here.
    # TODO Code here ...
    pass
