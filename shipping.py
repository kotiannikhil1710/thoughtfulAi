def sort(width, height, length, mass):
  '''
    This function will sort the packages based on the given dimensions and mass
    :param width: width of the package
    :param height: height of the package
    :param length: length of the package
    :param mass: mass of the package
    :return: string with the type of shipping
  '''
  bulky=0
  heavy=0
  if(height==''):
    height=0
  if(width==''):
    width=0
  if(length==''):
    length=0
  dimension=width*height*length

  if (height>150 or width>150 or length>150 or dimension >=1000000):
    bulky=1
  if mass>=20:
    heavy=1
  if (bulky==1) and (heavy==1):
    return "Rejected: Bulky AND Heavy"
  elif (bulky==1 or heavy==1):
    return "Special: Bulky OR Heavy"
  else:
    return "Standard: No Bulky No Heavy"

def main():
  width1,height1,length1,mass1=30,10,40,15
  print(f"Shipping 1st batch : {sort(width1,height1,length1,mass1)}")
  width2,height2,length2,mass2=30,10,40,25
  print(f"Shipping 2nd batch : {sort(width2,height2,length2,mass2)}")
  width3,height3,length3,mass3=500,10,40,13
  print(f"Shipping 3rd batch : {sort(width3,height3,length3,mass3)}")
  width4,height4,length4,mass4=150,100,300,35
  print(f"Shipping 4th batch : {sort(width4,height4,length4,mass4)}")
  height5=''
  width5,length5,mass5=1000,3000,3
  print(f"Shipping 5th batch : {sort(width5,height5,length5,mass5)}")


if __name__=="__main__":
  main()