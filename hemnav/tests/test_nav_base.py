from unittest import TestCase
from hemnav.base import NAVBase, RegionEnum
from doubles import allow, teardown
import zeep


class NAVBaseTestCase(TestCase):
    def test_region_parameter(self):
        wrapper = NAVBase(RegionEnum.EU, "GetInventory")
        self.assertEqual(wrapper._region, RegionEnum.EU)

        wrapper = NAVBase(RegionEnum.US, "GetInventory")
        self.assertEqual(wrapper._region, RegionEnum.US)

        with self.assertRaises(AttributeError):
            NAVBase(RegionEnum.UK, "")

    def test_service_name(self):
        allow(zeep).Client.and_return("")
        wrapper = NAVBase(RegionEnum.EU, "TestName")
        self.assertEqual(wrapper._service_name, "TestName")
        teardown()
