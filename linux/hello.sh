#!/bin/bash

echo "Name:"
read NAME
echo "Number:"
read NUMBER

for i in `seq $NUMBER`; do
	echo "Hello, $NAME!"
done
