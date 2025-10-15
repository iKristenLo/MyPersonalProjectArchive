import time
from hashlib import sha256
maxnonce = 1000000000
def f_sha256(text):
  return sha256(text.encode("ascii")). hexdigest()


def mine(blocknumber,transaction,previoushash,prefixzero):
  prefixstring = "0" * prefixzero
  for nonce in range(maxnonce):
    text = str(blocknumber + transaction + previoushash + str(nonce))
    newhash = f_sha256(text)
    if newhash.startswith(prefixstring):
      print("Coin_Mined!")
      return(newhash)
  return BaseException("UnableToMine")



#Demo
if __name__ == "__main__":
  transaction = []
  diffuculty = 4
  start = time.time()
  print("startMining")
  newhash = mine(5,prefixzero,transaction,diffuculty)
  totaltime = str((time.time()- start))
  print("nMining" ,totaltime)
  print(newhash)