## **Day 30: The Final Cipher – CodeQuest Ka Ultimate Challenge!** 🔥🔐

### **📜 Kahani / Story**  
Tum ab Mysterious Island ke sabse gehre jungle mein pahunche ho, jahan ek ancient terminal hai jo multiverse bachane ka ultimate secret rakhta hai.  
Echo, Nariyal Bhai, aur Mayur sab excited hain, lekin The Glitch ke andhere saaye abhi door nahi.  
Echo kehta hai,  
*"Yaar, ab humara final cipher solve karna hai – ek aisa puzzle jo pure CodeQuest ka climax hai! Tumhe ek string milegi jisme har character ko ek fixed offset se shift kiya gaya hai. Tumhe sahi offset dekh kar, original message recover karna hai!"*  
Nariyal Bhai thoda cheekhta hai,  
*"Bas, ekdum simple – thoda dimaag laga aur dekh kaise sab set ho jata hai!"*  
Mayur dramatic style mein add karta hai,  
*"Yeh challenge tumhare college assignments se zyada important hai – kyunki yeh tumhe future ka roadmap dega!"*

---

### **🎯 Challenge: Ultimate Cipher Decoder / Final Message Ka Raaz**  
Write a program that:  
1. **Takes a ciphered string and a shift value as input.**  
2. **Decodes the string by shifting each letter back by the given offset.**  
3. **Prints the decoded original message.**

*Notes:*  
- Only alphabetical characters should be shifted; numbers and symbols remain unchanged.  
- Handle both uppercase and lowercase letters appropriately.  
- Agar shift se letter 'A' ya 'a' se pehle chala jaye, toh wrap around karna hai.

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
- Use functions like `ord()` and `chr()` in Python to convert characters to ASCII codes and vice versa.  
- Consider writing a helper function that shifts a single character and returns the new character.  
- For letters, ensure the shift wraps around the alphabet (e.g., 'A' shifted by 1 becomes 'Z' when moving backwards).  
- In other languages, similar techniques with character manipulation will work.

---

### **📝 Tumhara Task**  
- Write your solution in **any programming language** (Python, C++, Java, etc.).  
- Save your file as `day30_final_cipher.[ext]` (e.g., `day30_final_cipher.py`).

---

### **🌟 Motivational Quote / Uplifting Message**  
*"Jab challenges bade ho, toh himmat aur dimaag ko aur tez chalao. Code likho, mistakes se seekho, aur multiverse ko bachao!"* 🚀

---

### **😂 Echo’s Dad Joke of the Day**  
*"Why did the coder bring sunglasses to the office?"*  
Kyunki uske code mein **too many bright ideas** chamak rahe the! 😆

---

The ultimate cipher holds the key to saving the multiverse and unlocking your true coding potential. Ab tumhare paas sab kuch hai – apne dimaag ko jagao, aur final challenge ko solve karo!  
Ready for the next step in your CodeQuest journey? Let’s go!