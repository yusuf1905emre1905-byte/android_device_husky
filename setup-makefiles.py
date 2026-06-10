#!/bin/bash
#
# SPDX-FileCopyrightText: 2026 The StaticOS Project
# SPDX-License-Identifier: Apache-2.0
#

set -e

MY_DIR="$(cd "$(dirname "${0}")"; pwd -P)"

pushd "${MY_DIR}/../shusky/husky"
./setup-makefiles.py
popd
