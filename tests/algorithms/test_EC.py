
from jose.jwk import ECKey
from jose.exceptions import JOSEError

import ecdsa
import pytest


@pytest.fixture
def alg():
    return ECKey(ECKey.SHA256)

private_key = """-----BEGIN EC PRIVATE KEY-----
MHQCAQEEIIAK499svJugZZfsTsgL2tc7kH/CpzQbkr4g55CEWQyPoAcGBSuBBAAK
oUQDQgAEsOnVqWVPfjte2nI0Ay3oTZVehCUtH66nJM8z6flUluHxhLG8ZTTCkJAZ
W6xQdXHfqGUy3Dx40NDhgTaM8xAdSw==
-----END EC PRIVATE KEY-----"""


class TestECAlgorithm:

    def test_EC_key(self, alg):
        key = ecdsa.SigningKey.from_pem(private_key)
        alg.prepare_key(key)

    def test_string_secret(self, alg):
        key = 'secret'
        with pytest.raises(JOSEError):
            alg.prepare_key(key)

    def test_object(self, alg):
        key = object()
        with pytest.raises(JOSEError):
            alg.prepare_key(key)
