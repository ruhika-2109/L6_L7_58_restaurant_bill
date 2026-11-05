
import pytest
from restaurant_bill import bill_total, split_bill, table_wait


# ========== BILL TOTAL: BRANCH TESTS ==========

def test_valid_section():
    assert bill_total("dine_in", 1000, 2, False) == 1155


def test_invalid_section():
    with pytest.raises(ValueError, match="unknown section"):
        bill_total("invalid", 1000, 2, False)


def test_negative_food_total():
    with pytest.raises(ValueError, match="invalid order"):
        bill_total("dine_in", -100, 2, False)


def test_zero_guests():
    with pytest.raises(ValueError, match="invalid order"):
        bill_total("dine_in", 1000, 0, False)


def test_happy_hour_applied():
    assert bill_total("dine_in", 1000, 2, True) == 924


def test_happy_hour_not_applied():
    assert bill_total("dine_in", 1000, 2, False) == 1155


def test_takeaway_excluded_from_happy_hour():
    assert bill_total("takeaway", 1000, 2, True) == 1050


def test_rooftop_service_charge():
    assert bill_total("rooftop", 1000, 2, False) == 1207


def test_large_group_extra_service():
    assert bill_total("dine_in", 1000, 8, False) == 1365


def test_group_below_eight():
    assert bill_total("dine_in", 1000, 7, False) == 1155


# ========== SPLIT BILL: BRANCH TESTS ==========

def test_invalid_people():
    with pytest.raises(ValueError, match="invalid people count"):
        split_bill(1000, 0, 10)


def test_valid_people():
    assert split_bill(1000, 4, 10) == 275


def test_negative_tip():
    with pytest.raises(ValueError, match="invalid tip"):
        split_bill(1000, 4, -5)


def test_zero_tip():
    assert split_bill(1000, 4, 0) == 250


def test_exact_bill_split():
    assert split_bill(1000, 4, 10) == 275


def test_bill_split_with_remainder():
    assert split_bill(1000, 3, 0) == 334


# ========== TABLE WAIT: BRANCH TESTS ==========

def test_party_over_twelve():
    assert table_wait(13, 5, False) == "call ahead"


def test_party_within_limit():
    assert table_wait(4, 5, False) == "seat now"


def test_reservation_available():
    assert table_wait(4, 0, True) == "seat now"


def test_no_reservation_no_tables():
    assert table_wait(4, 0, False) == "waitlist"


def test_large_party_only_one_table():
    assert table_wait(8, 1, False) == "waitlist"


def test_large_party_two_tables():
    assert table_wait(8, 2, False) == "seat now"


def test_small_party_one_table():
    assert table_wait(4, 1, False) == "seat now"
