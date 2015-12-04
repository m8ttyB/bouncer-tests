# Bouncer Tests for download.allizom.org

Thank you for checking out Mozilla's [Bouncer](https://wiki.mozilla.org/Bouncer) test suite. Mozilla and [Web QA team](https://quality.mozilla.org/teams/web-qa/) are grateful for the help and hard work of [many contributors](https://github.com/mozilla/bouncer-tests/graphs/contributors) like yourself.

## Getting involved as a contributor

We love working with contributors to fill out the test coverage for Bouncer Tests, but it does require a few skills. You will need to know some Python and you will need some basic familiarity with [GitHub](https://guides.github.com/).

If you need to brush up on programming but are eager to start contributing immediately, please consider helping us [find bugs in Mozilla Firefox](https://oneanddone.mozilla.org/team/2/) or [find bugs in the Mozilla websites](https://oneanddone.mozilla.org/team/6/) tested by the Web QA team.

To brush up on Python skills before engaging with us, [Dive Into Python](http://www.diveintopython.net/toc/) is an excellent resource. MIT also has [lecture notes on Python](http://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-189-a-gentle-introduction-to-programming-using-python-january-iap-2011/) available through their open courseware. The programming concepts you will need to know include functions, working with classes, and some object oriented programming basics.

## Questions are always welcome

While we take pains to keep our documentation updated, the best source of information is those of us who work on the project. Don't be afraid to join us in [irc.mozilla.org](https://wiki.mozilla.org/IRC) [#mozwebqa](http://chat.mibbit.com/?server=irc.mozilla.org&channel=#mozwebqa) to ask questions about Bouncer Tests. Mozilla also hosts the [#mozillians](http://chat.mibbit.com/?server=irc.mozilla.org&channel=#mozillians) chat room to answer your general questions about contributing to Mozilla.

## How to set up and build Bouncer tests locally

This repository contains tests suite used to test Mozilla's Bouncer. Mozilla maintains a guide to run automated tests on our [QMO website](https://quality.mozilla.org/docs/webqa/running-webqa-automated-tests/).

You will need to install the following:

* **Git**: If you have cloned this project already then you can skip this! GitHub has excellent guides for [Windows](https://help.github.com/articles/set-up-git/#platform-windows), [OS X](https://help.github.com/articles/set-up-git/#platform-mac) and [Linux](https://help.github.com/articles/set-up-git/#platform-linux).
* **Python**: Before you will be able to run these tests you will need to have [Python 2.6](https://www.python.org/download/releases/2.6/) installed.

### Installing `pip` (for managing Python packages)

```bash
sudo easy_install pip
```

### Installing dependencies

If you are using `virtualenv`, run the following in the project root:

```bash
virtualenv venv
source venv/bin/activate
pip install -r requirements.txt
```

If you are not using `virtualenv`, run the following in the project root to install dependencies globally:

```bash
sudo pip install -r requirements.txt
```

For more information on `virtualenv`, see below.

### Running tests locally

To run these tests, use:

```bash
py.test --baseurl="http://download.allizom.org" tests
```

Use `-k` to run a specific test. For example,

```bash
py.test -k test_that_checks_redirect_using_incorrect_query_values \
        --baseurl="http://download.allizom.org" tests
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

## License

This software is licensed under the MPL 2.0:

```
This Source Code Form is subject to the terms of the Mozilla Public
License, v. 2.0. If a copy of the MPL was not distributed with this
file, You can obtain one at http://mozilla.org/MPL/2.0/.
```
