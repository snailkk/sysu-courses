import matplotlib.pyplot as plt
p = [1, 1, 2/3, 0.75, 4/5, 5/6, 5/7, 6/8, 6/9, 7/10]
r = [1/7, 2/7, 2/7, 3/7, 4/7, 5/7, 5/7, 6/7, 6/7, 1]

plt.plot(r, p, linewidth=2)
plt.title("Precision-Recall Curve", fontsize=20)
plt.xlabel("Recall", fontsize=12)
plt.ylabel("Precision", fontsize=12)
plt.tick_params(axis='both', labelsize=10)
plt.show()
