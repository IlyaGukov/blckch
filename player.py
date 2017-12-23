class Player:
    def __init__(self, name, p, balance):
        self.name = name
        key = GenerateKey(p)
        self.private_key = key.x
        self.public_key = key.p, key.g, key.y
        self.balance = balance
        self.token_balance = {}
    
    def get_balance(self):
        return self.balance
    
    def get_token_balance(self):
        return self.token_balance
    
    def set_token_balance(self,token):
        self.token_balance[token[0]] = token[1]
        
    def Bet(self, event,token,value):
        return Txm_pool.append({'value':value,'event':event,'token':token,'pubkey':pubkey,'signature':signature})