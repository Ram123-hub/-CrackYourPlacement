# abin-Karp Algorithm for Pattern Searching
# Last Updated : 06 Sep, 2023
# Given a text T[0. . .n-1] and a pattern P[0. . .m-1], write a function search(char P[], char T[]) that prints all occurrences of P[] present in T[] using Rabin Karp algorithm. You may assume that n > m.

# Examples: 

# Input:  T[] = “THIS IS A TEST TEXT”, P[] = “TEST”
# Output: Pattern found at index 10

# Input:  T[] =  “AABAACAADAABAABA”, P[] =  “AABA”
# Output: Pattern found at index 0
#               Pattern found at index 9
#               Pattern found at index 12


def rabin_karp(text, pattern):

    d = 256
    
    q = 101
    
    n = len(text)
    m = len(pattern)
    p = 0    
    t = 0    
    h = 1
    

    for i in range(m-1):
        h = (h * d) % q
  
    for i in range(m):
        p = (d * p + ord(pattern[i])) % q
        t = (d * t + ord(text[i])) % q
    
    for i in range(n - m + 1):
      
        if p == t:
           
            match = True
            for j in range(m):
                if text[i + j] != pattern[j]:
                    match = False
                    break
            if match:
                print(f"Pattern found at index {i}")
        
       
        if i < n - m:
            t = (d * (t - ord(text[i]) * h) + ord(text[i + m])) % q
            
          
            if t < 0:
                t = t + q


text = "ABCCDDAEFG"
pattern = "CDD"
rabin_karp(text, pattern)

        

