import os
from flask import Flask, request, redirect, url_for, send_from_directory, safe_join, jsonify

from Crypto.PublicKey import RSA 
from Crypto.Signature import PKCS1_v1_5 
from Crypto.Hash import SHA256 
from base64 import b64encode, b64decode 

app = Flask(__name__)

@app.route('/upload/<idx>', methods=['POST'])
def upload_file(idx):

    kf = open('./keys/public.pem')

    signature = b64decode(request.form['signature'])
    key = RSA.importKey(kf.read())
    kf.close()

    verifier = PKCS1_v1_5.new(key)

    digest = SHA256.new()
    digest.update(b64decode(idx))

    #If signature matches
    if verifier.verify(digest, signature):

        #The file
        f = request.files['payload']

        #Check that the path is safe
        path = safe_join('./soundfiles/' + str(idx))

        #Save it to the disk
        f.save(path)

        return jsonify(True)
    else:
        return jsonify(False)

if __name__ == '__main__':
    app.run()
