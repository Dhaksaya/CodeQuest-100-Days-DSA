

# 🌀 Day 18: The Maze of Recursion – Nested Maze Depth Finder

## 📖 Story  
After crossing the Fibonacci Path, your journey brings you to a mysterious, multidimensional maze. The walls seem to fold into themselves—hallways within hallways, corridors nested deep inside others.

Echo, your spectral companion, whispers:  
> “This is no ordinary labyrinth. To escape, you must **understand the depth of recursion**. The maze is built on nested paths. Your task is to measure how deep it truly goes.”

The Debuggers believe this knowledge is the key to escaping The Glitch’s influence and reaching the next level of your journey.

---

## 🎯 Challenge Overview

You are given a **nested list** structure that represents a recursive maze. Your task is to write a **recursive function** that computes the **maximum depth** of this nested list.

### ✅ You must:
- Take a nested list as input.
- Determine how many **levels of nesting** it contains.
- Return or print the **maximum depth** found.

---

## 🧠 Problem Explanation

### What is “Depth” in this context?

- A **flat list** like `[1, 2, 3]` has a depth of `1` — it’s the surface level of the maze.
- A list like `[1, [2, 3]]` has a depth of `2` — the inner list represents one nested level.
- `[1, [2, [3, [4]]]]` has a depth of `4`.

The **depth** increases each time you go into another list inside the previous one.

---

## 💻 Input & Output Format

### Input:
A nested list of arbitrary depth.

```python
[1, [2, [3, [4]]]]
```

### Output:
A string stating the maximum depth.

```text
The maze has a depth of 4.
```

---

## 🔍 Sample Test Cases

### Test Case 1
```python
Input: [1, 2, 3]
Output: The maze has a depth of 1.
```

### Test Case 2
```python
Input: [1, [2, 3]]
Output: The maze has a depth of 2.
```

### Test Case 3
```python
Input: [[[[[[]]]]]]
Output: The maze has a depth of 6.
```

---

## 🧩 Hints

- Use **recursion** to explore each element of the list.
- If the element is itself a list, recursively find its depth.
- Track the **maximum depth** as you go.

---

## ✨ Example Solution Skeleton (Python)

```python
def find_depth(structure):
    if not isinstance(structure, list):
        return 0
    elif not structure:
        return 1
    else:
        return 1 + max(find_depth(item) for item in structure)

# Example
maze = [1, [2, [3, [4]]]]
depth = find_depth(maze)
print(f"The maze has a depth of {depth}.")
```

---

## 📝 Your Task

- Implement this in **any programming language** you prefer (Python, C++, Java, etc.).
- Save the solution as:  
  📁 `day18_recursive_depth.[ext]`  
  _Example:_ `day18_recursive_depth.py`

---

## 🌟 Motivational Quote of the Day
> "Every problem has a solution. Sometimes, you just have to look inside yourself—just like recursion reveals its answer from within." – Unknown

---

## 😂 Echo’s Dad Joke of the Day  
> **Q:** Why did the recursive function get a headache?  
> **A:** Because it couldn’t stop calling itself! 😆

---

You’ve peeled back the layers of the maze and revealed its hidden depth. Every level you conquer sharpens your mind for what lies ahead. Prepare for **Day 19**, where the recursion might turn… infinite. 🧠🔥

---

