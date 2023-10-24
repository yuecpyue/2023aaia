#week07-6
s = "abcdabcde"#字串str
d = {}#字典dict
for c in s:
  if c in d:
    d[c]=d[c]+1
  else:
    d[c]=1
  print('現在讀到的字母', c,"字典變成", d)