# 📘 Python Dictionary CLI App

A simple command-line dictionary tool written in Python.  
It fetches the **definition**, **part of speech**, and **example usage** of any English word using the free [DictionaryAPI.dev](https://dictionaryapi.dev) API.

---

## 🚀 Features

- 📝 Takes any English word as input  
- 📖 Returns its meaning, part of speech, and example sentence (if available)  
- ⚠️ Handles errors gracefully for words not found  
- 🔗 Uses a free public API, no key required  

---

## 🛠️ Requirements

- Python 3.x  
- [`requests`](https://pypi.org/project/requests/) library

Install the required package:

```bash
pip install requests
```

---

## 💻 How to Run

Clone or download this script, then run it:

```bash
python main.py
```

Enter a word when prompted, and get instant results!

---

## 🧠 Sample Output

```
Enter a word: innovate

 Word: innovate
 Part of Speech: verb
 Definition: make changes in something established, especially by introducing new methods, ideas, or products.
 Example: the company's failure to diversify and innovate competitively
```

---

## 🔍 API Used

- [https://dictionaryapi.dev/](https://dictionaryapi.dev/)

---

## 📝 License

This project is for **educational and personal use**.  
The data is fetched using a public API without authentication.
