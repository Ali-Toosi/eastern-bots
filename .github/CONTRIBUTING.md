# Contributing to Eastern Bots

Each bot has its own list of features that can be worked on. You can find these in [here](../docs/bots). Each bot has a
`contributing.rst` doc.

Alternatively, if you want to work on something related to the project itself and not the individual bots, here is a
list of things you can work on:

- Add some "Telegram Update Factories" so bots can be unit tested easily with different scenarios/updates.
- Cleanup [pipeline file](workflows/ci.yml) and put the deploy commands into a separate script.
- Document usage of [setup_bot](../eastern_bots/utils/management/commands/setup_bot.py) command somewhere.
