#!/bin/bash

read FILE

if test -f "$FILE"; then
	cp $FILE /tmp/ 

fi
