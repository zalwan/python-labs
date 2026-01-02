# Dataset Sorting Program

This is a simple Python program for managing and sorting a dataset using
the **pandas** library. The program is designed for academic purposes
and demonstrates basic data manipulation, sorting, and menu-driven
interaction in Python.

## Features

-   Display dataset in tabular format
-   Sort dataset by a single column
-   Sort dataset by multiple columns
-   Reset dataset to its original state
-   Interactive menu via terminal/command prompt

## Dataset Structure

The dataset contains the following columns: - **nama** (Name) - **umur**
(Age) - **gaji** (Salary) - **departemen** (Department)

## Project Structure

    python-dataset-sorting/
    │
    ├── src/
    │   └── dataset_sorting.py
    │
    ├── requirements.txt
    │
    └── README.md

## Requirements

-   Python 3.x
-   pandas

Install dependencies using:

``` bash
pip install -r requirements.txt
```

## How to Run

From the project root directory, run:

``` bash
python src/dataset_sorting.py
```

## Notes

-   This program uses pandas DataFrame and the `sort_values()` method.
-   The dataset reset feature restores the original unsorted data.
-   The program is suitable for beginners learning data processing in
    Python.

## Author

Rizal Suryawan - Software engineer
