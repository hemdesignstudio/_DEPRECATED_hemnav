# -*- coding: utf-8 -*-
"""VAT Business posting Group Module


"""
from hemnav.base import NAVBase

SERVICE_NAME = "VatBusinessPostingGroups"


class VatBusinessPostingGroup(NAVBase):
    """Class handles creation and quering of data from
    NAV (VatBusinessPostingGroups) soap service

    """

    def __init__(self, region):
        """Method initializes a soap zeep client for customer card by
        utilizing parent class (NAVbase)
        """

        super().__init__(region, SERVICE_NAME, False)

    def create_if_missing(self, tax_group_name) -> dict:
        """Method gets a list of tax groups by zipcode and in case of there are not
        groups it creates a group instead.

        Args:
            tax_group_name (str): Tax group name.

        Returns:
            dict: if groups are returned from nav,
            else it creates a group and no return.
        """

        groups = self._where({"Code": tax_group_name})
        if groups:
            return groups[0]
        else:
            self._create({"Code": tax_group_name})
