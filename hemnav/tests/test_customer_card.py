from unittest import TestCase
from hemnav.pages.customer_card import CustomerCard
from hemnav.pages.vat_business_posting_group import VatBusinessPostingGroup
from hemnav.settings import RegionEnum
import random
import string


def random_string(stringLength=10):
    """Generate a random string of fixed length """
    letters = string.ascii_lowercase
    return "".join(random.choice(letters) for i in range(stringLength))


ZIP_CODE_WITHOUT_CUSTOMERS = "60701"
ZIP_CODE_WITH_CUSTOMERS = "116 35"
NEW_TAX_GROUP = random_string()


class CustomerCardTestCase(TestCase):
    def setUp(self):
        # Create tax group in nav
        tax_group_client = VatBusinessPostingGroup(RegionEnum.EU)
        tax_group_client.create_if_missing(NEW_TAX_GROUP)

    def tearDown(self):
        # Remove tax group again after tests
        tax_group_client = VatBusinessPostingGroup(RegionEnum.EU)
        tax_group = tax_group_client.create_if_missing(NEW_TAX_GROUP)
        tax_group_client._delete(tax_group["Key"])

    def test_update_tax_group(self):
        customer_card_updater = CustomerCard(RegionEnum.EU)
        updated_cards = customer_card_updater.update_tax_group(
            ZIP_CODE_WITHOUT_CUSTOMERS, NEW_TAX_GROUP
        )
        self.assertIsNone(updated_cards)

        updated_cards = customer_card_updater.update_tax_group(
            ZIP_CODE_WITH_CUSTOMERS, NEW_TAX_GROUP
        )
        self.assertIsNotNone(updated_cards)
