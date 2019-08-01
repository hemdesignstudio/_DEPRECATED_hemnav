from unittest import TestCase
from hemnav.code_units.inventory import Inventory
from hemnav.settings import RegionEnum


class InventoryTestCase(TestCase):
    def test_get(self):
        # Test Invetory get function
        inventory = Inventory(RegionEnum.EU)

        # Product that does not exist
        product = inventory.get("doesnotexist")
        self.assertIsNone(product)

        # Product that does exist
        product = inventory.get("50042")
        self.assertIsNotNone(product)
