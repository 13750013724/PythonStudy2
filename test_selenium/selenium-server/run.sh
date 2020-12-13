#!/usr/bin/env bash
for i in `adb devices|grep -w device |awk '{print $1}'`
do
    echo $i
    udid=$i pytest test_selenium_appium.py
    echo $i
    sleep 10
done