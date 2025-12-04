# 🌟Savings Application (GUI)

A simple, user-friendly tool that calculates how much money to put in each of your savings bins.

## 📝 Overview

This application helps users automatically calculate how much money to allocate to different savings or budgeting bins.

Normally, this process requires a calculator — and a bunch of manual percentage calculations.
But doing all that math every time is very tedious, especially when multiple bins or custom percentages are involved.

This program simplifies the entire process:
1. Type in your salary
2.	Choose or customize your allocation settings
3.	Submit your input
4.	Instantly see how much goes into each bin

The goal is to make budgeting faster, clearer, and easier for anyone who wants to manage their money more effectively.

⸻

## 🎯 Features (Current & Planned)

✔ Current (Milestone 1)
- Basic GUI window using PyQt
- Salary input field
- “Calculate” button
- Placeholder output area
- Clean project structure
- Documentation (this README)

🔧 Coming Soon (Future Milestones)
- Predefined rules, such as:
- 50/30/20
- 50/10/40
- More in the future...
- Custom rules, including:
  - Up to 20 bins
  - User-defined percentages
  - Validation for min/max percentages
  - Total must equal 100%
  - Calculation Engine
  - Accurate distribution based on salary
  - Dynamic GUI output showing results
  - Testing
  - Unit tests for rules and calculations
  - Input validation tests
  - UI Improvements
  - Cleaner layout
  - Optional dark mode
  - Optional charts for visuals
  - Future Enhancements
  - Save/load custom rules
  - Export results (CSV/JSON)
  - Preset templates

## 📂 Project Structure
savings_app
 - main.py # Entry point of the GUI application
 - gui/
  - main_window.py      # Main PyQt window
  - settings_dialog.py  # (Milestone 2) Custom rule settings window
- core/
  - rules.py            # Prebuilt & custom rule definitions
  - calculation.py      # Allocation logic
- tests/
  - test_rules.py
  - test_calculation.py

## ▶️ How to Run
1. Install dependencies: pip install PyQt6
2. Start application: python main.py

## 💡 Motivation
Budgeting takes focus, planning, and discipline — it shouldn’t
also require doing percentages over and over again.

By automating the calculations, this application helps users
focus on their financial goals instead of manual math.