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

TDLPL currently recognizes Python, Ruby, PHP, C and JavaScript.
Adding new languages is really easy: edit the GNUmakefile to add the
corresponding rule that prepares the runnable file. The runnable file goes
into the run/ directory. Finally, create its sample configuration file under
config-samples/.

At this state the project only has basic start challenges. More should come
in a few months... sooner if you help me out!
To create a new challenge create a test under the test/ directory and add it
to the CHALLENGES variable to the GNUmakefile. Make sure you insert it in an
appropriate place according to the challenge difficulty.

If you are interested in extending TDLPL to support another language, you might
want to take a look at commit
*[e6dbd04087](https://github.com/alvarezp/tdlpl/commit/e6dbd04087efe0a4e545365b5f9ea94d408ed7e2)*.

If you are interested in extending TDLPL to include a new challenge, you might
want to take a look at commit
*[69124344c7](https://github.com/alvarezp/tdlpl/commit/69124344c75e7778bd5b85a70c4dcd1ded7cb521)*.

Enjoy!
