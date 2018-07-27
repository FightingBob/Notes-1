#!/bin/bash

# for pytest scriptz


when-changed -r -v -1 -s ./ "pytest $1"
