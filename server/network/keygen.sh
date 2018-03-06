mkdir keys
openssl genpkey -algorithm RSA -out private.pem -pkeyopt rsa_keygen_bits:2048
openssl rsa -in private.pem -outform PEM -pubout -out ./keys/public.pem
openssl rsa -in private.pem -out ./keys/private_unencrypted.pem -outform PEM


