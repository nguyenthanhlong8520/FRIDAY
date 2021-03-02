# importing modules  
import matplotlib.pyplot as plt 
import numpy as np 
  
# assigning x and y coordinates 
language = ['C','C++','Java','Python'] 
users = [80,60,130,150] 
  
# depicting the visualization 
index = np.arange(len(language)) 
plt.bar(index, users, color='green') 
plt.xlabel('Users') 
plt.ylabel('Language') 
plt.xticks(index, language) 
  
# displaying the title 
plt.title(label='Number of Users of a particular Language',  
          fontweight=10,  
          pad='2.0') 

plt.show()