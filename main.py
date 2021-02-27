#function of main
def main():
  #define function width
  def calcWidth(r,p):
    #equation for width using perimeter and ratio
    return p/(2*(r+1))
  #define function length
  def calcLength(r,w):
    #equation for length using width and ratio
    return r*w

#obtain ratio from user
  ratio = float (input ('Please enter ratio of length to width for the picture frame '))

#obtain perimeter from user
  perimeter = float (input ('Please enter the length of the wire for picture frame '))

#calculate width and lenth using the following 
  width = calcWidth(ratio, perimeter) 
  length = calcLength(ratio,width)

#output the width and length
  print ('The frame dimensions are', width, 'X', length)

#close main function
main()
