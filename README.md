# Bouncer Tests for http://bouncer-bouncer.stage.mozaws.net

This repository contains tests for Mozilla's [Bouncer website](https://wiki.mozilla.org/Bouncer).

[![license](https://img.shields.io/badge/license-MPL%202.0-blue.svg)](https://github.com/mozilla/bouncer-tests/blob/master/LICENSE)
[![travis](https://img.shields.io/travis/mozilla/bouncer-tests.svg?label=travis)](http://travis-ci.org/mozilla/bouncer-tests/)
[![stage](https://img.shields.io/jenkins/s/https/webqa-ci.mozilla.com/bouncer.stage.svg?label=stage)](https://webqa-ci.mozilla.com/job/bouncer.stage/)
[![prod](https://img.shields.io/jenkins/s/https/webqa-ci.mozilla.com/bouncer.prod.svg?label=prod)](https://webqa-ci.mozilla.com/job/bouncer.prod/)
[![requirements](https://img.shields.io/requires/github/mozilla/bouncer-tests.svg)](https://requires.io/github/mozilla/bouncer-tests/requirements/?branch=master)

## Getting involved
We love working with contributors to fill out the test coverage for Mozilla's
support website, but it does require a few skills. By contributing to our test
suite you will have an opportunity to learn and/or improve your skills with
Python, Selenium WebDriver, GitHub, virtual environments, the Page Object
Model, and more.

For some resources for learning about these technologies, take a look at our
documentation on [running Web QA automated tests][running-tests].

All of [these awesome contributors][contributors] have opened pull requests
against this repository.

## Questions are always welcome
While we take pains to keep our documentation updated, the best source of
information is those of us who work on the project. Don't be afraid to join us
in irc.mozilla.org [#mozwebqa][irc] to ask questions about our tests. We also
have a [mailing list][list] available that you are welcome to join and post to.

## How to run the tests locally
We maintain a [detailed guide][running-tests] to running our automated tests.
However, if you want to get started quickly, you can try following the steps
below:

### Clone the repository
If you have cloned this project already then you can skip this, otherwise you'll
need to clone this repo using Git. If you do not know how to clone a GitHub
repository, check out this [help page][git-clone] from GitHub.

If you think you would like to contribute to the tests by writing or maintaining
them in the future, it would be a good idea to create a fork of this repository
first, and then clone that. GitHub also has great documentation for
[forking a repository][git-fork].

### Create or activate a Python virtual environment
You should install this project's dependencies (which is described in the next
step) into a virtual environment in order to avoid impacting the rest of your
system, and to make problem solving easier. If you already have a virtual
environment for these tests, then you should activate it, otherwise you should
create a new one. For more information on working with virtual environments see
our [summary][virtualenv].

### Install dependencies
Install the Python packages that are needed to run our tests using pip. In a
terminal, from the the project root, issue the following command:

```bash
$ pip install -Ur requirements.txt
```

### Running tests locally

To run these tests, use:

```bash
py.test --baseurl="http://bouncer-bouncer.stage.mozaws.net" tests
```

Use `-k` to run a specific test. For example,

```bash
py.test -k test_that_checks_redirect_using_incorrect_query_values \
        --baseurl="http://bouncer-bouncer.stage.mozaws.net" tests
```

The mozwebqa plugin has advanced command line options for reporting and using browsers. To see the options available, try running:

```bash
py.test --help
```

Also see the documentation on davehunt's [pytest-mozwebqa](https://github.com/davehunt/pytest-mozwebqa) GitHub project page.

### `virtualenv` and `virtualenvwrapper` (optional, intermediate level)

While most of us have had some experience using virtual machines, [`virtualenv`](https://pypi.python.org/pypi/virtualenv) is something else entirely. It's used to keep libraries that you install from clashing and messing up your local environment. After installing `virtualenv`, installing [`virtualenvwrapper`](https://bitbucket.org/dhellmann/virtualenvwrapper) will give you some nice commands to use with `virtualenv`.

For a more detailed discussion of `virtualenv` and `virtualenvwrapper`, check out our [quick start guide](https://wiki.mozilla.org/QA/Execution/Web_Testing/Automation/Virtual_Environments) and also [this blog post](http://www.silverwareconsulting.com/index.cfm/2012/7/24/Getting-Started-with-virtualenv-and-virtualenvwrapper-in-Python).

### Moz-Grid-Config (optional, intermediate level)

Prerequisites: [Java Runtime Environment](http://www.oracle.com/technetwork/java/javase/downloads/), [Apache Ant](http://ant.apache.org/)

[Moz-Grid-Config](https://github.com/mozilla/moz-grid-config) is a project containing our Selenium Grid configuration. It uses Apache Ant to run the Selenium hub or node to the configuration defined in the yaml files.

We recommend git cloning the repository for a couple of reasons:

1. The commands to launch a node or hub are all pre-configured and as simple as typing `ant launch-hub` or `ant launch-node`
2. The paths to browser binaries and nodes can be stored in configuration (yaml) files
3. It contains a jar file of the latest Selenium in it's lib directory

(If you prefer to download Selenium it's own, you can do that from [here](https://code.google.com/p/selenium/downloads/list))

You will need to make sure that the name of your Firefox application matches one of the names in `moz-grid-config/grid_configuration.yml`.  As an example:  even though Firefox typically installs without a version number in the name, `moz-grid-config` requires it to be named `Firefox <version number>.app` on OS X.

## Writing tests

If you want to get involved and add more tests then there's just a few things we'd like to ask you to do:

1. Use an existing file from this repository as a template for all new tests and page objects
2. Follow our simple [style guide](https://wiki.mozilla.org/QA/Execution/Web_Testing/Docs/Automation/StyleGuide)
3. Fork this project with your own GitHub account
4. Add your test into the `tests` folder and the necessary methods for it into the appropriate file in `pages`
5. Make sure all tests are passing and submit a pull request with your changes

[contributors]: https://github.com/mozilla/bouncer-tests/contributors
[git-clone]: https://help.github.com/articles/cloning-a-repository/
[git-fork]: https://help.github.com/articles/fork-a-repo/
[irc]: http://widget01.mibbit.com/?settings=1b10107157e79b08f2bf99a11f521973&server=irc.mozilla.org&channel=%23mozwebqa
[list]: https://mail.mozilla.org/listinfo/mozwebqa
[appium]: http://appium.io/
[pytest-selenium]: https://github.com/mozilla/pytest-selenium
[running-tests]: https://developer.mozilla.org/en-US/docs/Mozilla/QA/Running_Web_QA_automated_tests
[virtualenv]: https://wiki.mozilla.org/QA/Execution/Web_Testing/Automation/Virtual_Environments
