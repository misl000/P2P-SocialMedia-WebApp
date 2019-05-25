import urllib.request
import json
import base64
import nacl.encoding
import nacl.signing
import time

class Login(object):

    #def authenticate(self,username,password):
        url = "http://cs302.kiwi.land/api/report"

        #STUDENT TO UPDATE THESE...
        username = "misl000"
        password = "misl000_171902940"

        publicKey = ""
        signatureTemp = ""
        signature = ""
        #password = "misl000_171902940"
        #Public key =
        # Signature - calculate
        # SendSig = signature
        signing_key = nacl.signing.SigningKey.generate()
        verify_key = signing_key.verify_key
        verify_key_hex = verify_key.encode(encoder=nacl.encoding.HexEncoder)
        publicKey = verify_key_hex.decode('utf-8')
        signatureMessage = bytes(publicKey + username, encoding = 'utf-8')
        signedMessage = signing_key.sign(signatureMessage, encoder=nacl.encoding.HexEncoder)
        signature_str = signedMessage.signature.decode('utf-8')


        # create HTTP BASIC authorization header
        credentials = ('%s:%s' % (username, password))
        b64_credentials = base64.b64encode(credentials.encode('ascii'))
        headers = {
            'Authorization': 'Basic %s' % b64_credentials.decode('ascii'),
            'Content-Type': 'application/json; charset=utf-8',

            
        }

        payload = {
            "connection_address": "202.36.244.134",
            "connection_location": "2",
            "incoming_pubkey":"c852f14e5c063da1dbedb7fa0d6cc9e4d6f61e581140b4ae2f46cddd67556d48"


            # STUDENT TO COMPLETE THIS...
        }

        # STUDENT TO COMPLETE:
        # 1. convert the payload into json representation,
        payload_str = json.dumps(payload)
        # 2. ensure the payload is in bytes, not a string
        json_payload = payload_str.encode('utf-8')

        # 3. pass the payload bytes into this function
        try:
            req = urllib.request.Request(url, data=json_payload, headers=headers)
            response = urllib.request.urlopen(req)
            data = response.read()  # read the received bytes
            # load encoding if possible (default to utf-8)
            encoding = response.info().get_content_charset('utf-8')
            response.close()
        except urllib.error.HTTPError as error:
            print(error.read())
            exit()

        JSON_object = json.loads(data.decode(encoding))
        print(JSON_object)
