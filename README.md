opencast
========

A tool to generate formal requirements documents from a RedMine issue tracker. It is primarily aimed at enabling:
	(1) Import of issues from external tabular formats, and
	(2) Export of issues to documents for external (traditional) reporting, e.g. LaTeX and Wordprocessor formats.


Setup the VirtualEnv
====================
Decide where you want to store your virtualenv. I use a hidden (dotfile) alongside my project repo, so if moot is stored in the projects/moot then the virtualenv is in projects/.moot

You can now create a virtualenv for moot using:

    $ virtualenv --no-site-packages --distribute .moot && source .moot/bin/activate && pip install -r moot/requirements.txt
