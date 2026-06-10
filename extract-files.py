#!/bin/bash
#
# SPDX-FileCopyrightText: 2026 The StaticOS Project
# SPDX-License-Identifier: Apache-2.0
#

set -e

# Scriptin çalıştığı dizini al
MY_DIR="$(cd "$(dirname "${0}")"; pwd -P)"

# shusky/husky altındaki sürücü ayıklama scriptine yönlendir
pushd "${MY_DIR}/../shusky/husky"
./extract-files.py "$@"
popd
