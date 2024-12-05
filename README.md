# My framework for solving Advent of Code

You need to add your Session key from the AOC-Website to the variable `SESSION_COOKIE=` in a .env file in the project root.

## Features:
- Pull problem description form AOC website.
- Get your Puzzle input.
- Automatic submission of your solution.

## Usage

```bash
usage: aoc.py [-h] [-i] [-s] [-t] [-d DAY] [-y YEAR]

Advent of Code Wrapper

options:
  -h, --help            show this help message and exit
  -i, --init            Initialize a new day
  -s, --submit          Run and submit solution via api
  -t, --test            Run on test data
  -d DAY, --day DAY     Day to run default is today
  -y YEAR, --year YEAR  Year to run default is this year
```