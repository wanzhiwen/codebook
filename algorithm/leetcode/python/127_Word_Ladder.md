## 127. Word Ladder

### 信息卡片

- 时间：2021-04-19
- 题目链接：https://leetcode.com/problems/word-ladder/
- tag：`string` `bfs`

### 题目描述

```
A transformation sequence from word beginWord to word endWord using a dictionary wordList is a sequence of words beginWord -> s1 -> s2 -> ... -> sk such that:
Every adjacent pair of words differs by a single letter.
Every si for 1 <= i <= k is in wordList. Note that beginWord does not need to be in wordList.
sk == endWord
Given two words, beginWord and endWord, and a dictionary wordList, return the number of words in the shortest transformation sequence from beginWord to endWord, or 0 if no such sequence exists.

Example 1:
Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]
Output: 5
Explanation: One shortest transformation sequence is "hit" -> "hot" -> "dot" -> "dog" -> cog", which is 5 words long.

Example 2:
Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log"]
Output: 0
Explanation: The endWord "cog" is not in wordList, therefore there is no valid transformation sequence.

Constraints:
1 <= beginWord.length <= 10
endWord.length == beginWord.length
1 <= wordList.length <= 5000
wordList[i].length == beginWord.length
beginWord, endWord, and wordList[i] consist of lowercase English letters.
beginWord != endWord
All the words in wordList are unique.
```

### 代码

```python
class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        def build_dict(word_list):
            d = {}
            for word in word_list:
                for i in range(len(word)):
                    tmp = word[:i] + '_' + word[i+1:]
                    d[tmp] = d.get(tmp,[]) + [word]
            return d
        
        if beginWord in wordList:
            d = build_dict(wordList)
        else:
            d = build_dict(wordList + [beginWord])
        visited = []
        queue = []
        queue.append(beginWord)
        visited.append(beginWord)
        step = 1
        count1 = 1
        count2 = 0
        while queue:
            word = queue.pop(0)
            count1 = count1 - 1
            if word == endWord:
                return step
            for i in range(len(word)):
                tmp = word[:i] + '_' + word[i+1:]
                ladder_words = d[tmp]
                for ladder_word in ladder_words:
                    if ladder_word not in visited:
                        visited.append(ladder_word)
                        queue.append(ladder_word)
                        count2 = count2 + 1
            if count1 == 0:
                step = step + 1
                count1 = count2
                count2 = 0
        return 0 
```
