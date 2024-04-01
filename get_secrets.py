import os
import json

from beyondtrust_agent import controller
import logging
from http.server import HTTPServer, CGIHTTPRequestHandler

os.environ["SECRETS_PATH"] = "/Users/abdulmelikkalkan/tmp/beyond/secrets_files"
os.environ["BT_API_URL"] = "https://44.207.168.98:443/BeyondTrust/api/public/v3"
os.environ["BT_API_KEY"] = "c79488314430a91e477d32bad64278c007f3b2860712785d25082a8a430e3325b99fa2be60f7c0cb4c5bd289d5e591cf211d0bc235d1776390bb286dd7b69933;runas=abdulmelik;"
os.environ["FOLDER_LIST"] = "abdulmelik/Dev/"
os.environ["BT_VERIFY_CA"] = "False"


def main():

    """
    Main function
    """
    secrets = controller.get_secrets()
    print(secrets)
    secrets_json = json.loads(secrets)
    # for k, v in secrets_json.items():
    #     print(k, v)
    # print(secrets_json["Quasys"]["beyondtrust"]["Password"])
    server_object = HTTPServer(server_address=('', 8080), RequestHandlerClass=CGIHTTPRequestHandler)
    server_object.serve_forever()

if __name__ == "__main__":
    main()