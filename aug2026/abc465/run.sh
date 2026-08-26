#!/usr/bin/env bash
set -euo pipefail

script_dir="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
source_file="$script_dir/abc465_f.cpp"
binary_file="$script_dir/abc465_f"

g++ -std=c++17 -Wall -O3 -Wextra -pedantic "$source_file" -o "$binary_file"
# g++ -std=c++17 -Wall -Wextra -pedantic "$source_file" -o "$binary_file"

if [[ $# -gt 0 ]]; then
    "$binary_file" < "$1"
else
    "$binary_file"
fi
