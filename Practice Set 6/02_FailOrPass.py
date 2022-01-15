sub1 = int(input("Enter subject 1 marks : "))
sub2 = int(input("Enter subject 2 marks : "))
sub3 = int(input("Enter subject 3 marks : "))

if(sub1<33 or sub2<33 or sub3<33):
    print("Failed because you scored less than 33% in one of the subject.")
elif ((sub1+sub2+sub3)/3)<40:
    print("Failed, because your total percentage is less than 40%.")
else:
    print("Congralution, you have passed the examination.")