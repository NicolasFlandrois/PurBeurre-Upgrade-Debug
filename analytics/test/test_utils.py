# from django.test import TestCase
import urllib.request
import json
from io import BytesIO

from analytics.utils import get_client_ip

# Mock Testing Client's IP


def test_get_client_ip(monkeypatch):
    request = {'HTTP_X_FORWARDED_FOR': "123.4.5.6"}

    def mockreturn(request):
        return BytesIO(json.dumps(results, sort_keys=True, indent=4,
                                  separators=(',', ': ')).encode())

    monkeypatch.setattr(urllib.request, 'urlopen', mockreturn)

    test_IP = "123.4.5.6"

    assert test_IP == get_client_ip(request)
