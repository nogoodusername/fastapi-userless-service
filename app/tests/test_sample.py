from app.api.sample_module.sample_api import sample_data_read


def test_sample_data_read() -> None:
    id = 1
    result = sample_data_read(1)
    assert isinstance(result, dict)
    assert result.get("item_id") == id
