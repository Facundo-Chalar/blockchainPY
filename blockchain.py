class Blockchain(object):
	def __init__(self):
		self.chain= []
		self.current_transactions = []

		#Crear bloque genesis
		self.new_block(previous_hash=1, proof=100)

		def new_block(self, proof, previous_hash=None):
			#Crea nuevo bloque y lo agrega a la cadena
			block ={
				'index': len(self.chain + 1),
				'timestamp': time(),
				'transactions': self.current_transactions,
				'proof': proof,
				'previous_hash': previous_hash or self.hash(self.chan[-1]),
			}

		def new_transaction(self, sender, recipient, amount):
			#Agrega una nueva transaccion a la lista

			self.current_transactions.append({
				'sender': sender,
				'recipient': recipient,
				'amount': amount,
				})
			
			return self.last_block['index'] + 1

		@staticmethod
		def hash(block):
				#Hashea un bloque
				pass

		@property

		def last_block(self):
			#Returns the last Block in the chain
			pass