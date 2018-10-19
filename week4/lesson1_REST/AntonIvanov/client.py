import requests as rq
import json

if __name__ == "__main__":
    serv_set = json.load(open("settings.json", "r"))
    url = f"http://{serv_set['host']}:{serv_set['port']}/user/denis"
    res = rq.get(url)
    print(res)
    if res.status_code < 500:
        print(f"Server: http://{serv_set['host']}:{serv_set['port']} is alive!")
    else:
        print(f"Server: http://{serv_set['host']}:{serv_set['port']} is die!")