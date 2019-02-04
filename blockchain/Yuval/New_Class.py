
class Book_Transaction:
  def __init__(self, time, moneyin: int, moneyout: int, balance: int, txid: str, block: int):
    self.time = time
    self.moneyin = moneyin
    self.moneyout = moneyout
    self.balance = balance
    self.txid = txid
    self.block = block

  @property
  def set_balance(self,balance):
      self.balance = balance


class PageBook:
  def __init__(self,address: str,final_balance: int,n_tx:int, total_received: int,total_sent:int, t: [Book_Transaction]):
    list1 = []
    for i in t:
        list1.append(i)
    self.transactions = list1
    self.address = address
    self.final_balance = final_balance
    self.n_tx = n_tx
    self.total_received = total_received
    self.total_sent = total_sent

  def set_final_balance(self):
      if len(self.transactions) == 0:
          pass
      else:
          self.final_balance = getattr(self.transactions[-1],'balance')

  def set_n_tx(self):
      self.n_tx = len(self.transactions)

  def set_total_received(self):
      x = 0
      for i in self.transactions:
          x += i.moneyin
      self.total_received = x

  def set_total_sent(self):
      x = 0
      for i in self.transactions:
          x += i.moneyout
      self.set_total_sent = x

  def __str__(self):
    return self.address

  @property
  def update_balance(newt: [Book_Transaction]):
      for i in newt.transactions:
          subtotal = 0
          try:
              subtotal += i.moneyin - i.moneyout
              i.set_balance(subtotal)
          except Exception:
              pass
      return newt

