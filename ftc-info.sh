#! /usr/bin/env bash

projdir="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$projdir"
./venv/bin/python get_last_transcript.py info
