## 125. Valid Palindrome

### 信息卡片

- 时间：2021-04-13
- 题目链接：https://leetcode.com/problems/valid-palindrome/
- tag：`string`

### 题目描述

```
Given a string s, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

Example 1:
Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.

Example 2:
Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.

Constraints:
1 <= s.length <= 2 * 10^5
s consists only of printable ASCII characters.
```

### 代码

```python
class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        l, r = 0, len(s)-1
        while(l<r):
            while l<r and not s[l].isalnum():
                l=l+1
            while r>l and not s[r].isalnum():
                r=r-1
            if s[l].lower() != s[r].lower():
                return False
            l = l + 1
            r = r - 1
        return True
```
