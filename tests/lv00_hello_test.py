from wake.testing import *
from tests.ethernaut_deployer import EthernautDeployer
from pytypes.contracts.lv00_hello import Tutorial


@default_chain.connect()
def test_level_00():
    service = EthernautDeployer(default_chain)
    contract = service.deploy_lv00()
    do_level_00_solution(contract)
    service.check_lv00(contract)

def do_level_00_solution(contract: Tutorial):
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
