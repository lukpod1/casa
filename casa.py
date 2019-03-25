import matplotlib.pyplot as plt
from matplotlib.path import Path
import matplotlib.patches as pactches

cor = ''
fig = plt.figure()
ax = fig.add_subplot(111)
ax.set_xlim(-10, 10)
ax.set_ylim(-10, 10)

def gerarTriangulo(cor):
    vertices = [(1, 1),
                (3,3),
                (5, 1),
                (0., 0.), ]
    comandos = [Path.MOVETO,
                Path.LINETO,
                Path.LINETO,
                Path.CLOSEPOLY, ]
    path = Path(vertices, comandos)
    patch = pactches.PathPatch(path, facecolor=cor, lw=2)
    ax.add_patch(patch)


def gerarFrente(cor):
    vertices = [(1, 1),
                (1, -4),
                (5, -4),
                (5, 1), ]
    comandos = [Path.MOVETO,
                Path.LINETO,
                Path.LINETO,
                Path.LINETO, ]
    path = Path(vertices, comandos)
    patch = pactches.PathPatch(path, facecolor=cor, lw=2)
    ax.add_patch(patch)


def gerarTelhado(cor):
    vertices = [(3, 3),
                (6, 6),
                (7.8, 3.8),
                (5, 1), ]
    comandos = [Path.MOVETO,
                Path.LINETO,
                Path.LINETO,
                Path.LINETO, ]
    path = Path(vertices, comandos)
    patch = pactches.PathPatch(path, facecolor=cor, lw=2)
    ax.add_patch(patch)


def gerarLateral(cor):
    vertices = [(7.8, 3.8),
                (7.8, -1.5),
                (5, -4),
                (5, 1), ]
    comandos = [Path.MOVETO,
                Path.LINETO,
                Path.LINETO,
                Path.LINETO, ]
    path = Path(vertices, comandos)
    patch = pactches.PathPatch(path, facecolor=cor, lw=2)
    ax.add_patch(patch)


def gerarPorta(cor):
    vertices = [(2.5, -4),
                (2.5, -2),
                (3.5, -2),
                (3.5, -4), 
                ]
    comandos = [Path.MOVETO,
                Path.LINETO,
                Path.LINETO,
                Path.LINETO, 
                ]
    path = Path(vertices, comandos)
    patch = pactches.PathPatch(path, facecolor=cor, lw=2)
    ax.add_patch(patch)


def gerarJanela():
    vertices = [(5.8, 0),
                (5.8, -2),
                (7.5, -0.6),
                (7.5, 1.5),
                (0., 0.), ]
    comandos = [Path.MOVETO,
                Path.LINETO,
                Path.LINETO,
                Path.LINETO,
                Path.CLOSEPOLY, ]
    path = Path(vertices, comandos)
    patch = pactches.PathPatch(path, facecolor='white', lw=2)
    ax.add_patch(patch)


def gerarCruzDaJanela():
    vertices = [(6.7, -1.2),
                (6.7, 0.8),
                # (6.2, 1.07),
                # (6.5, 1.5),
                # (6.2, 1.07),
                # (5.8, 0.50), 
                ]
    comandos = [Path.MOVETO,
                Path.LINETO,
                # Path.MOVETO,
                # Path.LINETO,
                # Path.MOVETO,
                # Path.LINETO, 
                ]
    path = Path(vertices, comandos)
    patch = pactches.PathPatch(path, facecolor='white', lw=2)
    ax.add_patch(patch)

def gerarCasa():
    gerarTriangulo('blue')
    gerarFrente('blue')
    gerarTelhado('Brown')
    gerarLateral('blue')
    gerarPorta('yellow')
    gerarJanela()
    gerarCruzDaJanela()
    plt.show()

gerarCasa()



