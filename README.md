# Eastern Bots

[![Documentation Status](https://readthedocs.org/projects/eastern-bots/badge/?version=latest)](https://eastern-bots.readthedocs.io/en/latest/?badge=latest)
![CI Status](https://github.com/Ali-Toosi/eastern-bots/actions/workflows/ci.yml/badge.svg?event=push)

[Full Documentation](https://eastern-bots.readthedocs.io/en/latest/)

[Change Log](https://github.com/Ali-Toosi/eastern-bots/blob/main/CHANGELOG.md)

[Contributing](https://github.com/Ali-Toosi/eastern-bots/blob/main/.github/CONTRIBUTING.md)


A repo of Telegram bots created using [aiogram](https://github.com/aiogram/aiogram) which are handy to the
public. If you have a need for a bot, and think it is needed by others too, feel free to implement it and put it in
here.

## What is the point?

This is for developers who want to create something small that helps their lives easier, but do not want to do the
whole process of deploying and maintaining a repo for it. If that's you, you can put your bot in here and the overhead
work of deploying is already done. Additionally, you are putting your bot in front of the eyes of other like-minded
developers who might be able to improve it.

## How do I add my bot?

Open a pull request with your bot source code.

## Can I add _any_ bot?

No, not really. You can only add bots that are:
- Useful to the public. I.e. it doesn't solve a problem very specific to you, it solves a problem for a group of people.
- Implemented with [aiogram](https://github.com/aiogram/aiogram). We would like to be able to maintain each other's bots and some consistency in the source codes is required for that.
- Following a basic set of good development practices i.e. have unit tests, documentation, readable source codes, etc..

## Should I pay anything for my bot to be deployed?

No, all bots are deployed together and developers do not need to pay for it. If you would like to donate and support the project you can reach out to see how your help can make things easier.

## Wait... isn't this going kind of backwards by making a big monolith?

Good question. It could seem that way but here is what I think: since each bot is a separate app, this project would
be a big Django project where all apps are completely independent of each other - No inter-app imports or logical relations.
Which means, although they are all in the same repo, they are still very much separated. If at any point, any of these
bots are too popular that they cannot be hosted alongside other bots, or are malfunctioning and need to be removed,
they can be immediately removed from this project and be deployed separately. Let's have a chat if you do not agree with the sentiment.

## Okay, what about dependencies?

The repo uses dependabot and dependencies are meant to be updated all the time. I expect most bots not to need a pinned
version of a dependency and be able to update but, it is understandable that sometimes some dependencies cannot be used
with their new version. However, it's not feasible for anyone to test all the bots when an update is about to happen.
This means, it is very important to have unit tests if you can so if an update breaks your bot, we would not go through
with it. If you have better ways of testing bots with new versions, please let us know.
