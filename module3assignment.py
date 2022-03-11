# Module 3 Assignment
# Casey Savoie

myfile= open('question.txt','r+')

weather = myfile.read()

prediction = input(weather)

myfile.write(prediction)

myfile.close()

