def first_non_repeating(s):
    for i in range(len(s)):
        current_char = s[i]
        is_repeating = False
        
        for j in range(len(s)):
            if i != j and current_char == s[j]:
                is_repeating= True
                break
        
        if not is_repeating:
            return current_char
    return '$'
    
s1 = "aabbccdd"
print(first_non_repeating(s1))
    
