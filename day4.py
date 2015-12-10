from hashlib import md5

key = 'ckczppom'


def mine(zeros):
    hash = ''
    nonce = 0
    while not hash.startswith('0'*zeros):
        nonce += 1
        hash = md5(key + str(nonce)).hexdigest()
    return nonce
# part 1
print mine(5)
#  part 2
print mine(6)
