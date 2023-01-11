from vedo import Mesh
from numpy import array, arange
from numpy.random import random

from Open3dFactory import Open3dFactory
from Open3dVisualizer import Open3dVisualizer


# 1. Create the Factory, bind it to a new Database
factory = Open3dFactory(database_name='mesh',
                        remove_existing=True)

# 2. Add objects to the Factory, then launch the Visualizer
armadillo = Mesh('armadillo.obj')
factory.add_mesh(positions=armadillo.points(),
                 cells=armadillo.cells(),
                 at=0,
                 alpha=0.8,
                 scalar_field=armadillo.points()[:, 1],
                 wireframe=True)
factory.add_mesh(positions=armadillo.points(),
                 cells=armadillo.cells(),
                 at=1,
                 c='green',
                 wireframe=True)
factory.add_points(positions=armadillo.points(),
                   at=2,
                   point_size=3,
                   alpha=0.8,
                   scalar_field=armadillo.points()[:, 1])
factory.add_arrows(positions=armadillo.points()[0:5],
                   vectors=armadillo.normals()[0:5] * 2,
                   at=2,
                   alpha=0.8,)
Open3dVisualizer.launch(database_path=factory.get_path(),
                        offscreen=False,
                        fps=20)

# 3. Run a few steps
dofs = armadillo.points().shape
A = arange(-3, 3, 0.1)
i = len(A) // 2
for step in range(200):
    factory.update_mesh(object_id=0,
                        positions=armadillo.points() + 0.1 * random(dofs))
    factory.update_mesh(object_id=1,
                        positions=armadillo.points() + 0.1 * random(dofs))
    factory.update_points(object_id=2,
                          positions=armadillo.points() + 0.1 * random(dofs))
    factory.update_arrows(object_id=3,
                          vectors=armadillo.normals()[0:5] * A[i])
    i = (i + 1) % len(A)
    if step == 100:
        print('change')
        factory.update_mesh(object_id=0,
                            scalar_field=armadillo.points()[:, 2],
                            wireframe=False,
                            alpha=0.8)
        factory.update_mesh(object_id=1,
                            c='yellow4',
                            alpha=0.9,
                            wireframe=False)
        factory.update_points(object_id=2,
                              alpha=0.5,
                              point_size=6,
                              scalar_field=armadillo.points()[:, 2])
        factory.update_arrows(object_id=3,
                              c='blue',
                              alpha=0.6)
    factory.render()
factory.close()