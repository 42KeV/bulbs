## What is Bulbs?
Bulbs is an open source message board developed in Python using the Pyramid Web Framework. 

Bulbs was first conceived when Jeff, the Sun God called upon TazG the Destroyer to create a forum that would rival the security and flexibility of the Great Gossamer Forum (GGF). Deep in our hearts we knew that such a thing would be no easy task, but regardless of jeff's unshakable feeling that TazG wouldn't have the skill or patience required to finish such a task, he took the challenge and even allowed Jeff to help with the production of the software - particularily in regards to the front-end design, which I must say was superb. TazG worked tirelessly for about 19 hours a day on the Bulbs project, 1 week in his morale was low and his patience all but gone; he was getting nowhere. The man who thought he knew it all was defeated, and so he locked up Bulbs' source, copied it onto a floppy drive and threw the drive into the deep pits of hell. Bulbs was dead.

A year later, jeff decided to create his own version of Bulbs. A harder, better, faster, stronger version of Bulbs. This resurrection of a dead forum engine, who was abused by its previous maintainer came after the founder(s) of New Free Games Forum grew tired of using the ravaged perl monstrosity known as Gossamer Forum. In a drunken rage Bulbs was reborn and a large shadow cast upon Gossamer Forum; it has finally met a true rival, one that wouldn't be so easily defeated. 

## Requirements
* Python 3.4+
* Pyramid
* PostgreSQL

## How to install
* Clone the repository, `git clone https://github.com/galileo94/bulbs.git`

Switch into your virtual environment

* `python setup.py develop` to install the package and dependencies
* `pthon setup.py configure` to configure database information

If nothing exploded, you should be ready to rock and roll

* `pserve development.ini --reload` to start the server in development mode and automatically reload files as you change them. It is not recommended to use the reload argument in production environments.
