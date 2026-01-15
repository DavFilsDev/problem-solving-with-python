# 🧠 SLIDING WINDOW ALGORITHM

## 1️⃣ What problem does it solve?

Sliding Window is used when:

* You work with **arrays / strings**
* You need a **subarray / substring**
* The subarray must be **contiguous**
* You want to **optimize performance**

Typical questions:

* Maximum / minimum sum of a subarray
* Longest substring without repeating characters
* Fixed-size window problems
* Variable-size window problems

---

## 2️⃣ Why Sliding Window exists

### ❌ Brute force (bad)

Example: max sum of subarray of size `k`

```python
# O(n²) → too slow
for i in range(n):
    for j in range(i, i+k):
        ...
```

### ✅ Sliding Window (good)

* Reuse previous calculations
* Move window step by step
* Time complexity: **O(n)**

---

## 3️⃣ Fixed-size Sliding Window (core pattern)

### 🎯 Problem

> Given an array of integers and a number `k`, find the **maximum sum of any subarray of size `k`**.

Example:

```python
arr = [2, 1, 5, 1, 3, 2]
k = 3
Output: 9  # [5,1,3]
```

---

## ✅ Python solution (fixed window)

```python
def max_subarray_sum(arr, k):
    if len(arr) < k:
        return None

    window_sum = sum(arr[:k])
    max_sum = window_sum

    for i in range(k, len(arr)):
        window_sum += arr[i]        # add next element
        window_sum -= arr[i - k]    # remove left element
        max_sum = max(max_sum, window_sum)

    return max_sum
```

---

## 🔍 Explanation (VERY IMPORTANT)

### Step 1: First window

```python
window_sum = sum(arr[:k])
```

We calculate the sum **once**.

---

### Step 2: Slide the window

```python
window_sum += arr[i]
window_sum -= arr[i - k]
```

Window moves like this:

```
[2, 1, 5] 1 3 2
 2 [1, 5, 1] 3 2
 2 1 [5, 1, 3] 2
```

✔ Add right
✔ Remove left
✔ Constant time

---

### Step 3: Track maximum

```python
max_sum = max(max_sum, window_sum)
```

---

## ⏱ Complexity

| Metric | Value    |
| ------ | -------- |
| Time   | **O(n)** |
| Space  | **O(1)** |

---

## 4️⃣ Variable-size Sliding Window (advanced & powerful)

### 🎯 Problem

> Longest substring **without repeating characters**

Example:

```
"abcabcbb" → 3 ("abc")
```

---

## ✅ Python solution (variable window)

```python
def longest_unique_substring(s):
    seen = set()
    left = 0
    max_length = 0

    for right in range(len(s)):
        while s[right] in seen:
            seen.remove(s[left])
            left += 1

        seen.add(s[right])
        max_length = max(max_length, right - left + 1)

    return max_length
```

---

## 🔍 How it works

* `left` and `right` define the window
* Expand window by moving `right`
* Shrink window by moving `left`
* Keep condition valid

---

## 🧠 Mental model (IMPORTANT)

Think of a window like:

```
|---- WINDOW ----|
left            right
```

* Expand → add elements
* Violate rule → shrink
* Track best result

---

## 5️⃣ When should YOU use Sliding Window?

Ask yourself:
✔ Subarray / substring?
✔ Contiguous elements?
✔ Optimization needed?

If YES → Sliding Window.

---

## 📁 Repo structure suggestion

```
algorithms/
│
├── sliding_window_fixed.py
├── sliding_window_variable.py
├── sliding_window_test.py
```

---

# 🧠 Full testable Python file

Copy **everything below** into `sliding_window_test.py` 👇

```python
# sliding_window_test.py

def max_subarray_sum(arr, k):
    if len(arr) < k:
        return None

    window_sum = sum(arr[:k])
    max_sum = window_sum

    for i in range(k, len(arr)):
        window_sum += arr[i]
        window_sum -= arr[i - k]
        max_sum = max(max_sum, window_sum)

    return max_sum


def longest_unique_substring(s):
    seen = set()
    left = 0
    max_length = 0

    for right in range(len(s)):
        while s[right] in seen:
            seen.remove(s[left])
            left += 1

        seen.add(s[right])
        max_length = max(max_length, right - left + 1)

    return max_length


def run_tests():
    print("=== FIXED SIZE SLIDING WINDOW ===")
    print(max_subarray_sum([2, 1, 5, 1, 3, 2], 3), "→ expected 9")
    print(max_subarray_sum([1, 2, 3, 4, 5], 2), "→ expected 9")
    print(max_subarray_sum([1, 1, 1, 1], 4), "→ expected 4")

    print("\n=== VARIABLE SIZE SLIDING WINDOW ===")
    print(longest_unique_substring("abcabcbb"), "→ expected 3")
    print(longest_unique_substring("bbbbb"), "→ expected 1")
    print(longest_unique_substring("pwwkew"), "→ expected 3")


if __name__ == "__main__":
    run_tests()
```

---

# ▶️ How to run it in the terminal (Debian)

### 1️⃣ Open terminal

```bash
cd ~
```

(or go to the folder where the file is)

---

### 2️⃣ Run the file

```bash
python3 sliding_window_test.py
```

---

# 🖥 Expected output

```
=== FIXED SIZE SLIDING WINDOW ===
9 → expected 9
9 → expected 9
4 → expected 4

=== VARIABLE SIZE SLIDING WINDOW ===
3 → expected 3
1 → expected 1
3 → expected 3
```

If:

* result == expected → ✅ algorithm works
* result ≠ expected → ❌ bug detected

---

# 🧠 Why this is a GOOD testing style

✔ No extra libraries
✔ Works everywhere
✔ Fast feedback
✔ Easy to understand
✔ Perfect for learning

Later, you can upgrade to:

* `unittest`
* `pytest`
* CI pipelines

---
