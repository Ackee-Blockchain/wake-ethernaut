from wake.testing import *
from tests.level_service import LevelService
from pytypes.contracts.i00_hello import Tutorial


@default_chain.connect()
def test_level_00():
    service = LevelService(default_chain)
    contract = service.deploy_level_00()
    do_level_00_solution(contract)
    service.check_level_00(contract)

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
