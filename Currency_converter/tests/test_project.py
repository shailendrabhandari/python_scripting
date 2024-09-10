# This is the test file for pytest
import pytest
from project import get_conversion_rate, convert_currency

# Test Function 1: Test if the conversion rate is fetched correctly
def test_get_conversion_rate(monkeypatch):
    def mock_get(url):
        class MockResponse:
            @staticmethod
            def json():
                return {
                    'conversion_rates': {
                        'EUR': 0.85,
                        'USD': 1.0
                    }
                }
            status_code = 200
        return MockResponse()

    monkeypatch.setattr('requests.get', mock_get)
    assert get_conversion_rate('USD', 'EUR') == 0.85

# Test Function 2: Test if the currency conversion is calculated correctly
def test_convert_currency(monkeypatch):
    def mock_get(url):
        class MockResponse:
            @staticmethod
            def json():
                return {
                    'conversion_rates': {
                        'EUR': 0.85,
                        'USD': 1.0
                    }
                }
            status_code = 200
        return MockResponse()

    monkeypatch.setattr('requests.get', mock_get)
    assert convert_currency('USD', 'EUR', 100) == 85.0

# Additional test cases can be added for different currency pairs
