some_list=['a','b','c', 'b','d','m','n','n' ]
#primero ordenamos
sorted_list=sorted(some_list)

for i,letra in enumerate(sorted_list):
  if letra == some_list[i+1]:
    print(letra)
  else: continue