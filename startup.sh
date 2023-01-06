#!/bin/bash

scheduleShutdown () {
	sudo timedatectl set-timezone Europe/Berlin
	sudo shutdown -h 17:15
	path="$( cd -- "$(dirname "$0")" >/dev/null 2>&1 ; pwd -P )"
	python3 ${path}/SMA_Bot.py
	$BASH
}

gateway=`ip route | grep default | cut -d ' ' -f 3`

while ! ping -c1 $gateway &>/dev/null; do echo "Ping Fail - `date`"; done ; echo "Host Found - `date`" ; scheduleShutdown
