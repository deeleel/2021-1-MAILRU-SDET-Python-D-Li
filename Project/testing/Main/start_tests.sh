#!/bin/bash

pytest -s -l -v --vnc "${TESTS_PATH}" -n "${THREADS:-2}" --alluredir="/tmp/reports"
#