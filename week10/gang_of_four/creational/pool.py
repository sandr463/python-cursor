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


if __name__ == "__main__":

    configs_pool = ConfigPool()
    configs_pool.init_configs()

    config = configs_pool.get_config()

    print(f"First config id {id(config)}")

    second_config = configs_pool.get_config()
    print(f"Second config id {id(second_config)}")

    print(f"First config state {config.state}")
    config.state = 1

    third_config = configs_pool.get_config()
    print(f"Third config id {id(third_config)}")
    print(f"First config state {third_config.state}")

    print(f"Is third and first object the same {config is third_config}")