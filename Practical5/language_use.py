#build a dictionary of languages and their use in the world
#generate a bar chart of different percentages of computerlanguages used in the world
import matplotlib.pyplot as plt
import numpy as np
language_using={'Javacript':62.3,'HTML':52.9,'Python':51,'SQL':51,'TypeScript':38.5}
languages=list(language_using.keys())# store the key values of the dictionary in a list
values=list(language_using.values())# store the values of the dictionary in a list
plt.title('Percentage of computer languages used in the world')
plt.xlabel('Languages')
plt.ylabel('Percentage')
plt.bar(languages,values,color='green')

plt.show()
language='JavaScript'#the language type that can be modified(JavaScript,HTML,Python,SQL,TypeScript)
print(language_using[language])