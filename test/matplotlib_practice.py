import matplotlib.pyplot as plt
import pandas as pd
'''
x = [1,2,3,4]
y = [10,20,25,30]

plt.plot(x,y)
plt.savefig("plot.png")
plt.show()
'''
'''
x = [1,2,3,4]
y = [10,20,25,30]
plt.plot(x,y)
plt.xlabel('X-axis')
plt.ylabel("Y-axis")
plt.title("Simple Line Plot")
plt.show()
'''
'''
x = [1,2,3,4]
y1 = [10,20,25,30]
y2 = [15,18,22,28]
plt.plot(x,y1,label='Line 1')
plt.plot(x,y2,label = 'Line 2')
plt.xlabel("X-axis")
plt.ylabel("values")
plt.title("Multiple Line Plot")
plt.legend()
plt.show()
'''
'''
names = ['A', 'B','C','D']
marks = [75, 82, 90, 68]
plt.bar(names,marks)
plt.xlabel("Students")
plt.ylabel("Marks")
plt.title("Student Marks")
plt.show()
'''
'''
marks = [75,82,90,68,85,78,92,88]
plt.hist(marks)
plt.xlabel("Marks")
plt.ylabel("Frequency")
plt.title("Marks Distribution")
plt.show()
'''
'''
labels = ['CSE','ECE','EEE','ME']
students = [40,30,20,10]
plt.pie(students, labels=labels,autopct='%1.1f%%')
plt.title("Department-wise Student Distribution")
plt.show()'''
'''
x = [1,2,3,4,5]
y = [10,15,20,25,30]
plt.scatter(x,y)
plt.xlabel("x Values")
plt.ylabel("Y Values")
plt.title("Scatter Plot")
plt.show()
'''

'''
data ={
    'Name':['A','B','C','D'],
    'Marks':[75,82,90,68]
}
df = pd.DataFrame(data)
df.plot(x='Name', y ='Marks',kind='bar')
plt.title("Marks using Pandas")
plt.show()'''

names = ['A', 'B', 'C', 'D'] 
marks = [75, 82, 90, 68] 
plt.bar(names, marks) 
plt.axhline(y=40) 
plt.xlabel('Students') 
plt.ylabel('Marks') 
plt.title('Student Performance') 
plt.show() 