#!/usr/bin/env bash
set -e 

. ~/.virtualenvs/parcial2/bin/activate

PYTHONPATH=. py.test --junitxml=python_tests.xml