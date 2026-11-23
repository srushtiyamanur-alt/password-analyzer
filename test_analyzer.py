import pytest
from analyzer import check_length, character_variety_score, calculate_entropy, strength_rating

def test_check_length_valid():
    assert check_length("Secure123") is True

def test_check_length_short():
    assert check_length("abc12") is False

def test_variety_score_all_types():
    assert character_variety_score("Abc123!@") == 4

def test_variety_score_only_lowercase():
    assert character_variety_score("password") == 1

def test_entropy_empty():
    assert calculate_entropy("") == 0.0

def test_entropy_calculation():
    assert calculate_entropy("abcd") == 18.8

def test_strength_rating_strong():
    assert strength_rating("Str0ng!Pass#2026") == "Strong"

def test_strength_rating_weak():
    assert strength_rating("12345") == "Weak"
