'''
     * In The Name Of God *
''' 
#              H
#             /|\
#            / | \
#           /--F--\
#          / \ | / \
#         *--- A ---*
#          \ / Z \ /
#           \  A  /
#            *-R-*
#             \ /
#          ====*=====
#          | HFAZAR |
#          ==========
'''
================================================
  Author         : HFAzar
  Project Title  : File Management and Analysis Tool
  Class Session  : 09
  Level          : {level}
  Date           : 1405-07-10
  Python Version : 3.13.14
  GitHub         : https://github.com/HFAzar
  Status         : {status}
================================================
'''
#%%
'''
Task number 03: 

Description: File Management and Analysis Tool

OS · Math · Loops · Functions
Design a program that takes a folder path from the user and analyzes the files 
contained within it.
For example, consider a folder with the following files:
project/
├── main.py
├── users.txt
├── report.pdf
├── image.jpg
└── data.csv
Required features:
1.	Check for the existence of the folder using the `os` module.
2.	Display the names of all files present in the folder.
3.	Calculate the total number of files.
4.	Calculate the size of each file in KB.
5.	Calculate the total and average size of the files.
6.	Identify the largest and smallest files.
7.	Use `math.ceil()` to round file sizes up to the nearest integer.
8.	Count files based on their extensions (e.g., `.py`, `.txt`).
Bonus Challenge: Use the `os` module to create a folder named "reports" and 
save the analysis report into a text file inside it.
Note: For the main part of the exercise, only files located directly within 
the folder should be analyzed; processing subfolders is optional.
'''
#%%

import os 
import math

# ================================================
#   Task 3 — File Management and Analysis Tool
# ================================================

# ---------- Helper Functions ----------

def get_folder_path():
    path = input("Enter your folder path: ")
    if os.path.isdir(path):
        return path
    else:
        print("Error: Folder does not exist!")
        return None


def list_files(folder_path):
    files = []
    for item in os.listdir(folder_path):
        full_path = os.path.join(folder_path, item)
        if os.path.isfile(full_path):
            files.append(item)
    return files


def get_file_sizes(folder_path, files):
    sizes = []
    for name in files:
        full_path = os.path.join(folder_path, name)
        size_bytes = os.path.getsize(full_path)
        size_kb = math.ceil(size_bytes / 1024)
        sizes.append((name, size_kb))
    return sizes


def calculate_stats(sizes):
    count = len(sizes)
    total = sum(size for _, size in sizes)
    average = total / count if count > 0 else 0
    largest = max(sizes, key=lambda x: x[1]) if sizes else None
    smallest = min(sizes, key=lambda x: x[1]) if sizes else None
    return {
        "count": count,
        "total": total,
        "average": average,
        "largest": largest,
        "smallest": smallest
    }


def count_by_extension(files):
    ext_count = {}
    for name in files:
        ext = os.path.splitext(name)[1]
        if ext in ext_count:
            ext_count[ext] += 1
        else:
            ext_count[ext] = 1
    return ext_count


def save_report(folder_path, sizes, stats, ext_count):
    os.makedirs("reports", exist_ok=True)
    report_path = os.path.join("reports", "report.txt")
    with open(report_path, "w", encoding="utf-8") as f:
        f.write(f"Folder: {folder_path}\n")
        f.write("=" * 30 + "\n")
        f.write("Files and sizes (KB):\n")
        for name, size in sizes:
            f.write(f"  {name}: {size} KB\n")
        f.write("-" * 30 + "\n")
        f.write(f"Count: {stats['count']}\n")
        f.write(f"Total: {stats['total']} KB\n")
        f.write(f"Average: {stats['average']:.2f} KB\n")
        f.write(f"Largest: {stats['largest']}\n")
        f.write(f"Smallest: {stats['smallest']}\n")
        f.write("-" * 30 + "\n")
        f.write("Extensions:\n")
        for ext, cnt in ext_count.items():
            f.write(f"  {ext}: {cnt}\n")
    print(f"Report saved to {report_path}")

# ---------- Main ----------

def main():
    folder_path = get_folder_path()
    if folder_path is None:
        return

    files = list_files(folder_path)
    if not files:
        print("No files found in this folder.")
        return

    sizes = get_file_sizes(folder_path, files)
    stats = calculate_stats(sizes)
    ext_count = count_by_extension(files)

    print("\n--- Analysis ---")
    print(f"Files: {files}")
    print(f"Count: {stats['count']}")
    print(f"Total: {stats['total']} KB")
    print(f"Average: {stats['average']:.2f} KB")
    print(f"Largest: {stats['largest']}")
    print(f"Smallest: {stats['smallest']}")
    print(f"Extensions: {ext_count}")

    save_report(folder_path, sizes, stats, ext_count)


if __name__ == "__main__":
    main()



