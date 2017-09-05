import matplotlib.pyplot as plt
#plt.ion()
F = [32,212]
C = [0,100]

plt.title('Convert C to F')
plt.ylabel('degree C')
plt.xlabel('degree F')
#plt.xlim(32,212)
#plt.ylimit()
plt.grid(True)

plt.scatter(F,C,c = 'pink')
plt.show()