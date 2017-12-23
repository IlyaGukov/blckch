class Miner:
    def __init__(self):
        self.blockchain = []
        self.transactions = set([])
		self.block = []
	def verify_tnx(self,tnx):
		if tnx['value'] > 0:
			if tnx['event'].not_past == True:
				if tnx['signature']# is valid...
					return True
				else: return False
			else: return False
		else: return False
		
	def add_tnx(self):
		tnx = Txm_pool.pop()
		if verify_tnx() == True:
			self.block.append(tnx)
	
    def verify_block(self, block):
        for tnx in block:
		
    def mine(self):
		self.blockchain.append(self.block)
		self.block = []