## **Day 13: The Hidden Coordinates 📍**  

### **📜 Story**  
With the **First Key** in hand, Echo scans it and **deciphers a strange code** embedded in its structure:  

**"To find the next key, decode the coordinates hidden within this number!"**  

The Debuggers’ archive hints at a **pattern-based decoding** system. The only way to extract the location is by **identifying and printing all even digits** in a given number.  

---

### **🎯 Challenge: Extract the Hidden Coordinates 🔢**  
You need to create a program that:  
1. **Takes a number (N) as input**.  
2. **Extracts and prints all even digits from N**.  
3. If there are **no even digits**, print `"No even digits found!"`  

---

### **🔍 Example Input/Output**  

#### **Example 1**  
**Input:**  
```
Enter N: 295874
```  
**Output:**  
```
Even digits: 2 8 4
```  

#### **Example 2**  
**Input:**  
```
Enter N: 13579
```  
**Output:**  
```
No even digits found!
```  

---

### **💡 Hints**  
- A number’s **even digits** are those divisible by `2`.  
- Convert the number to a **string** and check each digit.  
- In Python, you can iterate using `for digit in str(N)`.  
- In C++, extract digits using a **while loop** (`N % 10` and `N // 10`).  
- In JavaScript, split the number into an array (`.split('')`) and filter even numbers.  

---

### **📝 Your Task**  
- Write your solution in any programming language.  
- Save it as `day13_coordinates.[ext]` (e.g., `day13_coordinates.py`).  

---

### **😂 Fun Break - Nariyal Bhai's Joke Corner**  
🧉 Nariyal Bhai: *"Why do programmers prefer dark mode?"*  
You: **"Why?"**  
Nariyal Bhai: *"Because light attracts bugs!"* 🐛😂  

---

The **coordinates are extracted**, leading to a **mysterious island** far away. What’s waiting there? Find out in **Day 14!** 🔥