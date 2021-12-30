from ags import bykey,byplace
import pytest

def test_bykey():
    assert bykey('07138041') ==  ["07138041", "Linz am Rhein, Stadt"]