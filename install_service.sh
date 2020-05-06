#!/bin/bash
set -e

readonly script_dir=$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)
readonly install_dir="/etc/systemd/system/"

sudo cp -f "${script_dir}/pi_status_display.service" "${install_dir}"

sudo systemctl reenable pi_status_display.service

sudo systemctl restart pi_status_display.service
