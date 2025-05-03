## **Day 27: The Campus Code – Group Project Debugging!** 🎓💻

### **📜 Story / Kahani**  
Ab tum college campus par ho, jahan assignments aur group projects se sab busy hain. Par is baar, tumhara project ek secret code par based hai – jo multiverse bachane ka raaz rakhta hai!  
  
**Echo** (tumhara friendly AI assistant) kehta hai,  
*"Yaar, tumhara group project abhi tak incomplete hai. Tumhe code ke har part ko sahi se debug karna hoga, just like fixing that buggy assignment in college!"*  
  
**Nariyal Bhai** (the quirky, wise coconut) bolta hai,  
*"Arre bhai, jab coding ka tension ho, toh thoda coconut water pee lo. Tab sab set ho jayega!"*  
  
**Mayur** (tumhara dramatic sidekick) kehta hai,  
*"Group projects are like dance performances – timing aur coordination sabse important hai. Tum sab milke ye code choreograph karo!"*  
  
Lekin, **The Glitch** (villain) akele hi code mein ghus gaya hai aur sab functions ko corrupt kar diya hai. Ab tumhe un sab functions ko sahi se **debug** karna hai aur project complete karna hai!

---

### **🎯 Challenge: Group Project Debugger**  
Write a program that:  
1. **Takes a list of integers as input, representing different code module statuses** (each number symbolizes a module's performance score).  
2. **Filters out all modules with scores below a threshold (e.g., 50) – these are the buggy modules that need debugging.**  
3. **Prints the list of modules that need fixing.**

*The idea is to simulate debugging a group project: only the modules scoring 50 or above are considered working; below that, they need attention!*

---

### **🔍 Example Input/Output**

#### **Example 1**  
**Input:**  
```
Enter module scores (space-separated): 65 42 70 55 30
```  
**Output:**  
```
Modules to debug: 42 30
```

#### **Example 2**  
**Input:**  
```
Enter module scores (space-separated): 80 90 75 60
```  
**Output:**  
```
All modules are working fine!
```

#### **Example 3**  
**Input:**  
```
Enter module scores (space-separated): 45 40 35 55 48
```  
**Output:**  
```
Modules to debug: 45 40 35 48
```

---

### **💡 Hints**  
- **Input Handling:**  
  - Split the input string into individual numbers.  
- **Filtering:**  
  - Use a loop or list comprehension to filter out numbers below 50.  
- **Output:**  
  - If no module requires debugging (i.e., all scores are 50 or above), print a message indicating that everything is working fine.

---

### **📝 Tumhara Task**  
- Write your solution in **any programming language** (Python, C++, Java, etc.).  
- Save your file as `day27_campus_code.[ext]` (for example, `day27_campus_code.py`).

---

### **🌟 Motivational Quote / Uplifting Message**  
*"Group projects may be challenging, but they also teach you teamwork, resilience, and innovation – just like every coding problem!"* – Unknown

---

### **😂 Echo’s Dad Joke of the Day**  
*"Why did the programmer bring a ladder to college?"*  
Because he heard the **code had high-level functions!** 😆

---

Tumhara group project abhi bhi chal raha hai, par jab sab log milke debug karte hain, toh koi bhi bug The Glitch se bach nahi sakta! Ab ready ho jao for **Day 28**, jahan aur bhi campus-style coding challenges tumhara intezaar kar rahe hain!## **Day 28: The Secret Cipher – Caesar Cipher Ka Jadoo!** 🔐✨

### **📜 Kahani / Story**  
Mysterious Island mein aage badhte hue, tumhe ek purani scroll mili hai jisme ek rahasyamayi sandesh likha hai. Scroll kehte hai:  
*"Jisne yeh cipher decode kiya, wahi chhupa hua khazana dhoondh lega."*  

Echo ghabrata nahi, aur kehta hai,  
*"Relax, yeh bas ek Caesar Cipher hai. Thoda shift karo letters ko, aur message samne aa jayega!"*  

Nariyal Bhai halka sa muskurata hai:  
*"College assignments ki tarah, yeh cipher bhi practice se aasan ho jayega."*  

Mayur subtly add karta hai,  
*"Bas, thoda dhyan se padh aur shift samajh – baaki sab automatic ho jayega!"*

---

### **🎯 Challenge: Caesar Cipher Decoder / Cipher Ka Jadoo**  
Write a program that:  
1. **Takes a ciphered text and a shift value as input.**  
2. **Decodes the text by shifting each alphabetical character back by the given shift value.**  
3. **Prints the decoded (original) message.**

*Note:*  
- Non-alphabetical characters should remain unchanged.  
- Assume the cipher uses only English letters.

---

### **🔍 Example Input/Output**

#### **Example 1**  
**Input:**  
```
Enter cipher text: "Uifsf jt op tqppo"
Enter shift value: 1
```  
**Output:**  
```
Decoded Message: "There is no spoon"
```

#### **Example 2**  
**Input:**  
```
Enter cipher text: "Dro aesmu lbygx pyh TEWZC yfob dro vkji nyq."
Enter shift value: 10
```  
**Output:**  
```
Decoded Message: "The quick brown fox JUMPS over the lazy dog."
```

#### **Example 3**  
**Input:**  
```
Enter cipher text: "Fyyfhp fy ifbs!"
Enter shift value: 5
```  
**Output:**  
```
Decoded Message: "Attack at dawn!"
```

---

### **💡 Hints**  
- For each letter, determine its position in the alphabet and then shift it back by the provided value.  
- In Python, you can use `ord()` and `chr()` functions to manipulate ASCII values.  
- Ensure you handle both uppercase and lowercase letters appropriately.  
- If a letter shifts before 'A' or 'a', wrap around to 'Z' or 'z'.

---

### **📝 Tumhara Task**  
- Write your solution in **any programming language** (Python, C++, Java, etc.).  
- Save your file as `day28_caesar_cipher.[ext]` (e.g., `day28_caesar_cipher.py`).

---

### **🌟 Motivational Quote / Uplifting Message**  
*"Har problem ka solution hota hai, bas sahi shift dhoondna padta hai. Keep decoding and keep shining!"* 🚀

---

### **😂 Echo’s Dad Joke of the Day**  
*"Why did the letter 'B' always get invited to parties?"*  
Kyunki woh **always 'A' se shift karta rehta hai – it's all about that upgrade!** 😆

---

Scroll ka jadoo tum par chhaya hua hai – ab dekho, decoded message tumhe island ke agle raaz tak le jayega. Ab taiyaar ho jao for **Day 29** as the adventure continues!