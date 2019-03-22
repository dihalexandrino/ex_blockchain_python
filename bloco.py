class Bloco:

  def __init__(self, transactions, prev_hash):
    self.transactions = transactions
    self.prev_hash = prev_hash
    self.nonce = 0
    self.timestamp = datetime.now()
    self.hash = self.gerar_hash()
 
  def gerar_hash(self):
    bloco_top = str(self.time_stamp) + str(self.transactions) +str(self.prev_hash) + str(self.nonce)
    hash_do_bloco = sha256(bloco_top.encode())
    return hash_do_bloco.hexdigest()
