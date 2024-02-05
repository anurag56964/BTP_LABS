# //////////////// STUDENT INFO /////////////////

# Student Name : Anurag Das
# Student ID   : 126031228
# Email        : adas35@myseneca.ca

# ///////////////////////////////////////////////

def if_prime(num):
  """Check If Its A Prime Num"""
  if num <= 1:
    return False
  for i in range(2, int(num**0.5) + 1):
    if num % i == 0:
      return False;
  return True

def getPrimeNumbers(n):
  """Return List Of Prime Num Between 2 & n"""
  return [num for num in range(2, n+1) if if_prime(num)]

n = input("Please Enter The Last Number Of Range = ")
n = int(n)
print(f"Prime Number In The Range 2 - {n}: ", getPrimeNumbers(n))
