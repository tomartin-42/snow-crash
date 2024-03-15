#!/bin/sh

for i in /home/tommy/snow-crash/level04/* ; do
	(ulimit -t 5; bash -x "$i")
	sleep 100
done
