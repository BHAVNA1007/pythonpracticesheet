'''
130 Find the maximum occurring word. 
S = "a b a c a" a

'''

s = input('Enter string: ')
words = s.split()

m_count = 0
m_word = ''

for i in words:
   count = 0
   for j in words:
       if i == j:
          count += 1

   if count > m_count :
       m_count = count
       m_word = i

print("maximum occurring word", m_word) 
