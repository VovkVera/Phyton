def count_symbols(w):
   d={}
   keys=set(w)
   for k in keys:
     d[k]=0
   for k in keys:
      for b in w:
         if k==b:
           d[k]=d[k]+1
   
   return d
      
w = input()
if len(w)>0:
  print(count_symbols(w))
else:
  print("let your word be longer")


### palindromic ####
def is_palindromic(s): return all(s[i] == s[~i] for i in range(len(s) / 2)) 
