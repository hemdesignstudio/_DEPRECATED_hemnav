"""Sales Order Module

"""
from ..base import NAVBase

SERVICE_NAME = "SalesOrderWS"


class SalesOrder(NAVBase):
    """Class handles creation and quering of data from
    NAV (Sales Order) soap service

    """

    def __init__(self, region):
        """Method initializes a soap zeep client for Sales Order by
        utilizing parent class (NAVbase)
        """

        super().__init__(region, SERVICE_NAME, False)

    def create(self, sales_order):
        """
        Args:
            sales_order (dict): NAV SalesOrder to be created
        Returns:
            dict: The newly created order
        Raises:
            Fault: Zeep Faults in case of exceptions
        """
        return self._client.service.Create(sales_order)
