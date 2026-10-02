# Calendar Program

A simple Python program that prints the calendar of any month and year you enter.

## How to use

Run the file with Python:

    python CALENDAR.py

It will ask you for a year and a month, then show the calendar for that month.

## Example

    Enter year: 2026
    Enter month: 10

         October 2026
    Mo Tu We Th Fr Sa Su
              1  2  3  4
     5  6  7  8  9 10 11
    12 13 14 15 16 17 18
    19 20 21 22 23 24 25
    26 27 28 29 30 31

## What I used

- Python 3
- `calendar` module to print the calendar
- `sys` module to exit the program on wrong input

## How it works

- First it asks for a year and checks if the input is a number
- Then it asks for a month and checks if it is between 1 and 12
- If everything is fine, it prints the calendar using `calendar.month()`
- If the input is wrong, it shows an error message and stops
