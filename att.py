import numpy as np
import matplotlib.pyplot as plt
from matplotlib.path import Path
import matplotlib.patches as pactches

# vertices = [
#     (2, 4),
#     (1, 2),
#     (3, 0),
#     (5, 1),
#     (6.5, 3),

#     (1,2),
#     (3.5,2.5),
#     (5,1)
# ]
# comandos = [
#     Path.MOVETO,
#     Path.LINETO,
#     Path.LINETO,
#     Path.LINETO,
#     Path.LINETO,
#     Path.MOVETO,
#     Path.LINETO,
#     Path.LINETO,
# ]
data1 = [9,5,2,4,6,8]
data2 = [9.8,4.8,1.8,3.8,5.8,7.8]
x = 10*np.array(range(len(data1)))

plt.plot( x, data1, 'go') # green bolinha
plt.plot( x, data1, 'k:', color='orange') # linha pontilha orange

plt.plot( x, data2, 'r^') # red triangulo
plt.plot( x, data2, 'k--', color='blue')  # linha tracejada azul

plt.axis([-10, 60, 0, 11])
plt.title("Mais incrementado")

plt.grid(True)
plt.xlabel("eixo horizontal")
plt.ylabel("que legal")
plt.show()


# import matplotlib.pyplot as plt
# from matplotlib.path import Path
# import matplotlib.patches as pactches

# vertices = [
#     (2, 4),
#     (1, 2),
#     (3, 0),
#     (5, 1),
#     (6.5, 3),

#     (1,2),
#     (3.5,2.5),
#     (5,1)
# ]
# comandos = [
#     Path.MOVETO,
#     Path.LINETO,
#     Path.LINETO,
#     Path.LINETO,
#     Path.LINETO,
#     Path.MOVETO,
#     Path.LINETO,
#     Path.LINETO,
# ]

# path = Path(vertices, comandos)
# patch = pactches.PathPatch(path, facecolor='white', lw=2)
# fig = plt.figure()
# ax = fig.add_subplot(111)
# ax.add_patch(patch)
# ax.set_xlim(-10, 10)
# ax.set_ylim(-10, 10)
# plt.show()
