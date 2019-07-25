import yaml, os
from dotenv import load_dotenv
from enum import Enum


class RegionEnum(Enum):
    EU = "eu"
    US = "us"


class Settings:
    """Settings module for NAV Base wrapper
    """

    def __init__(self, region):
        """
        Args:
            region (RegionEnum): NAV region config
        Raises:
            AttributeError: In case of wrong region
        """
        yaml_doc = open("config.yml", "r")
        config = yaml.load(yaml_doc, Loader=yaml.FullLoader)
        yaml_doc.close()

        load_dotenv(".env")
        environment = os.environ["ENV"].lower()

        self.nav_username = os.environ["NAV_USERNAME"]
        self.nav_password = os.environ["NAV_PASSWORD"]
        self.base_url = config[environment]["base_url"]
        self.store_name = config[environment][region.value]["store_name"].replace(
            " ", "%20"
        )
