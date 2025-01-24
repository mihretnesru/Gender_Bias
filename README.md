# 💼 Bayesian Gender Bias Detector in Job Descriptions

This project implements a **Bayesian classifier** to identify gender-coded language in job descriptions. By analyzing the presence of **feminine-coded** and **masculine-coded** words, the tool evaluates whether job descriptions lean toward feminine or masculine language, promoting awareness of potential gender biases in hiring practices.

---

## 📜 Overview

Job descriptions can unintentionally contain gender-coded language, potentially discouraging certain candidates from applying. This tool:
- Uses **Naive Bayes** to classify job descriptions as **feminine-coded** or **masculine-coded** based on predefined word lists.
- Aims to highlight and mitigate gender biases in job descriptions to create more inclusive hiring practices.

---

## ⚙️ Features

1. **Predefined Word Lists**:
   - **Feminine-coded words**: Words associated with warmth, collaboration, and nurturing (e.g., *compassion*, *nurture*, *inclusive*).
   - **Masculine-coded words**: Words linked to dominance, independence, and assertiveness (e.g., *aggressive*, *fearless*, *leader*).

2. **Custom Text Preprocessing**:
   - Removes punctuation, stop words, and converts text to lowercase.
   - Tokenizes job descriptions into words for analysis.

3. **Naive Bayes Classification**:
   - Calculates the probability of a job description being feminine- or masculine-coded based on word frequencies.
   - Provides insights into how gender-coded language impacts the overall classification.

4. **User Configurability**:
   - Easily add or modify the predefined feminine and masculine word lists.
   - Test the model on custom job description datasets.

---

## 🛠 Installation and Usage

### Prerequisites
- Python 3.x
- Required libraries: `pandas`, `numpy`, `string`
