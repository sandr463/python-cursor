import sys

try:
    import redis
except ImportError:
    print("No install please redis package")
    sys.exit(0)


if __name__ == "__main__":
    print("Yes all fine")
