TDLPL
=====

*Test-Driven Learning Programming Languages* is a set of programming challenges
for people that already know programming but want to learn a new language.

How to use
==========

Clone the repository with:

`git clone https://github.com/alvarezp/tdlpl.git`

Make sure you GNU Make is installed, then just run

`make`

You might need to run `gmake` on non-GNU or non-Linux systems.

Current state
=============

TDLPL currently recognizes two programming languages: Python and Ruby.
Adding new languages is really easy: edit the GNUmakefile to add the
corresponding rule that prepares the runnable file. The runnable file goes
into the run/ directory. Announce the new supported language in
test/messages/welcome.

At this state the project only has basic start challenges. More should come
in a few months... sooner if you help me out!
To create a new challenge create a test under the test/ directory and add it
to the CHALLENGES variable to the GNUmakefile. Make sure you insert it in an
appropriate place according to the challenge difficulty.

Enjoy!
