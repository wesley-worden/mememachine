#!/bin/bash
if [[ -f idontwannadie ]]
then
	kill -9 $(cat idontwannadie)
	rm idontwannadie
else
	echo "bruh no pid file but check this out:"
	ps aux | grep mememachine.py
fi
