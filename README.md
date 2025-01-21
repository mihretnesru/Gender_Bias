# Bayesian Gender Bias Detection in Job Descriptions
This project uses a Bayesian approach to detect gender bias in job descriptions based on predefined lists of "feminine" and "masculine" coded words. The goal is to predict whether a given job description is more aligned with feminine or masculine stereotypes. The model processes the job descriptions, calculates probabilities based on the frequency of gendered words, and provides a prediction of the job description’s bias.

Features
Bayesian Classification: Utilizes Bayesian probabilities to predict gender bias based on the occurrence of feminine and masculine words.
Text Preprocessing: Tokenizes job descriptions, removes stop words, and normalizes text for better accuracy.
Word Frequency Counting: Counts the frequency of feminine and masculine words in job descriptions.
Bias Prediction: Classifies job descriptions as either "feminine" or "masculine" based on the calculated probabilities.
