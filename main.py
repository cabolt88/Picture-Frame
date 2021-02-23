#Get ratio of length to width from user
ratio = float (input ('Please enter ratio of length to width for the picture frame '))
#Get total length of wire frame (perimeter) from user
perimeter= float (input ('Please enter total length of wire for picture frame '))
#calculate width
width = perimeter / (2* (ratio +1))
#calulate length
length = ratio * width
#output frame dimension width and length 
print ('The frame dimensions are', width, 'X', length)