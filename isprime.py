def isPrime(a,b):
 
  print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")

  arePrime : False
  i = 2
  while i < a and a % i != 0 and i < b and b % i != 0 :
    i = i + 1

  if i == a and i == b:
    arePrime = True
    print("Les nombres ", a, b, bool(arePrime), " sont premierS ! Fantastique !")
  else:
    print("Un des nombres n'est pas un nombre premier. ",bool(arePrime))
  
  return arePrime
    