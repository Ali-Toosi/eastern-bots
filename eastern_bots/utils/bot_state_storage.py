from typing import Any, cast

from aiogram import Bot
from aiogram.fsm.state import State
from aiogram.fsm.storage.base import BaseStorage, StateType, StorageKey
from django.core.cache import cache


def rep_key(key: StorageKey, sub_key="state"):
    return f"{str(key.bot_id)}:{str(key.user_id)}:{str(key.chat_id)}:{sub_key}"


class DjangoCacheStorage(BaseStorage):
    def __init__(self, state_ttl=None, data_ttl=None):
        super().__init__()
        self.state_ttl = state_ttl
        self.data_ttl = data_ttl

    def get_and_decode(self, key: StorageKey, sub_key: str):
        value = cache.get(rep_key(key, sub_key))
        if isinstance(value, bytes):
            value = value.decode("utf-8")
        return value

    async def set_state(
        self, bot: Bot, key: StorageKey, state: StateType = None
    ) -> None:
        key_str = rep_key(key, "state")
        if state is None:
            cache.delete(key_str)
        else:
            cache.set(
                key_str,
                cast(str, state.state if isinstance(state, State) else state),
                self.state_ttl,
            )

    async def get_state(self, bot: Bot, key: StorageKey) -> str:
        return self.get_and_decode(key, "state")

    async def set_data(self, bot: Bot, key: StorageKey, data: dict[str, Any]) -> None:
        key_str = rep_key(key, "data")
        if not data:
            cache.delete(key_str)
        else:
            cache.set(key_str, data, self.data_ttl)

    async def get_data(self, bot: Bot, key: StorageKey) -> dict[str, Any]:
        return self.get_and_decode(key, "data")

    async def close(self) -> None:
        pass
