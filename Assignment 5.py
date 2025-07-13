# Create a Dictionary of Student Marks

students={'Shreya':98,'Adam':67,'Noura':78,'Alex':85,'Lily':59,'Teymour':100}
st=input("Enter Student Name: ")
if st in students:
    print(students[st])
else:
    print("Student Not Found")


# Demonstrate List Slicing

l=list(range(1,11))
print('Original List:',l)
n=l[:5]
print('Extracted five elements:',n)
n1=l[4::-1]
print('Reversed extracted elements:',n1)
