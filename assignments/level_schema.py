from typing import List

class Level:
    def __init__(self, **kwargs):
        self.name = str(kwargs.get('name'))
        self.created = str(kwargs.get('created'))
        self.difficulty = int(kwargs.get('difficulty'))
        self.description = str(kwargs.get('description'))
        self.completed_description = str(kwargs.get('completedDescription'))
        self.level_contract = str(kwargs.get('levelContract'))
        self.instance_contract = str(kwargs.get('instanceContract'))
        self.reveal_code = kwargs.get('revealCode')
        self.deploy_params = kwargs.get('deployParams')
        self.deploy_funds = kwargs.get('deployFunds')
        self.deploy_id = str(kwargs.get('deployId'))
        self.instance_gas = kwargs.get('instanceGas')
        self.author = str(kwargs.get('author'))
