from decimal import Decimal

from bracketeering.brackets import calculate_tax
from bracketeering.domain import FilingStatus


def test_some_brackets():
    assert calculate_tax(Decimal(0), 2022, FilingStatus.SINGLE) == 0
    assert calculate_tax(Decimal(10000), 2022, FilingStatus.SINGLE) == 1000
    assert calculate_tax(Decimal(20000), 2022, FilingStatus.SINGLE) == 1027.5 + (20000 - 10275) * 0.12
    assert calculate_tax(Decimal(50000), 2022, FilingStatus.SINGLE) == 1027.5 + (41775 - 10275) * 0.12 + (50000 - 41775) * 0.22

    assert calculate_tax(Decimal(0), 2022, FilingStatus.MARRIED_FILING_JOINTLY) == 0
    assert calculate_tax(Decimal(20000), 2022, FilingStatus.MARRIED_FILING_JOINTLY) == 2000
