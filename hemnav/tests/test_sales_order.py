from unittest import TestCase
from hemnav.pages.sales_order import SalesOrder
from hemnav.settings import RegionEnum
from zeep.exceptions import Fault

TEST_DOCUMENT_NO = "TEST_SALES_ORDER"


class SalesOrderTestCase(TestCase):
    def test_where(self):
        # On something that exists
        sales_order_client = SalesOrder(RegionEnum.EU)
        order = sales_order_client._where({"No": 180905})
        self.assertIsNotNone(order)

        # On something that does not exist
        order = sales_order_client._where({"No": "doesnotexist"})
        self.assertIsNone(order)

        # On a faulty field
        with self.assertRaises(Fault):
            order = sales_order_client._where({"WrongFieldName": ""})

    def test_get_create_and_delete(self):
        sales_order_client = SalesOrder(RegionEnum.EU)

        try:
            # See if the test order exists
            sales_order_client._get({"No": TEST_DOCUMENT_NO})
        except Exception:
            # Order did not exist. Creating it
            created_order = sales_order_client._create(
                {"No": TEST_DOCUMENT_NO}
            )
            self.assertIsNotNone(created_order)

        # Try to fetch it now
        fetched_order = sales_order_client._get({"No": TEST_DOCUMENT_NO})
        self.assertIsNotNone(fetched_order)

        # Delete order
        deleted_order = sales_order_client._delete(fetched_order["Key"])
        self.assertTrue(deleted_order)

        # Make sure order is deleted
        with self.assertRaises(Exception):
            sales_order_client._get({"No": TEST_DOCUMENT_NO})
