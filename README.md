# Tests for Mozilla's Bouncer

This repository contains tests for Mozilla's [Bouncer](https://wiki.mozilla.org/Bouncer).

[![license](https://img.shields.io/badge/license-MPL%202.0-blue.svg)](https://github.com/mozilla/bouncer-tests/blob/master/LICENSE)
[![travis](https://img.shields.io/travis/mozilla/bouncer-tests.svg?label=travis)](http://travis-ci.org/mozilla/bouncer-tests/)
[![stage](https://img.shields.io/jenkins/s/https/webqa-ci.mozilla.com/bouncer.stage.svg?label=stage)](https://webqa-ci.mozilla.com/job/bouncer.stage/)
[![prod](https://img.shields.io/jenkins/s/https/webqa-ci.mozilla.com/bouncer.prod.svg?label=prod)](https://webqa-ci.mozilla.com/job/bouncer.prod/)
[![requirements](https://img.shields.io/requires/github/mozilla/bouncer-tests.svg)](https://requires.io/github/mozilla/bouncer-tests/requirements/?branch=master)

## Getting involved
We love working with contributors to fill out the test coverage for Mozilla's
Bouncer, but it does require a few skills. By contributing to our test
suite you will have an opportunity to learn and/or improve your skills with
Python, GitHub, and virtual environments.

All of [these awesome contributors][contributors] have opened pull requests
against this repository.

## Questions are always welcome
While we take pains to keep our documentation updated, the best source of
information is those of us who work on the project. Don't be afraid to join us
in irc.mozilla.org [#mozwebqa][irc] to ask questions about our tests. We also
have a [mailing list][list] available that you are welcome to join and post to.

## How to run the tests locally

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
$ py.test --baseurl http://bouncer-bouncer.stage.mozaws.net
```

Use `-k` to run a specific test. For example,

```bash
$ py.test --baseurl http://bouncer-bouncer.stage.mozaws.net -k test_that_checks_redirect_using_incorrect_query_values
```

[contributors]: https://github.com/mozilla/bouncer-tests/contributors
[git-clone]: https://help.github.com/articles/cloning-a-repository/
[git-fork]: https://help.github.com/articles/fork-a-repo/
[irc]: http://widget01.mibbit.com/?settings=1b10107157e79b08f2bf99a11f521973&server=irc.mozilla.org&channel=%23mozwebqa
[list]: https://mail.mozilla.org/listinfo/mozwebqa
[virtualenv]: https://wiki.mozilla.org/QA/Execution/Web_Testing/Automation/Virtual_Environments
