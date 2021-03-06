import pytest
from django.urls import reverse

@pytest.fixture
def resp(client, db):
    return client.get(reverse('cadastro:setor'))

def test_setor_page(resp):
    assert resp.status_code == 200