#!/usr/bin/python3
# 10-divisible_by_2.py


def divisible_by_2(my_list=[]):
    """Find all multiples of 2 in a list."""
    multiples = []
    for i in range(len(my_list)):
        if my_list[i] % 2 == 0:
            multiples.append(True)
        else:
            multiples.append(False)


# ============================================================
# hospital_analysis.sh
# KNH Hospital Analysis Script
# ------------------------------------------------------------
# Member 5 (Clinical Analyst):  process_vitals()
# Member 6 (Facility Auditor):  water_audit()
# ============================================================


# ------------------------------------------------------------
# MEMBER 5 — Clinical Analyst
# Function: process_vitals()
# Placeholder — to be implemented by Member 5
# ------------------------------------------------------------
process_vitals() {
    echo "[INFO] process_vitals() — awaiting Member 5 implementation."
}


# ------------------------------------------------------------
# MEMBER 6 — Facility Auditor
# Function: water_audit()
#
# What this function does:
#   It reads the water usage log file.
#   It finds all rows that belong to ICU_WATER_RESERVE.
#   It adds up all the usage values and counts how many rows there are.
#   It divides the total by the count to get the average.
#   It prints a neat summary to the screen.
# ------------------------------------------------------------
water_audit() {

    echo "============================================"
    echo "   KNH Facility Water Audit"
    echo "   Device: ICU_WATER_RESERVE"
    echo "============================================"

    # --- Step 1: Make sure the reports folder exists ---
    if [ ! -d "reports" ]; then
        echo "[ERROR] The reports folder does not exist."
        echo "        Please run hospital_admin.sh first."
        exit 1
    fi

    # --- Step 2: Make sure the water log file exists ---
    if [ ! -f "active_logs/water_usage.log" ]; then
        echo "[ERROR] Water usage log not found."
        echo "        Make sure the hospital engine is running."
        exit 1
    return (multiples)
