def sorted_reading(r):
  a = int(input("enter the reading"))
  l = str(a)
  order = sorted(l)
  n = 0
  for i in range(len(l)):
    if (order[i] == l[i]):
      n += 1
    else:
      print()
      
def checking_unitsplace():
  
  first = int(input("enter starting range"))
  last  = int(input("enter the last range")) 
  
  list = [i for i in range(first,last)if(i % 10 ) > (i // 10)]
  
  if a in list:
    for j in len(list):
      if a == last - 1 :
        print(list[len(list) - 2],list[0])
        break
      else:
        print(list[j - 1],list[j + 1])
        break
  else:
    print("invalid input")
   
    
