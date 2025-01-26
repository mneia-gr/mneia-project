import pytest
from mneia_backend.models.link import Link


@pytest.mark.django_db
def test_link_attribute_count():
    """
    Integration test to compare the `attribute_count` field on the Link model with the count of attributes in the
    database.
    """
    for link in Link.objects.all():
        print(f"Link {link.id} attribute_count: {link.attribute_count} calculated: {link.calculated_attribute_count}")
        assert link.attribute_count == link.calculated_attribute_count
