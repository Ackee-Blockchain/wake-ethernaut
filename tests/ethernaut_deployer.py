import random
import string

from wake.testing import *
from pytypes.contracts.lv00_hello import Tutorial
from pytypes.contracts.lv01_fallback import Fallback
from pytypes.contracts.lv02_fallout import Fallout
from pytypes.contracts.lv03_coinflip import CoinFlip
from pytypes.contracts.lv04_telephone import Telephone
from pytypes.contracts.lv05_token import Token
from pytypes.contracts.lv06_delegation import Delegate, Delegation
from pytypes.contracts.lv07_force import Force
from pytypes.contracts.lv08_vault import Vault
from pytypes.contracts.lv09_king import King
from pytypes.contracts.lv10_reentrancy import Reentrance

class EthernautDeployer:
    chain: Chain
    owner: Account
    attacker: Account
    other_account: Account

    def __init__(self, chain: Chain):
        self.chain = chain
        self.owner = self.chain.accounts[0]
        self.attacker = self.chain.accounts[1]
        self.other_account = self.chain.accounts[2]
        self.chain.set_default_accounts(self.attacker)
        self.attacker.balance = 10 * 10**18             # set attacker's balance to 10 Eth

    def deploy_lv00(self):
        return Tutorial.deploy("ethernaut0", from_=self.owner)
    
    def deploy_lv01(self):
        return Fallback.deploy(from_=self.owner)
    
    def deploy_lv02(self):
        return Fallout.deploy(from_=self.owner)

    def deploy_lv03(self):
        return CoinFlip.deploy(from_=self.owner)
    
    def deploy_lv04(self):
        return Telephone.deploy(from_=self.owner)
    
    def deploy_lv05(self):
        contract = Token.deploy(1000, from_=self.owner)        # owner deploys the contract
        contract.transfer(self.attacker, 20, from_=self.owner) # owner gives you 20 tokens to start with
        return contract
    
    def deploy_lv06(self):
        delegate = Delegate.deploy(self.owner, from_=self.owner)     # first deploy the delegate
        return Delegation.deploy(delegate.address, from_=self.owner) # than deploy the delegation with address to delegate 
    
    def deploy_lv07(self):
        return Force.deploy(from_=self.owner)
    
    def deploy_lv08(self):
        vault_key = ''.join(random.choice(string.ascii_letters + string.digits) for i in range(random.randint(7,13)))
        return Vault.deploy(bytes32(bytes(vault_key, "ascii")), from_=self.owner)
    
    def deploy_lv09(self):
        return King.deploy(from_=self.owner, value=1 * 10**18)
    
    def deploy_lv10(self):
        contract = Reentrance.deploy(from_=self.owner)
        contract.transact(value=5 * 10**18, from_=self.owner)
        contract.donate(self.other_account, from_=self.owner, value=1 * 10**18)
        contract.donate(self.owner, from_=self.owner, value=3 * 10**18)
        contract.withdraw(2 * 10**18, from_=self.owner)
        return contract
    
    def check_attacker_is(self, contract_owner: Account, msg = "owner"):
        assert contract_owner == self.attacker.address, f"You must take the {msg}ship."
        print(f"You are the {msg} now.")
    
    def check_lv00(self, contract: Tutorial):
        assert contract.getCleared(), "You must hack the authentication."
        print("You passed the authentication, well done!")
        print("Level 00 passed.")

    def check_lv01(self, contract: Fallback):
        self.check_attacker_is(contract.owner())
        assert contract.balance == 0, "You must take all the funds."
        print("You taken it all, well done!")
        print("Level 01 passed.")
        
    def check_lv02(self, contract: Fallout):
        self.check_attacker_is(contract.owner())
        print("Level 02 passed.")
        
    def check_lv03(self, contract: CoinFlip):
        assert contract.consecutiveWins() >= 10, "You must guess right at least 10 times in row."
        print("You guessed it right 10 times consecutively, impressive!")
        print("Level 03 passed")
        
    def check_lv04(self, contract: Telephone):
        self.check_attacker_is(contract.owner())
        print("Level 04 passed.")
        
    def check_lv05(self, contract: Token):
        balance = contract.balanceOf(self.attacker)
        print(f"You obtained {balance} tokens.")
        assert balance >= 1020, "You must steal at least 1020 tokens."
        if balance == 115792089237316195423570985008687907853269984665640564039457584007913129639935:
            print("Nicely done, you took maximum amout of tokens possible.")
        elif balance >= 10000:
            print("Wait, where did you get so many tokens?!")
        print("Level 05 passed.")

    def check_lv06(self, contract: Delegation):
        self.check_attacker_is(contract.owner())
        print("Level 06 passed")

    def check_lv07(self, contract: Force):
        assert contract.balance > 0, "You must force the cat to take some Ether."
        print("Wait... How did you force the cat to take it?!")
        print("Level 07 passed")

    def check_lv08(self, contract: Vault):
        assert contract.locked() == False, "You must unlock the vault."
        print("Your lockpicking skills are almost as good as LockPickingLawyer's.")
        print("Level 08 passed")

    def check_lv09(self, contract: King):
        self.check_attacker_is(contract._king(), "king")
        with must_revert:
            contract.transact(value=10_000 * 10**18, from_=self.owner)
        print("Level 09 passed")

    def check_lv10(self, contract: Reentrance):
        assert contract.balance == 0, "You must withdraw all funds."
        print("Level 09 passed")