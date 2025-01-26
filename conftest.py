import pytest


@pytest.fixture(scope="session")
def django_db_setup():
    """
    No-op database setup so that the integration tests can use the production database.
    """
    pass
    # settings.DATABASES['default'] = {
    #     'ENGINE': 'django.db.backends.mysql',
    #     'HOST': 'db.example.com',
    #     'NAME': 'external_db',
    # }
