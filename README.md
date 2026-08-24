# practice-healthcare-intake

A small console app for practicing Python OOP — inheritance, encapsulation, and properties — modeled as a clinic contact directory.

## Requirements

Python 3.8+. No third-party dependencies.

## Run

```bash
python3 main.py
```

## What it does

Starts with seeded doctors and patients, then loops on a menu:

1. List doctors
2. List patients
3. Add doctor
4. Add patient
5. Exit

Added records live in memory only — nothing is persisted between runs.

## Design

`Person` is the base class, holding name, last name, and phone number behind read-only properties. `Doctor` and `Patient` extend it with `specialty` and `symptom` respectively, and each overrides `describe()` to format its own summary line.
