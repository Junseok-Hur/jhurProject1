import school_api


def test_get_data():
    data = school_api.get_data()
    assert len(data) > 3000
