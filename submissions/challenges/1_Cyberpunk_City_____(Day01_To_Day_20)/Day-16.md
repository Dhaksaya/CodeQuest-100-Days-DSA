## **Day 16: The Code of Courage – Factorial of Destiny** 🔥

### **📜 Story**  
After successfully navigating the maze, you arrive at a towering temple guarded by ancient digital runes.  
Echo whispers,  
*"This temple requires you to demonstrate the power of recursion! Calculate the factorial of a number to unlock its secrets and move forward on your quest."*  

### **🎯 Challenge: Factorial Calculator**  
Write a program that calculates the factorial of a given non-negative integer. The factorial of a number \( n \) (denoted as \( n! \)) is the product of all positive integers less than or equal to \( n \).  
- For \( n = 0 \), \( n! \) is defined as 1.

---

### **🔍 Example Input/Output**

#### **Example 1**  
**Input:**  
```
Enter a number: 5
```  
**Output:**  
```
Factorial of 5 is 120
```

#### **Example 2**  
**Input:**  
```
Enter a number: 0
```  
**Output:**  
```
Factorial of 0 is 1
```

#### **Example 3**  
**Input:**  
```
Enter a number: 7
```  
**Output:**  
```
Factorial of 7 is 5040
```

---

### **💡 Hints**  
- **Recursive Approach:**  
  - Use the formula:  
    \[
    n! = n \times (n-1)! \quad \text{for } n \geq 1, \quad \text{and} \quad 0! = 1
    \]
  - In Python, you can define a function like:  
    ```python
    def factorial(n):
        if n == 0:
            return 1
        else:
            return n * factorial(n-1)
    ```
- **Iterative Approach:**  
  - Use a loop to multiply numbers from 1 to \( n \).  
- Choose any approach and any language (Python, C++, Java, etc.).

---

### **📝 Your Task**  
- Write your solution using **any programming language**.  
- Save your file as `day16_factorial.[ext]` (for example, `day16_factorial.py`).

---

### **🌟 Motivational Quote of the Day**  
*"Courage is not the absence of fear, but the triumph over it."* – Nelson Mandela

---

### **😂 Echo’s Dad Joke of the Day (if you need a smile)**  
*"Why did the recursive function go to therapy?"*  
Because it couldn’t stop calling itself! 😆

---

Your code of courage has been tested! The temple doors slowly creak open, revealing the next stage of your adventure. Get ready for **Day 17**! 🚀