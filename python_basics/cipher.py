import numpy as np 

letter =np.array( ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"])
number = np.array(range(1, len(letter)+1))

text = input("Enter A text: ").split()

text = np.array([text])

matrix = np.array([[1,-1],[-5,2]])

for i in text:
    for j in range(1, len(letter)):
        if i == letter[j]:
            for h in range(1, len(number)):
                if letter[j] == number[h]:
                    print(f"Text Encoded by {number[h]}")
