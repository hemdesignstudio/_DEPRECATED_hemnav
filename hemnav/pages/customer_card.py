# -*- coding: utf-8 -*-
"""Customer Card Updater Module
Module is updates customer cards with new Tax groups
"""

from hemnav.base import NAVBase

SERVICE_NAME = "CustomerCardWS"


class CustomerCard(NAVBase):
    """Class extends base class (NAVbase) which creates
    a soap zeep client for customer card
    """

    def __init__(self, region):
        """Method initializes a soap zeep client for customer card by
        utilizing parent class (NAVbase)

        """
        super().__init__(region, SERVICE_NAME, False)

    def update_tax_group(self, zip_code, new_tax_group):
        """Update customer card with with correct tax group

        Args:
            zip_code (str, numeric): Zip code to update tax group on
            new_tax_group (str): The new tax group
        """

        customer_cards = self._where({"Post_Code": zip_code})

        if customer_cards:
            for card in customer_cards:
                card["VAT_Bus_Posting_Group"] = new_tax_group

            return self._update_multiple(customer_cards)
