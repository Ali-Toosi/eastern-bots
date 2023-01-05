.. _opanonbot_contributing:

Contributing to Opanon Bot
=====================================

Here is a list of features you can start working on:

- Add feature to unblock users after they are blocked
- Allow users to have multiple codes and delete them separately
- Allow replying to messages (the message id needs to be stored next to the chat code)
- Feature to choose protecting your messages (send message with protect_content attribute to the API) to prevent saving
- Right now the bot works in 2 languages under 2 different bot accounts but they share the data (the chat links). This
can be changed by adding the bot username to the ChatCode model.
