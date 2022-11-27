.. _new_bots_requirements:

New Bots Requirements
=====================

General Requirements
---------------------------------

If you would like to add a new bot to this repo, your bot needs to have a few simple requirements:

-   | It should be implemented using `aiogram <https://github.com/aiogram/aiogram>`_. This way, each bot will
        be an independent app and they will all use the same design. Hence, it will be easier for people to work on other bots in the
        repo too.
-   | It should be useful for a group of people, not just you. The goal of this project is to be a repository of small
        bots that are useful for the public (or a subset of the public) so when a bot is added, there would be other
        developers seeing a point in working on it.
-   | It should be following a basic set of good development practices, so others won't find it impossible to extend your
        bot. Check out technical requirements below.

Technical Requirements
-----------------------------------

In order for your bot to be added to the repo, it must have:

-   | Working unit tests. Ideally, these tests cover most of the functionalities so if someone else changes your code,
        they can see if they are breaking anything.
-   | Your bot needs to have documentation. Follow the other bots in the repo as examples. Make sure you explain what the
        bot does and how it can be used in your index and, how others can contribute in a *contributing.rst* file.
