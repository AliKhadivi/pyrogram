import asyncio

from pyrogram import Client


def make_client(name: str, **kwargs) -> tuple[Client, asyncio.AbstractEventLoop]:
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    return Client(name, api_id=1, api_hash="0" * 32, in_memory=True, **kwargs), loop


def close_client(client: Client, loop: asyncio.AbstractEventLoop) -> None:
    client.executor.shutdown(wait=False)
    asyncio.set_event_loop(None)
    loop.close()


def test_jalgo_desktop_connection_metadata_defaults():
    client, loop = make_client("test")

    try:
        assert client.app_version.startswith("Jalgo Desktop ")
        assert client.device_model == "Jalgo Desktop"
        assert client.system_version
        assert "Python" not in client.device_model
        assert "Pyrogram" not in client.app_version
    finally:
        close_client(client, loop)


def test_connection_metadata_can_be_overridden():
    client, loop = make_client(
        "test-custom",
        app_version="Custom App 1.0",
        device_model="Custom Device",
        system_version="Custom OS"
    )

    try:
        assert client.app_version == "Custom App 1.0"
        assert client.device_model == "Custom Device"
        assert client.system_version == "Custom OS"
    finally:
        close_client(client, loop)
