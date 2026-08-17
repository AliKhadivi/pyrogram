from pyrogram import Client


def test_jalgo_desktop_connection_metadata_defaults():
    client = Client("test", api_id=1, api_hash="0" * 32, in_memory=True)

    try:
        assert client.app_version.startswith("Jalgo Desktop ")
        assert client.device_model == "Jalgo Desktop"
        assert client.system_version
        assert "Python" not in client.device_model
        assert "Pyrogram" not in client.app_version
    finally:
        client.executor.shutdown(wait=False)


def test_connection_metadata_can_be_overridden():
    client = Client(
        "test-custom",
        api_id=1,
        api_hash="0" * 32,
        in_memory=True,
        app_version="Custom App 1.0",
        device_model="Custom Device",
        system_version="Custom OS"
    )

    try:
        assert client.app_version == "Custom App 1.0"
        assert client.device_model == "Custom Device"
        assert client.system_version == "Custom OS"
    finally:
        client.executor.shutdown(wait=False)
