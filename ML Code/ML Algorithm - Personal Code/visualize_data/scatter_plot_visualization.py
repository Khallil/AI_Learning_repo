import numpy as np
import matplotlib.pyplot as plt

# Fixing random state for reproducibility
np.random.seed(19680801)
'''
dataset = [
[3.393533211,2.331273381,0],
[3.110073483,1.781539638,0],
[1.343808831,3.368360954,0],
[3.582294042,4.67917911,0],
[2.280362439,2.866990263,0],
[7.423436942,4.696522875,1],
[5.745051997,3.533989803,1],
[9.172168622,2.511101045,1],
[7.792783481,3.424088941,1],
[7.939820817,0.791637231,1],
[2.771244718,1.784783929,2],
[1.728571309,1.169761413,2],
[3.678319846,2.8128135,2],
[3.961043357,2.61995032,2],
[2.999208922,2.209014212,2],
[7.497545867,3.162953546,2],
[9.00220326,3.339047188,2],
[7.444542326,0.476683375,2],
[10.12493903,3.234550982,2],
[6.642287351,3.319983761,2]]
'''
dataset = [
[2.327868056,	2.458016525,	-1],
[3.032830419,	3.170770366,	-1],
[4.485465382,	3.696728111,	-1],
[3.684815246,	3.846846973,	-1],
[2.283558563,	1.853215997,	-1],
[7.807521179,	3.290132136,	1],
[6.132998136,	2.140563087,	1],
[7.514829366,	2.107056961,	1],
[5.502385039,	1.404002608,1],
[7.432932365,	4.236232628,	1]]


x = [row[0] for row in dataset]
y = [row[1] for row in dataset]
classes = [row[2] for row in dataset]

plt.scatter(x, y, c=classes, alpha=0.5)
plt.show()