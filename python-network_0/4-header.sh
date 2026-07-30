
# y the body of a url call 
curl -sG "$1" -H "X-School-User-Id: 98"Lab 1: Grade Evaluator & Archiveri

This project contains a Python application that evaluates a student's final academic standing from a CSV file of grades, and a Bash script that archivesthat CSV file and resets the workspace for the next batch of grades.

## Files

- grade-evaluator.py: Reads grades.csv, validates it, calculates the final
  GPA, determines PASSED/FAILED status, and reports which failed Formative
  assignment(s) are eligible for resubmission.
- organizer.sh: Archives the current grades.csv into an archive folder with
  a timestamped filename, creates a fresh empty grades.csv, and logs the
  action to organizer.log.
- grades.csv: Sample grade data used for testing.

## Requirements

- Python 3
- Bash (Linux/macOS/WSL)

## Running the Python application

Run: python3 grade-evaluator.py

You will be prompted to enter the CSV filename, e.g. grades.csv

The program prints:
1. A per-assignment breakdown (score, weight, weighted contribution).
2. The Formative and Summative category totals and percentages.
3. The overall Total Grade (out of 100) and GPA (out of 5.0).
4. The final status: PASSED or FAILED. A student must score at least 50
   percent in both the Formative and Summative categories to pass.
5. Any failed Formative assignment(s) eligible for resubmission: the
   failed Formative assignment(s) with the highest weight, including ties.

Expected CSV header: assignment,group,score,weight

- group must be Formative or Summative.
- score must be between 0 and 100.
- All weights must sum to exactly 100, with Formative weights summing to
  60 and Summative weights summing to 40.

If the file is missing, empty, has an out-of-range score, or the weights
do not add up correctly, the program prints a clear error message and
exits without crashing.

## Running the archiver

Run: bash organizer.sh
or, if executable: ./organizer.sh

