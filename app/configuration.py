import logging
import os
from typing import Iterable, List, Tuple

from dotenv import find_dotenv, load_dotenv
from pydantic import BaseModel

logger = logging.getLogger(__name__)


class CORSConfiguration(BaseModel):
    allowed_hosts = str

    @property
    def allowed_origins(self) -> List[str]:
        return self.allowed_hosts.split(",")


class Configuration(BaseModel):
    environment: str
    cors: CORSConfiguration


def __set_hierarchical_key(config: dict, key_path: [str], value: str) -> None:
    path_length = len(key_path)
    key = key_path[0]

    if path_length == 1:
        config[key] = value
    else:
        nested_config = config.get(key)
        if not nested_config:
            nested_config = {}
            config[key] = nested_config
        __set_hierarchical_key(nested_config, key_path[1:], value)


def build_dict(params: Iterable[Tuple[str, str]], *, key_separator: str) -> dict:
    config = {}
    for key, value in params:
        key_path = key.lower().split(key_separator)
        __set_hierarchical_key(config, key_path, value)
    return config


def load_from_env(*, key_separator: str = ".") -> dict:
    dotenv_path = find_dotenv(usecwd=True)
    if dotenv_path:
        logger.info("Loading configuration from file %s", dotenv_path)
        load_dotenv(dotenv_path)
    return build_dict(os.environ.items(), key_separator=key_separator)


def load(
    service_name: str,
    key_separator: str = ".",
) -> dict:
    config = load_from_env(key_separator=key_separator)

    return config


configuration = Configuration.parse_obj(load("market-engine-api", key_separator="__"))
