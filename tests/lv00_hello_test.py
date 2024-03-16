from wake.testing import *
from tests.ethernaut_deployer import EthernautDeployer
from pytypes.contracts.lv00_hello import Tutorial


@default_chain.connect()
def test_level_00():
    ethernaut = EthernautDeployer(default_chain)
    contract = ethernaut.deploy_lv00()
    exploit_level_00(contract)
    ethernaut.check_lv00(contract)

def exploit_level_00(contract: Tutorial):
    # Training: simple method calling
    print(contract.info())
    print(contract.info1())
    print(contract.info2("hello"))
    print(contract.infoNum())
    print(contract.info42())
    print(contract.theMethodName())
    print(contract.method7123949())
    print(contract.password())

    contract.authenticate(contract.password())
