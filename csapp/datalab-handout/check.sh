#!/bin/zsh
echo "--------whether legal-------"
./dlc bits.c
echo "------operator counts-------"
./dlc -e bits.c
