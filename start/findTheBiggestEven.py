def highest_even(list):
  
  ordered=sorted(list)
 
  for numero in ordered:
    if numero%2==0:
      numeroPar=numero
  return f"el numero Par más alto es: {numeroPar}" 
  
    
      
    

    
  



print(highest_even([10,1,2,4,8,7,9,11,13,15,16,22,1,2,12]))