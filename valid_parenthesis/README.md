This is the valid parenthesis problem:

---
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

- Open brackets must be closed by the same type of brackets.
- Open brackets must be closed in the correct order.
- Every close bracket has a corresponding open bracket of the same type.

---

Approach:
- initiate an empty stack (we will use stack because it will allow us to keep the idea of last in first out - that is for every closing bracket, we will check whether the most recent bracket is an opening bracket)
- Go through all the characters in the stack
- whenever we come across an opening bracket, we append it to the stack. 
- whenever we come across a closing bracket;

-> we make sure the stack is not empty. 

-> And also that the most recent (or the parenthesis at the top of the stack connects can be closed by the bracket)

- If the two above conditions are met, pop the bracket. 
