Keyboard Row Words Finder
Problem Description
Given an array of strings words, return the words that can be typed using letters from only one row of an American keyboard.

Keyboard Rows:
First Row: "qwertyuiop"
Second Row: "asdfghjkl"
Third Row: "zxcvbnm"
Note:

The comparison is case-insensitive — uppercase and lowercase letters are treated as the same.


The Solution Logic:

First, we create three sets containing letters from each keyboard row
For each word we:

Convert it to lowercase (so 'A' and 'a' are treated the same)
Check if all its letters appear in any single row
If yes, we keep the word; if no, we skip it




Why it Works:

Using sets makes it easy to check if all letters belong to one row
The issubset() function checks if all letters of the word are contained in a keyboard row
We check against all three rows for each word
We keep the original word (with its original case) in our results