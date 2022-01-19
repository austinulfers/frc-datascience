import base64
import argparse

# Create a function where a user passes in a string on the command line and the
# string is encoded in base64 and printed in the terminal


def base64_encode(string: str):
    encoded_string = base64.b64encode(string.encode("utf-8"))
    print(encoded_string.decode("utf-8"))


parser = argparse.ArgumentParser(description="Encode a string in base64")
parser.add_argument("--string", "-s", help="String to encode")
args = parser.parse_args()
base64_encode(args.string)
