import hashlib
import requests

from Crypto.PublicKey import RSA 
from Crypto.Signature import PKCS1_v1_5 
from Crypto.Hash import SHA256 
from base64 import b64encode, b64decode 

class Networking():

    def __init__(self, remote_addr, keyfile='./keys/private_unencrypted.pem'):

        self.remote_addr = remote_addr
        kf = open(keyfile)
        self.key = kf.read()
        kf.close()

    def make_signature(self, inp):

        #Let's load our private key
        key = self.key
        rsakey = RSA.importKey(key) 
        signer = PKCS1_v1_5.new(rsakey) 
        digest = SHA256.new()

        #Let's hash the idx and sign it
        digest.update(b64decode(inp))
        signature = signer.sign(digest)         
        
        return signature


    def send_order(self, file_name, idx=None, extra_data={}):

        #Let's make id
        if idx == None:
            idx = hashlib.sha224(file_name.encode('utf8')).hexdigest()

        #Let's make a signature
        signature = self.make_signature(idx)

        #Let's POST
        files = {'payload': open(file_name, 'rb')}
        response = requests.post(self.remote_addr + 'upload/'+str(idx), files=files, data={'signature': b64encode(signature)})

        return response

def test():

    nn = Networking('http://127.0.0.1:5000/')
    nn.send_order('public.pem')

if __name__ == '__main__':
    test()







