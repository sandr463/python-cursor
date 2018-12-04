from __future__ import annotations

from typing import List


class ConfigPool:
    __configs: List[Config] = []
    __max_configs = 5

    def init_configs(self):
        for _ in range(self.__max_configs):
            self.__configs.append(Config())

    def get_config(self):
        for config in self.__configs:
            if config.state:
                config.state = 0
                return config
        else:
            raise Exception("No configs are availabe")


class Config:
    state = 1


class MultitoneConfig:
    __count = 0
    __max_count = 3

    def __new__(cls, *args, **kwargs):
        print("Method __new__ is calling")
        # if Config.__instance is None:
        #     print("We have no inst yet")
        #     cls.__instance = super().__new__(cls)
        # else:
        #     print("Return old one")
        # return cls.__instance
        if cls.__count < cls.__max_count:
            cls.__count += 1
            return super().__new__(cls)
        else:
            raise Exception("Too much objects")

    def __init__(self):
        print("Method init is calling")

class OrdinaryConfig:
    pass


if __name__ == "__main__":
    first_conf = Config()
    second_conf = Config()
    third_conf = Config()
    fourth_conf = Config()
    # ord_conf_first = OrdinaryConfig()
    # ord_conf_second = OrdinaryConfig()
    # print(first_conf is second_conf)
    # print(id(first_conf) == id(second_conf))
    # print(id(first_conf))
    # print(id(second_conf))

    # nd_conf)
    # print(id(ord_conf_first) == id(ord_conf_second))
    # print(id(ord_conf_first))
    # print(id(ord_conf_second))