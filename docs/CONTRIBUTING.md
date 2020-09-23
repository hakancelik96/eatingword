Firstly make sure you have python 3.8 version installed on your system.

## Development and Contributing

## Issue

To make an improvement, add a new feature or anything else, please open a issue first.

**Good first issues are the issues that you can quickly solve, we recommend you take a
look.**
[Good first issue](https://github.com/hakancelik96/eatingword/labels/good%20first%20issue)

## Fork Repository

[fork the eatingword.](https://github.com/hakancelik96/eatingword/fork)

## Clone Repository

```shell
$ git clone git@github.com:<USERNAME>/eatingword.git
$ cd eatingword
$ python3.8 -m venv env
$ source env/bin/activate
$ python -m pip install requirements.txt
$ python -m pip install requirements-dev.txt
$ sudo apt install postgresql postgresql-contrib python-celery-common
$ sudo service postgresql start
$ sudo -u postgres psql
$ CREATE DATABASE eatingword;
$ CREATE USER projectuser WITH PASSWORD 'password';
$ ALTER ROLE projectuser SET client_encoding TO 'utf8';
$ ALTER ROLE projectuser SET default_transaction_isolation TO 'read committed';
$ ALTER ROLE projectuser SET timezone TO 'UTC';
$ GRANT ALL PRIVILEGES ON DATABASE eatingword TO projectuser;
```

Run redis-server

```shell
$ redis-server
```

Create a file called `.env`

```shell
DEBUG=on
SECRET_KEY=key
DATABASE_URL=postgresql://projectuser:password@127.0.0.1:5432/eatingword
ALLOWED_HOSTS=*
INTERNAL_IPS=127.0.0.1
CELERY_BROKER_URL=redis://localhost:6379
```

Run celery

```shell
$ celery -A eatingword worker -l info
```

## Setup Branch

```shell
git checkout -b i{your issue number}
```

## Install pre-commit hooks

```shell
$ pre-commit install # to pre-commit will run automatically on git commit!
```

## How to Update My Local Repository

```shell
$ git remote add upstream git@github.com:hakancelik96/eatingword.git
$ git fetch upstream
$ git rebase upstream/master
```

## Testing

After typing your codes, you should run the tests by typing the following command.

```shell
$ tox
```

or

```shell
$ python manage.py test apps
```

If all tests pass.

## The final step

After adding a new feature or fixing a bug please report your change to
[CHANGELOG.md](CHANGELOG.md) and write your name, github address and email in the
[AUTHORS.md](AUTHORS.md) file in alphabetical order.

### Commit Messages

If you want, you can use the emoji about the commit message you will throw, this can
help us better understand the change you have made and also it is fun.

- When you make any support commit; 💪
- When you make any tests commit; 🧪
- When you make any fix commit; 🐞
- When you make any optimizasiyon commit; 💊
- when you make any new feature commit; 🔥

## License

Eatingword is MIT licensed, as found in the LICENSE file.
