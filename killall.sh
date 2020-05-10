#!/bin/bash
ps aux | grep "python3 mememachine.py" | awk '{print $2}' | xargs kill -9
