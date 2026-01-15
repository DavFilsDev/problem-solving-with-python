
---

# 🧠 BINARY SEARCH (THE RIGHT WAY)

## 1️⃣ What problem does Binary Search solve?

Binary Search is used when:

* The data is **sorted**
* You need to **find an element quickly**

Instead of scanning one by one (**O(n)**), binary search works in **O(log n)**.

---

## 2️⃣ The core idea (intuition)

Imagine searching a word in a dictionary 📖:

* You don’t start at page 1
* You open the **middle**
* Decide left or right
* Repeat

That’s binary search.

---

## 3️⃣ Classic problem

> Given a **sorted list** and a target, return the **index** of the target
> Return `-1` if not found

Example:

```python
nums = [1, 3, 5, 7, 9]
target = 7
→ 3
```

---

## 4️⃣ Clean Python implementation (iterative)

```python
def binary_search(arr, target):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1
```

---

## 5️⃣ Line-by-line explanation

```python
left = 0
right = len(arr) - 1
```

Search range starts full array.

---

```python
while left <= right:
```

Keep searching while range is valid.

---

```python
mid = (left + right) // 2
```

Find middle index.

---

```python
if arr[mid] == target:
    return mid
```

Found 🎯

---

```python
elif arr[mid] < target:
    left = mid + 1
```

Target is on the right.

---

```python
else:
    right = mid - 1
```

Target is on the left.

---

```python
return -1
```

Not found.

---

## ⏱ Complexity

| Metric | Value        |
| ------ | ------------ |
| Time   | **O(log n)** |
| Space  | **O(1)**     |

🔥 Extremely efficient

---

## ▶️ Run the file

```bash
python3 binary_search_test.py
```

Expected output:

```
=== BINARY SEARCH TESTS ===
0 → expected 0
3 → expected 3
6 → expected 6
-1 → expected -1
-1 → expected -1
```


---

## 🧠 Variations you SHOULD learn next

Binary Search is more than just finding a number:

1️⃣ First / last occurrence
2️⃣ Binary search on answers
3️⃣ Rotated sorted array
4️⃣ Lower bound / upper bound
5️⃣ Infinite arrays

---
