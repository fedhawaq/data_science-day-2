# Statistical Engine & Monte Carlo Simulation

## 📌 Project Overview
This project is a **pure-Python statistical engine** built completely from scratch without using external libraries like NumPy or Pandas.

It performs the following tasks:

- Calculates **mean, median, mode**
- Calculates **variance** (sample & population)
- Calculates **standard deviation**
- Detects **outliers** using standard deviation
- Handles **mixed data types** and **empty datasets**
- Runs a **Monte Carlo simulation** to model server crash probability and demonstrate the **Law of Large Numbers (LLN)**

The project also includes a fully functional **unittest test suite**, a realistic **sample salary dataset**, and a clean project folder structure.

---

## 🧮 Mathematical Logic

### **1. Mean**
The mean is the sum of all values divided by how many values exist.
Mean = (Sum of all values) ÷ (Number of values)

---

### **2. Median (Even vs. Odd Rule)**  
To find the median, the dataset is sorted first.

- **Odd count:**  
  The middle value is the median.
  
  Example:  
  `[3, 5, 8] → median = 5`

- **Even count:**  
  The median is the average of the two middle values.
  
  Example:  
  `[3, 5, 8, 10] → median = (5 + 8) ÷ 2 = 6.5`

---

### **3. Mode**
The mode is the value that appears most frequently.

- If multiple values tie → return all (multimodal)  
- If all values occur once → "No mode"

Example:
[2, 2, 3, 3, 4] → modes = [2, 3]
[1, 2, 3] → No mode

---

### **4. Variance (Sample vs Population)**  
Variance measures how far values are spread from the mean.

- **Population Variance** (used when entire population is known):
σ² = Σ(xi − mean)² / N


Where:

- `N` = number of values  
- `Σ(xi − mean)²` = sum of squared differences from the mean  

---

### **5. Standard Deviation**
Standard deviation is the square root of variance.
Standard Deviation = √Variance


    Setup Instructions:
### Setup Instructions

Follow these steps to run the project on your computer.

### 1. Clone (download) the project from GitHub
Open your terminal or VS Code terminal and type:

```bash
git clone <https://github.com/fedhawaq/data_science-day-2>
### 2 Run the Statistical Engine

``` bash   python src/stat_engine.py
### 3 Run the Monte Carlo Simulation
python src/monte_carlo.py
### 4 Run everything together (recommended)

```bash    python main.py
This file will load the salary dataset, run calculations, show outliers, and run the Monte Carlo probability simulation.


Testing

my project includes unit tests to verify the correctness of all statistical functions (mean, variance, standard deviation, and Bessel’s correction).

## the following are How to run the tests
1. Open the terminal
2. Navigate to the project folder:
 bash: cd your-project-folder
3.  Run the test suite using Python's built-in unittest:
   python -m unittest


