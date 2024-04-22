from typing import List

class Level:
    def __init__(self, **kwargs):
        self.name = kwargs.get('name')
        self.created = kwargs.get('created')
        self.difficulty = int(kwargs.get('difficulty'))
        self.description = kwargs.get('description')
        self.completed_description = kwargs.get('completedDescription')
        self.level_contract = kwargs.get('levelContract')
        self.instance_contract = kwargs.get('instanceContract')
        self.reveal_code = kwargs.get('revealCode')
        self.deploy_params = kwargs.get('deployParams')
        self.deploy_funds = kwargs.get('deployFunds')
        self.deploy_id = kwargs.get('deployId')
        self.instance_gas = kwargs.get('instanceGas')
        self.author = kwargs.get('author')
