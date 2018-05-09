#!/bin/sh
echo "Compile Sauce"
sassc -t compressed public/css/main.sass public/css/main.min.css &
echo "Start le server"
exec crystal src/galaxy.cr
wait
