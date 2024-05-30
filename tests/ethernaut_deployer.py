import os
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
from pytypes.contracts.lv11_elevator import Elevator
from pytypes.contracts.lv12_privacy import Privacy
from pytypes.contracts.lv13_gatekeeper_one import GatekeeperOne
from pytypes.contracts.lv14_gatekeeper_two import GatekeeperTwo
from pytypes.contracts.lv15_naught_coin import NaughtCoin
from pytypes.contracts.lv16_preservation import Preservation, LibraryContract
from pytypes.contracts.lv17_recovery import Recovery
from pytypes.contracts.lv18_magic_number import MagicNum
from pytypes.contracts.lv19_alien_codex import AlienCodex
from pytypes.contracts.lv20_denial import Denial
from pytypes.contracts.lv21_shop import Shop
from pytypes.contracts.lv22_dex import Dex, SwappableToken
from pytypes.contracts.lv23_dex_two import DexTwo, SwappableTokenTwo
from pytypes.contracts.lv24_puzzle_wallet import PuzzleWallet, PuzzleProxy
from pytypes.contracts.lv25_motorbike import Motorbike, Engine
from pytypes.contracts.lv27_good_samaritan import GoodSamaritan
from pytypes.contracts.lv26_double_entry_point import Forta, CryptoVault, LegacyToken, DoubleEntryPoint, DelegateERC20
from pytypes.contracts.lv28_gatekeeper_three import GatekeeperThree
from pytypes.contracts.lv29_switch import Switch
from pytypes.contracts.lv30_higher_order import HigherOrder
from pytypes.contracts.lv31_stake import Stake
from pytypes.contracts.helper.DefaultERC20 import DefaultERC20
from pytypes.contracts.helper.CheckSizeContract import CheckSizeContract
from pytypes.contracts.helper.Deployer import Deployer
from pytypes.contracts.helper.ForceTransfer import ForceTransfer
from pathlib import Path


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
        self.attacker.balance = 10 * 10**18             # lower attacker's balance to 10 Eth
        print()

    #################### Shared helper functions ####################

    def check_attacker_is(self, contract_owner: Account, must = "You must take the ownership.", done = "You are the owner now."):
        assert contract_owner == self.attacker.address, must
        print(done)
        
    def check_attacker_is_entrant(self, entrant: Account):
        self.check_attacker_is(entrant, "You must pass the gatekeeper.", "You passed the gate.")
        return Switch.deploy(from_=self.owner)

    #################### LEVEL 00 ####################

    def deploy_lv00(self) -> Tutorial:
        return Tutorial.deploy("ethernaut0", from_=self.owner)
    
    def check_lv00(self, contract: Tutorial):
        assert contract.getCleared(), "You must hack the authentication."
        print("You passed the authentication, well done!")
        print("Level 00 passed.")

    #################### LEVEL 01 ####################

    def deploy_lv01(self) -> Fallback:
        return Fallback.deploy(from_=self.owner)
    
    def check_lv01(self, contract: Fallback):
        self.check_attacker_is(contract.owner())
        assert contract.balance == 0, "You must take all the funds."
        print("You taken it all, well done!")
        print("Level 01 passed.")

    #################### LEVEL 02 ####################
    
    def deploy_lv02(self) -> Fallout:
        return Fallout.deploy(from_=self.owner)
        
    def check_lv02(self, contract: Fallout):
        self.check_attacker_is(contract.owner())
        print("Level 02 passed.")

    #################### LEVEL 03 ####################

    def deploy_lv03(self) -> CoinFlip:
        return CoinFlip.deploy(from_=self.owner)
        
    def check_lv03(self, contract: CoinFlip):
        assert contract.consecutiveWins() >= 10, "You must guess right at least 10 times in row."
        print("You guessed it right 10 times consecutively, impressive!")
        print("Level 03 passed")

    #################### LEVEL 04 ####################
    
    def deploy_lv04(self) -> Telephone:
        return Telephone.deploy(from_=self.owner)
        
    def check_lv04(self, contract: Telephone):
        self.check_attacker_is(contract.owner())
        print("Level 04 passed.")

    #################### LEVEL 05 ####################
    
    def deploy_lv05(self) -> Token:
        contract = Token.deploy(1000, from_=self.owner)        # owner deploys the contract
        contract.transfer(self.attacker, 20, from_=self.owner) # owner gives you 20 tokens to start with
        return contract
        
    def check_lv05(self, contract: Token):
        balance = contract.balanceOf(self.attacker)
        print(f"You obtained {balance} tokens.")
        assert balance >= 1020, "You must steal at least 1020 tokens."
        if balance == 115792089237316195423570985008687907853269984665640564039457584007913129639935:
            print("Nicely done, you took maximum amout of tokens possible.")
        elif balance >= 10000:
            print("Wait, where did you get so many tokens?!")
        print("Level 05 passed.")

    #################### LEVEL 06 ####################
    
    def deploy_lv06(self) -> Delegation:
        delegate = Delegate.deploy(self.owner, from_=self.owner)     # first deploy the delegate
        return Delegation.deploy(delegate.address, from_=self.owner) # than deploy the delegation with address to delegate 

    def check_lv06(self, contract: Delegation):
        self.check_attacker_is(contract.owner())
        print("Level 06 passed")

    #################### LEVEL 07 ####################

    def deploy_lv07(self) -> Force:
        return Force.deploy(from_=self.owner)

    def check_lv07(self, contract: Force):
        assert contract.balance > 0, "You must force the cat to take some Ether."
        print("Wait... How did you force the cat to take it?!")
        print("Level 07 passed")

    #################### LEVEL 08 ####################
    
    def deploy_lv08(self) -> Vault:
        vault_key = ''.join(random.choice(string.ascii_letters + string.digits) for i in range(32))
        return Vault.deploy(bytes32(bytes(vault_key, "ascii")), from_=self.owner)

    def check_lv08(self, contract: Vault):
        assert contract.locked() == False, "You must unlock the vault."
        print("Your lockpicking skills are almost as good as LockPickingLawyer's.")
        print("Level 08 passed")

    #################### LEVEL 09 ####################
    
    def deploy_lv09(self) -> King:
        return King.deploy(from_=self.owner, value=1 * 10**18)

    def check_lv09(self, contract: King, newOvner: Address):
        assert contract._king() == newOvner, "You must take the kingship."
        print("You are the king now.")
        assert contract.balance <= 10 * 10**18, "You can't use more than 10 Ether"
        try:
            with must_revert():
                contract.transact(value=10_000 * 10**18, from_=self.owner)
            print("Did you really declined 10 000 Ether for the throne?!")
            print("Level 09 passed")
        except:
            raise AssertionError("The kingship was taken from you - you did not break the game.")

    #################### LEVEL 10 ####################
    
    def deploy_lv10(self) -> Reentrance:
        contract = Reentrance.deploy(from_=self.owner)
        contract.transact(value=5 * 10**18, from_=self.owner)
        contract.donate(self.other_account, from_=self.owner, value=1 * 10**18)
        contract.donate(self.owner, from_=self.owner, value=3 * 10**18)
        contract.withdraw(2 * 10**18, from_=self.owner)
        return contract

    def check_lv10(self, contract: Reentrance):
        assert contract.balance == 0, "You must withdraw all funds."
        print("You have taken what wasn't meant for you! Well done!")
        print("Level 10 passed")

    #################### LEVEL 11 ####################
    
    def deploy_lv11(self) -> Elevator:
        return Elevator.deploy(from_=self.owner)

    def check_lv11(self, contract: Elevator):
        assert contract.top(), "You must reach the top with this elevator."
        print("That's some suspicious implementation of a building ...")
        print("Level 11 passed")

    #################### LEVEL 12 ####################
    
    def deploy_lv12(self) -> Privacy:
        some_data = List3([random.randbytes(32), random.randbytes(32), random.randbytes(32)])
        return Privacy.deploy(some_data, from_=self.owner)

    def check_lv12(self, contract: Privacy):
        assert contract.locked() == False, "You must unlock this contract."
        print("Well done! You proved, no data can be hidden on blockchain.")
        print("Level 12 passed")

    #################### LEVEL 13 ####################

    def deploy_lv13(self) -> GatekeeperOne:
        return GatekeeperOne.deploy(from_= self.owner)
        
    def check_lv13(self, contract: GatekeeperOne):
        self.check_attacker_is_entrant(contract.entrant())
        print("Well done! Your hacker skills are on the rise!")
        print("Level 13 passed")

    #################### LEVEL 14 ####################

    def deploy_lv14(self) -> GatekeeperTwo:
        return GatekeeperTwo.deploy(from_= self.owner)
        
    def check_lv14(self, contract: GatekeeperTwo):
        self.check_attacker_is_entrant(contract.entrant())
        print("You are becoming good at bribing these gatekeepers.")
        print("Level 14 passed")

    #################### LEVEL 15 ####################
    
    def deploy_lv15(self) -> NaughtCoin:
        return NaughtCoin.deploy(_player= self.attacker, from_=self.owner)
        
    def check_lv15(self, contract: NaughtCoin):
        assert contract.balanceOf(self.attacker.address) == 0, "You must withdraw all your assets."
        print("Nice! You figured out some features of ERC20")
        print("Level 15 passed")

    #################### LEVEL 16 ####################

    def deploy_lv16(self) -> Preservation:
        library1 = LibraryContract.deploy(from_=self.owner)
        library2 = LibraryContract.deploy(from_=self.owner)
        return Preservation.deploy(library1, library2, from_=self.owner)

    def check_lv16(self, contract: Preservation):
        self.check_attacker_is(contract.owner())
        print("Gotcha! You are becoming really good in understanding delegate calls.")
        print("Level 16 passed")

    #################### LEVEL 17 ####################
    
    def deploy_lv17(self) -> Recovery:
        contract = Recovery.deploy(from_=self.owner)
        contract.generateToken(_name = "UKN", _initialSupply = 1000, from_=self.owner)
        return contract

    def check_lv17(self, contract: Recovery, lostAddress: Address):
        assert get_create_address(contract.address, contract.nonce-1) == lostAddress, "You must find the lost address."
        print("Well done! You are a big fan of Yellow paper!")
        print("Level 17 passed") 

    #################### LEVEL 18 ####################

    def deploy_lv18(self) -> MagicNum:
        return MagicNum.deploy(from_=self.owner)

    def check_lv18(self, contract: MagicNum):
        encodedCall = Abi.encode_with_signature("whatIsTheMeaningOfLife()", [], [])
        resultEncodedCall = Account(contract.solver(), self.chain).call(data=encodedCall)
        (decodedData,) = Abi.decode(data=resultEncodedCall,types=['uint256'])
        helper = CheckSizeContract.deploy()
        sizeCheck = helper.checkSize(contract.solver())
        assert sizeCheck <= 10, "Your contract must consist of maximum 10 opcodes."
        assert decodedData == 42, "Contract must receive '42' as the answer."
        print("Nice! You have talent to assembly!")
        print("Level 18 passed")

    #################### LEVEL 19 ####################
    
    def deploy_lv19(self) -> AlienCodex:
        # must be deployed from compiled source due to version unsupported by wake framework (lower than 0.6.2)
        source = Path(__file__).parent.parent / "bin" / "AlienCodex.bin"
        bytecode_for_lv19 = bytes.fromhex(source.read_text())
        deployer = Deployer.deploy()
        return AlienCodex(deployer.deployCode(bytecode_for_lv19).return_value)
        
    def check_lv19(self, contract: AlienCodex):
        self.check_attacker_is(contract.owner())
        print("Congratulations! You really become good at overflows/underflows.")
        print("Level 19 passed")

    #################### LEVEL 20 ####################
    
    def deploy_lv20(self) -> Denial:
        contract = Denial.deploy(from_=self.owner)
        contract.transact(value=10 * 10**18, from_=self.owner)
        contract.setWithdrawPartner(self.owner)
        return contract

    def check_lv20(self, contract: Denial):
        balance_before_withdraw = self.owner.balance
        contract.withdraw()
        assert balance_before_withdraw == self.owner.balance, "You must deny the owner from withdrawing funds."
        print("Good! You drained all available gas for transaction.")
        print("Level 20 passed")

    #################### LEVEL 21 ####################
    
    def deploy_lv21(self) -> Shop:
        return Shop.deploy(from_=self.owner)
    
    def check_lv21(self, contract: Shop):
        assert (contract.isSold() == False), "Product has not been bought!"
        assert (contract.price() == 100), "The price changed during the purchase."
        print("Nicely Done! You have deceived the shop.")
        print("Level 21 passed")

    #################### LEVEL 22 ####################

    def deploy_lv22(self) -> Dex:
        dex = Dex.deploy(from_=self.owner)
        token1 = SwappableToken.deploy(dex.address, "Token 1", "TKN1", 110, from_=self.owner)
        token2 = SwappableToken.deploy(dex.address, "Token 2", "TKN2", 110, from_=self.owner)
        dex.setTokens(token1.address, token2.address, from_=self.owner)
        dex.approve(dex.address, 100, from_=self.owner)
        dex.addLiquidity(token1.address, 100, from_=self.owner)
        dex.addLiquidity(token2.address, 100, from_=self.owner)
        token1.transfer(self.attacker, 10, from_=self.owner)
        token2.transfer(self.attacker, 10, from_=self.owner)
        return dex

    def check_lv22(self, contract: Dex):
        print("DEX's balance: \n\tToken1: ", contract.balanceOf(contract.token1(), contract.address), "\n\tToken2: ", contract.balanceOf(contract.token2(), contract.address))
        assert (contract.balanceOf(contract.token1(), contract.address) == 0 or contract.balanceOf(contract.token2(), contract.address) == 0), "You must drain all the Tokens 1 or all the Tokens 2."
        print("Well done! You are one stop closer to become DeFi master.")
        print("Level 22 passed")

    #################### LEVEL 23 ####################

    def deploy_lv23(self) -> DexTwo:
        dex = DexTwo.deploy(from_=self.owner)
        token1 = SwappableTokenTwo.deploy(dex.address, "Token 1", "TKN1", 110, from_=self.owner)
        token2 = SwappableTokenTwo.deploy(dex.address, "Token 2", "TKN2", 110, from_=self.owner)
        dex.setTokens(token1.address, token2.address, from_=self.owner)
        dex.approve(dex.address, 100, from_=self.owner)
        dex.add_liquidity(token1.address, 100, from_=self.owner)
        dex.add_liquidity(token2.address, 100, from_=self.owner)
        token1.transfer(self.attacker, 10, from_=self.owner)
        token2.transfer(self.attacker, 10, from_=self.owner)
        return dex
    
    def check_lv23(self, contract: DexTwo):
        print("DEX's balance: \n\tToken1: ", contract.balanceOf(contract.token1(), contract.address), "\n\tToken2: ", contract.balanceOf(contract.token2(), contract.address))
        assert (contract.balanceOf(contract.token1(), contract.address) == 0 and contract.balanceOf(contract.token2(), contract.address) == 0), "You must drain all the Tokens 1 and all the Tokens 2."
        print("Perfectly performed heist! You robbed the DEX to the last penny.")
        print("Level 23 passed")

    #################### LEVEL 24 ####################
    
    def deploy_lv24(self) -> PuzzleProxy:
        wallet_logic = PuzzleWallet.deploy(from_=self.owner)
        data = Abi.encode_with_selector(PuzzleWallet.init.selector, ['uint256'], [0]) 
        proxy = PuzzleProxy.deploy(self.owner.address, wallet_logic.address, data, from_=self.owner)
        instance = PuzzleWallet(proxy.address)
        instance.addToWhitelist(self.owner.address, from_=self.owner)
        instance.deposit(value=10 * 10**18, from_=self.owner)
        return proxy
        
    def check_lv24(self, contract: PuzzleProxy):
        self.check_attacker_is(contract.admin(), "You must become the admin of the wallet.", "You are the admin now.")
        assert contract.balance == 0, "You must drain all funds from the puzzle wallet."
        print("Beautiful pickpocket! You disintegrated the puzzle wallet into the puzzle pieces.")
        print("Level 24 passed")

    #################### LEVEL 25 ####################
    
    def deploy_lv25(self) -> Motorbike:
        engine = Engine.deploy(from_=self.owner.address)
        ForceTransfer.deploy(engine.address, value=10 * 10**18, from_=self.owner.address)
        return Motorbike.deploy(_logic=engine.address, from_=self.owner.address)

    def check_lv25(self, contract: Motorbike):
        implementation_slot = 0x360894a13ba1a3210667c828492db98dca3e2076cc3735a920a3ca505d382bbc
        (logic_contract, ) = Abi.decode(['address'], self.chain.chain_interface.get_storage_at(str(contract.address), implementation_slot))
        engine = Engine(logic_contract)

        assert engine.upgrader() == self.attacker.address, "You must became the upgrader off the engine to be able to remove it."
        assert engine.balance == 0, "You must selfdestruct the engine and drain all it's Ether gas."
        assert self.attacker.balance == 20 * 10**18, "Do not spend the Ether gas yet!"
        print("You are such a great technic! The motorbike is no longer able to drive.")
        print("Level 25 passed")

    #################### LEVEL 26 ####################

    def deploy_lv26(self) -> DoubleEntryPoint:
        old_legacy_token = LegacyToken.deploy(from_=self.owner)
        forta = Forta.deploy(from_=self.owner)
        crypto_vault = CryptoVault.deploy(self.owner.address, from_=self.owner)
        new_token = DoubleEntryPoint.deploy(old_legacy_token.address, crypto_vault.address, forta.address, self.attacker.address, from_=self.owner)
        crypto_vault.setUnderlying(new_token.address, from_=self.owner)
        old_legacy_token.delegateToNewContract(DelegateERC20(new_token), from_=self.owner)
        old_legacy_token.mint(crypto_vault.address, 100 * 10**18, from_=self.owner)
        return new_token

    def check_lv26(self, contract: DoubleEntryPoint):
        forta = contract.forta()
        vault = CryptoVault(contract.cryptoVault())
        detection_bot = forta.usersDetectionBots(self.attacker).address
        assert detection_bot != 0, "You must set Detection Bot."
        try:
            with must_revert():
                legacy_token = contract.delegatedFrom()
                vault.sweepToken(legacy_token)
        except:
            raise AssertionError("You must protect the vault - DoubleEntryPoint tokens can't be swept.")
        assert contract.balanceOf(contract.cryptoVault()) > 0, "You must protect the vault, but it's DoubleEntryPoint token balance is 0."
        print("Level 26 passed.")

    #################### LEVEL 27 ####################
    
    def deploy_lv27(self) -> GoodSamaritan:
        return GoodSamaritan.deploy(from_=self.owner)

    def check_lv27(self, contract: GoodSamaritan):
        assert contract.coin().balances(contract.wallet()) == 0, "You must drain good samaritan's wallet entirely."
        print("Wait, you only requested 10 tokens, don't ya?!!")
        print("Level 27 passed")

    #################### LEVEL 28 ####################

    def deploy_lv28(self) -> GatekeeperThree:
        return GatekeeperThree.deploy(from_=self.owner)

    def check_lv28(self, contract: GatekeeperThree):
        self.check_attacker_is_entrant(contract.entrant())
        print("Your are becomming a gatekeeper yourself ...")
        print("Level 28 passed")

    #################### LEVEL 29 ####################

    def deploy_lv29(self) -> Switch:
        return Switch.deploy(from_=self.owner)
  
    def check_lv29(self, contract: Switch):
        assert contract.switchOn() == True, "You must turn the switch on."
        print("You have turned the switch on.")
        print("Level 29 passed")

    #################### LEVEL 30 ####################

    def deploy_lv30(self) -> HigherOrder:
        return HigherOrder.deploy(from_=self.owner)
        
    def check_lv30(self, contract: HigherOrder):
        self.check_attacker_is(contract.commander(), "You must become the Commander of the Higher Order.", "You are now the Commander of the Higher Order.")
        print("Extraordinary! You proved you belong to the members of the Higher Order.")
        print("Level 30 passed")

    #################### LEVEL 31 ####################

    def deploy_lv31(self) -> Stake:
        weth = DefaultERC20.deploy("Dummy WETH", "WETH")
        return Stake.deploy(weth)
        
    def check_lv31(self, contract: Stake):
        assert contract.balance != 0, "The Stake contract's ETH balance has to be greater than 0"
        assert contract.totalStaked() > contract.balance, "totalStaked must be greater than the Stake contract's ETH balance"
        assert contract.Stakers(self.attacker), "You must be a staker."
        assert contract.UserStake(self.attacker) == 0, "Your staked balance must be 0."
        print("Level 31 passed")

    #################### LEVEL 32 ####################
    # TODO Copy this template when adding new level

    def deploy_lv32(self):
        return
        
    def check_lv32(self, contract):
        print("Level 32 passed")
