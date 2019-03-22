from bloco import Bloco

class Blockchain:
  def __init__(self):
    self.chain = []
    self.unconfirmed_transactions = []
    self.first_block()

  def genesis_block(self):
    transactions = []
    first_block = Bloco(transactions, "0")
    first_block.gerar_hash()
    self.chain.append(first_block)

  def add_block(self, transactions):
    prev_hash = (self.chain[len(self.chain)-1]).hash
    new_block = Bloco(transactions, prev_hash)
    new_block.gerar_hash()
    proof = self.proof_of_work(new_block)
    self.chain.append(new_block)
    return proof, new_block



  def validar_chain(self):
    for i in range(1, len(self.chain)):
      curr = self.chain[i]
      prev = self.chain[i-1]
      if(curr.hash != curr.gerar_hash()):
        return False

      if(current.prev_hash != prev.gerar_hash()):
       
        return False
    return True
  
  def proof_of_work(self, bloco, difficulty=2):
    proof = bloco.gerar_hash()
    while proof[:difficulty] != '0'*difficulty:
      bloco.nonce += 1
      proof = bloco.gerar_hash()
    bloco.nonce = 0
    return proof
