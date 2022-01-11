letter = '''\nDear <Name>,
You are selected for the final round of the interview.
All the best for your upcoming interview.

Thanks and Regards.
Date : <Date>'''

name = input("Enter your name : ")
date = input("Enter today's date : ")

# String "REPLACE" function
letter = letter.replace("<Name>" , name)
letter = letter.replace("<Date>" , date)

print(letter)