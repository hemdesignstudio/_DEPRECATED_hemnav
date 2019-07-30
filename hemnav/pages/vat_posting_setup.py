# -*- coding: utf-8 -*-
"""VAT Posting Setup Module

"""
from hemnav.base import NAVBase

SERVICE_NAME = "VatPostingSetup"
US_SALES_TAX_ACCOUNT = 2310


class VatPostingSetup(NAVBase):
    """Class handles creation and quering of data from
    NAV (VatPostingSetup) soap service


    """

    def __init__(self, region):
        """Method initializes a soap zeep client for customer card by
        utilizing parent class (NAVbase)

        """
        super().__init__(region, SERVICE_NAME, False)

    def create_if_missing(self, tax_group_name, tax_group_vat) -> dict:
        """Method gets a list of "VAT posting setups" by their "tax groups" and in case
        of there are not "VAT posting setups" it creates a "VAT posting setup" instead.

        Args:
            tax_group_name (str): Tax group name
            tax_group_vat (str): Tax group vat

        Returns:
            dict: if groups are returned from nav,
            else it creates a posting setup and no return.
        """
        posting_setups = self._where({"VAT_Bus_Posting_Group": tax_group_name})

        if posting_setups:
            return posting_setups[0]
        else:
            return self._create(
                {
                    "VAT_Bus_Posting_Group": tax_group_name,
                    "VAT_Prod_Posting_Group": "STANDARD",
                    "VAT_Percent": tax_group_vat,
                    "VAT_Calculation_Type": "Normal_VAT",
                    "Sales_VAT_Account": US_SALES_TAX_ACCOUNT,
                    "Sales_VAT_Unreal_Account": US_SALES_TAX_ACCOUNT,
                    "EU_Service": False,
                }
            )
