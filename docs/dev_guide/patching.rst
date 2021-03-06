Patching Cheetah
================


How to commit changes to git, or submit patches, or send pull requests,
how to run the test suite. Describe distutils and how the regression tests
work.

File Requirements
-----------------


The code{Template} class contains not only the Cheetah
infrastructure, but also some convenience methods useful in all
templates. More methods may be added if it's generally agreed among
Cheetah developers that the method is sufficiently useful to all
types of templates, or at least to all types of HTML-output
templates. If a method is too long to fit into {Template} -
especially if it has helper methods - put it in a mixin class under
{Cheetah.Utils} and inherit it.

Routines for a specific problem domain should be put under
{Cheetah.Tools}, so that it doesn't clutter the namespace unless
the user asks for it.

Remember: {Cheetah.Utils} is for objects required by any part of
Cheetah's core. {Cheetah.Tools} is for completely optional objects.
It should always be possible to delete {Cheetah.Tools} without
breaking Cheetah's core services.

If a core method needs to look up an attribute defined under
{Cheetah.Tools}, it should use {hasattr()} and gracefully provide a
default if the attribute does not exist (meaning the user has not
imported that subsystem).

Testing Changes and Building Regression Tests
---------------------------------------------


Cheetah ships with a regression test suite. To run the built-in
tests, execute at the shell prompt:

::

        cheetah test

To run the test suite with all supported Python versions use ``tox``.

Before checking any changes in, run the tests and verify they all
pass. That way, users can check out the git version of Cheetah at
any time with a fairly high confidence that it will work. If you
fix a bug or add a feature, please take the time to add a test that
exploits the bug/feature. This will help in the future, to prevent
somebody else from breaking it again without realizing it. Users
can also run the test suite to verify all the features work on
their particular platform and computer.

The general procedure for modifying Cheetah is as follows:


#. Write a simple Python program that exploits the bug/feature
   you're working on. You can either write a regression test (see
   below), or a separate program that writes the template output to
   one file and put the expected output in another file; then you can
   run {diff} on the two outputs. ({diff} is a utility included on all
   Unix-like systems. It shows the differences between two files line
   by line. A precompiled Windows version is at
   http://gnuwin32.sourceforge.net/packages/diffutils.htm, and MacOS
   sources at
   http://perso.wanadoo.fr/gilles.depeyrot/DevTools\_en.html.)

#. Make the change in your Cheetah git sandbox or in your installed
   version of Cheetah. If you make it in the sandbox, you'll have to
   run {python setup.py install} before testing it. If you make it in
   the installed version, do { not} run the installer or it will
   overwrite your changes!

#. Run {cheetah test} to verify you didn't break anything. Then run
   your little test program.

#. Repeat steps 2-3 until everything is correct.

#. Turn your little program into a regression test as described
   below.

#. When {cheetah test} runs cleanly with your regression test
   included, update the {docs/news.rst} file and check in your changes. If
   you made the changes in your installed copy of Cheetah, you'll have
   to copy them back into the git sandbox first. If you added any
   files that must be distributed, { be sure to} {cvs add} them before
   committing. Otherwise Cheetah will run fine on your computer but
   fail on anybody else's, and the test suite can't check for this.

#. Announce the change on the cheetahtemplate-discuss list and
   provide a tutorial if necessary. The documentation maintainer will
   update the Users' Guide and Developers' Guide based on this message
   and on the changelog.


If you add a directory to Cheetah, you have to mention it in
{setup.py} or it won't be installed.

The tests are in the {Cheetah.Tests} package, aka the {Cheetah/Tests/}
directory of your git sandbox. Most of the tests are in
{SyntaxAndOutput.py}. You can either run all the tests or choose
which to run:

    Run all the tests. (Equivalent to {cheetah test}.)

    Run only the tests in that module.

    Run only the tests in the class {CGI} inside the module. The class
    must be a direct or indirect subclass of
    {unittest\_local\_copy.TestCase}.

    Run the tests in classes {CGI} and {Indenter}.

    Run only test {test1}, which is a method in the {CGI} class.


To make a SyntaxAndOutput test, first see if your test logically
fits into one of the existing classes. If so, simply add a method;
e.g., {test16}. The method should not require any arguments except
{self}, and should call {.verify(source, expectedOutput)}, where
the two arguments are a template definition string and a control
string. The tester will complain if the template output does not
match the control string. You have a wide variety of placeholder
variables to choose from, anything that's included in the
{defaultTestNameSpace} global dictionary. If that's not enough, add
items to the dictionary, but please keep it from being cluttered
with wordy esoteric items for a single test).

If your test logically belongs in a separate class, create a
subclass of {OutputTest}. You do not need to do anything else; the
test suite will automatically find your class in the module. Having
a separate class allows you to define state variables needed by
your tests (see the {CGI} class) or override {.searchList()} (see
the {Indenter} class) to provide your own searchList.

To modify another test module or create your own test module,
you'll have to study the existing modules, the
{unittest\_local\_copy} source, and the {unittest} documentation in
the Python Library Reference. Note that we are using a hacked
version of {unittest} to make a more convenient test structure for
Cheetah. The differences between {unittest\_local\_copy} and
Python's standard {unittest} are documented at the top of the
module.


