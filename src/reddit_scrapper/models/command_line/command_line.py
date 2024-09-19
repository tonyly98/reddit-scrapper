import argparse

parser = argparse.ArgumentParser(
    description="Provide databack as json or sql"
)

parser.add_argument(
    "-data", "--datatype", metavar="datatype",
    required=True, help="Return as DB or json"
)

args = parser.parse_args()
s = "Hello {args.datatype}"
print(s)