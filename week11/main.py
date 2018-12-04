import argparse
import sys

from no_sql.redis.redis_handler import RedisHandler

dbs = {"redis": RedisHandler}


def validate_command(value):
    if value in ["add", "get", "delete"]:
        return value
    else:
        raise ValueError


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Our first script')
    # parser.add_argument('-st', '--storage', help='Name of storage', required=True)
    parser.add_argument('-ht', '--host', dest="host", default="localhost")
    parser.add_argument('-pt', '--port', dest="port", default=6379)
    parser.add_argument('-db', '--db', dest="db", default=0)
    parser.add_argument('--command', type=validate_command, dest="command", help="Possible choises [add, save, delete]")
    parser.add_argument('--key', dest="key")
    parser.add_argument('--value', dest="value")

    args = parser.parse_args()

    r = RedisHandler(host=args.host, port=args.port, db=args.db)

    if args.command == "add":
        r.conn.set(args.key, args.value)
        print("Successfully add new value to redis")
        sys.exit(0)
