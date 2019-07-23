""" Inventory Module

"""
from ..base import NAVBase
import datetime

SERVICE_NAME = "GetInventory"


class Inventory(NAVBase):
    """Class handles creation and quering of data from
    NAV (Inventory) soap service

    """

    def __init__(self, region):
        """Method initializes a soap zeep client for Inventory by
        utilizing parent class (NAVbase)
        """

        super().__init__(region, SERVICE_NAME)

    def get(self, sku=None):
        """Get the virtual inventory for a particular sku with the start date as the day when the
        function is called
        Args:
            sku (string, numeric): Product sku
        Returns:
            list: list of available quantities at different dates
        Raises:
            Fault: Zeep Faults in case of exceptions
        """
        return self._client.service.GetInventory(
            itemFilter=sku,
            startDate=datetime.datetime.now().strftime("%Y-%m-%d"),
            categoryFilter="",
            retValues={},
        )
