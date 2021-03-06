opencast
========

A tool to generate formal requirements documents from a RedMine issue tracker. It is primarily aimed at enabling:
	(1) Import of issues from external tabular formats, and
	(2) Export of issues to documents for external (traditional) reporting, e.g. LaTeX and Wordprocessor formats.


Setup the VirtualEnv
====================
Decide where you want to store your virtualenv. I use a folder in my project root named $PROJECT.env, so if opencast is stored in projects/opencast then the virtualenv is in projects/opencast/opencast.env/

You can now create a virtualenv for opencast using the following command in /projects/opencast/:

    $ virtualenv --no-site-packages --distribute opencast.env && source opencast.env/bin/activate && pip install -r opencast.env/requirements.txt


Run the Code
============
To run the Test Suite:

    $ PYTHONPATH=`pwd`/src python test/test_opencast.py

To run opencast:

    $ PYTHONPATH=`pwd`/src python src/main.py

Even better, export the opencast src dir onto your PYTHONPATH. Assuming that you are in the opencast project root dir:

    $ export PYTHONPATH=`pwd`/src

You should now be able to execute:

    $ python test/test_opencast.py

& see the output from the unittests.