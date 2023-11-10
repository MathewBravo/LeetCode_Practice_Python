from typing import List
def longestCommonPrefix(strs: List[str] ) -> str:
    if not strs:
        return ""
    
    # Find the shortest string in strs
    min_str = min(strs, key=len)
    
    for i in range(len(min_str)):
        char = min_str[i]
        for string in strs:
            if string[i] != char:
                return min_str[:i]
    
    return min_str

    
longestCommonPrefix(["dog","racecar","car"])