import os
import json

from beyondtrust_agent import controller
import logging
from http.server import HTTPServer, CGIHTTPRequestHandler


def main():

    """
    Main function
    """
    secrets = controller.get_secrets()
    print(secrets)
    secrets_json = json.loads(secrets)
    # for k, v in secrets_json.items():
    #     print(k, v)
    print(secrets_json["Quasys"]["beyondtrust"]["Password"])
    server_object = HTTPServer(server_address=('', 8080), RequestHandlerClass=CGIHTTPRequestHandler)
    server_object.serve_forever()

if __name__ == "__main__":
    main()