# Day-26-Power-of-Two
Day 26/100 - Python Program to Check if a Number is a Power of Two

# Check if a Number is a Power of Two
A program to determine whether a given integer is a power of two using a highly efficient bitwise operation.

## 📝 Description

This program evaluates a user-inputted number to check if it is a power of two (e.g., 1, 2, 4, 8, 16). Instead of using a loop to repeatedly divide the number by 2, this script utilizes a clever **bitwise manipulation** technique for $O(1)$ time complexity execution.

In binary representation, a power of two always has exactly one bit set to `1` (e.g., 8 is `1000`). If you subtract 1 from a power of two, all the bits after that single `1` flip to `1`, and the original `1` becomes `0` (e.g., 7 is `0111`). Therefore, performing a bitwise AND operation (`&`) between the number and the number minus one (`n & (n - 1)`) will always result in `0` if the number is a power of two.

---

## 🎯 Problem Statement

### Input:

* **Input 1:** A single integer value.

### Output:

* A formatted string stating: "[num] is a power of two." or "[num] is not a power of two."

### Rules:

1. The program must accept an integer input from the user.
2. The program must use a function (e.g., `power_of_two`) to evaluate the number.
3. The number must be strictly greater than zero (`n > 0`), as zero and negative numbers cannot be powers of two in this context.
4. The program must evaluate the mathematical condition using the bitwise AND operator: `(n & (n - 1)) == 0`.
5. If both conditions (`n > 0` and the bitwise result) are true, return `True`. Otherwise, return `False`.

---

## 💡 Examples

### Example 1 (Standard Power of Two)

**Input:**

```
16


```

**Output:**

```
16 is a power of two.


```

**Explanation:** In binary, 16 is `10000`. 15 is `01111`.
The bitwise AND operation: `10000 & 01111 = 00000` (which is 0).

### Example 2 (Not a Power of Two)

**Input:**

```
14


```

**Output:**

```
14 is not a power of two.


```

**Explanation:** In binary, 14 is `1110`. 13 is `1101`.
The bitwise AND operation: `1110 & 1101 = 1100` (which is 12, not 0).

### Example 3 (The Base Case)

**Input:**

```
1


```

**Output:**

```
1 is a power of two.


```

**Explanation:** 1 is $2^0$. In binary, 1 is `1`. 0 is `0`. `1 & 0 = 0`. The condition holds true.

### Example 4 (Edge Case: Zero or Negative)

**Input:**

```
0


```

**Output:**

```
0 is not a power of two.


```

**Explanation:** The program first checks `n > 0`. Since 0 is not greater than 0, it immediately evaluates to `False` without even checking the bitwise condition, preventing logical errors.

---

## 🚀 How to Use

1. **Clone this repository** (or save the script)

```bash
git clone https://github.com/adiaryaz/Day-26-Power-of-Two.git
cd power-of-two


```

2. **Run the program**:

```bash
python main.py


```

Enter an integer when prompted to see if it is a mathematical power of two.
