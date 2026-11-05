
import pytest
from restaurant_bill import bill_total, split_bill, table_wait


# ========== BILL TOTAL TESTS ==========

def test_invalid_section():
    with pytest.raises(ValueError, match="unknown section"):
        bill_total("invalid", 1000, 2, False)


def test_negative_food_total():
    with pytest.raises(ValueError, match="invalid order"):
        bill_total("dine_in", -100, 2, False)


def test_invalid_guest_count():
    with pytest.raises(ValueError, match="invalid order"):
        bill_total("dine_in", 1000, 0, False)


def test_happy_hour_discount():
    assert bill_total("dine_in", 1000, 2, True) == 924


def test_takeaway_during_happy_hour():
    assert bill_total("takeaway", 1000, 2, True) == 1050


def test_rooftop_large_group():
    assert bill_total("rooftop", 1000, 8, False) == 1417


# ========== SPLIT BILL TESTS ==========

def test_invalid_people_count():
    with pytest.raises(ValueError, match="invalid people count"):
        split_bill(1000, 0, 10)


def test_negative_tip():
    with pytest.raises(ValueError, match="invalid tip"):
        split_bill(1000, 4, -5)


def test_split_with_remainder():
    assert split_bill(1000, 3, 0) == 334


# ========== TABLE WAIT TESTS ==========

def test_large_party():
    assert table_wait(13, 5, False) == "call ahead"


def test_reservation():
    assert table_wait(4, 0, True) == "seat now"


def test_no_free_tables():
    assert table_wait(4, 0, False) == "waitlist"


def test_large_party_limited_tables():
    assert table_wait(8, 1, False) == "waitlist"


def test_normal_seating():
    assert table_wait(4, 2, False) == "seat now"
