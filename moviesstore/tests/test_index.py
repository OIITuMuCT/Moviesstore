import pytest
from django.urls import reverse

def test_index_view(client):
    """
    Tests the Home page view to ensure it returns a 200 OK status.
    """
    url = reverse('home.index')  # Assuming your homepage URL is named 'homepage'
    response = client.get(url)
    assert response.status_code == 200
    # Optional: Assert specific content in the response
    assert b"Welcome to the Home Page" in response.content

def test_about_view(client):
    """
    Tests the About page view to ensure it returns a 200 OK status.
    """
    url = reverse('home.about')
    response = client.get(url)
    assert response.status_code == 200
