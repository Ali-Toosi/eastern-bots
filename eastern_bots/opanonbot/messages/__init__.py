from collections import defaultdict

from . import en, fa

bot_map = {
    "opanonbot": en.Messages,
    "nashenasbot": fa.Messages,
    "botdevtestbot": en.Messages,
}


class Union(en.Messages):
    def __init__(self, **messages):
        self.__dict__.update(messages)


# Merge messages across all langs into one object
messages_dict = defaultdict(list)
for lang in [en, fa]:
    for message_key in dir(lang.Messages):
        if not message_key.startswith("_") and isinstance(
            getattr(lang.Messages, message_key), str
        ):
            messages_dict[message_key].append(getattr(lang.Messages, message_key))

union: en.Messages = Union(**messages_dict)
