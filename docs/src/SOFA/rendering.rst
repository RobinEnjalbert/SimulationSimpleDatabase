SOFA Rendering
==============

Specificity
-----------

The **SSD** project provides a compatible *Factory* with :SOFA:`SOFA <>` framework.
As in the storage package, there are several advantages with this specialized *Factory*:

 * the recording can be launched whether the simulation is driven by the :SOFA:`SOFA <>` GUI or by a Python
   interpreter;
 * callbacks can be defined to record automatically Data fields of SOFA components;
 * the *Visualizer* provides a way to visualize SOFA simulations even if the GUI is not used.

.. note::
    The SOFA version of the *Factory* is able to record data at each time step since it inherits from
    :guilabel:`Sofa.Core.Controller`. The event corresponding to the end of the time step is therefore caught and
    triggers access to the recorded Data fields.


.. note::

    The ``SSD.SOFA.Rendering`` also includes the *Visualizers* so that users can import their tools from a single
    module, but they do not have additional features.


Record Data fields
------------------

The way to create these *Factory* and *Visualizer* is slightly different than in the ``Core`` version.
In fact, the *Factory* is considered as a SOFA component and must be added to the scene graph.
Only the root node of the scene graph should be given, the *Factory* will then create its own child node and add
itself to the graph.

Adding callbacks is very simple, since you only have to specify:

 * the adding method to use from the *Factory*;
 * the absolute path to the SOFA component in the scene graph and possibly the name of the Data field to record
   (depending on the object type).

Moreover, the rendering of the *Visualizer* (which was triggered with the call to ``render()``) is done automatically
since it is now called by the *Factory* itself.

.. warning::

    It is important to keep the *Visualizer* in your code even if you want it to be offscreen, since the
    synchronization process requires both the *Factory* and the *Visualizer*.


.. tabs::

    .. tab:: Python Interpreter

        .. code-block:: python

            import Sofa
            from SSD.SOFA.Storage.Database import Database

            # Create the root node
            root = Sofa.Core.Node('root')
            root.addObject('RequiredPlugin', pluginName=['SofaOpenglVisual', 'SofaNonUniformFem', 'SofaLoader', 'SofaConstraint',
                                                         'SofaImplicitOdeSolver', 'SofaMeshCollision', 'SofaSimpleFem'])

            # Create a falling ball
            root.addChild('ball')
            root.ball.addObject('EulerImplicitSolver')
            root.ball.addObject('CGLinearSolver')
            root.ball.addObject('MechanicalObject', name='BallMO', template='Rigid3')
            root.ball.addObject('UniformMass', totalMass=1.)

            # Add a visual model
            root.ball.addChild('visual')
            root.ball.visual.addObject('MeshObjLoader', name='Loader', filename='mesh/ball.obj')
            root.ball.visual.addObject('OglModel', name='BallOGL', src='@Loader')
            root.ball.visual.addObject('RigidMapping', input='@..', output='@.')

            # Create a new Visualizer and a new Factory (pay attention to offscreen flag)
            visualizer = VedoVisualizer(database_name='ball', remove_existing=True, offscreen=False)
            factory = VedoFactory(root=root, database=visualizer.get_database())
            factory.add_points(position_object='@ball.BallMO', animated=False,
                               at=0, c='red4', point_size=8)
            factory.add_mesh(position_object='@ball.visual.BallOGL', cell_type='triangles', animated=True,
                             at=0, c='green', alpha=0.8)
            factory.add_mesh(position_object='@ball.visual.BallOGL', cell_type='quads', animated=True,
                             at=0, c='green', alpha=0.8)
            visualizer.init_visualizer()

            # Init the scene graph and run some step of the simulation
            Sofa.Simulation.init(root)
            for _ in range(10):
                Sofa.Simulation.animate(root, root.dt.value)


    .. tab:: SOFA GUI

        .. code-block:: python

            from SSD.SOFA.Storage.Database import Database

            def createScene(root):

                # Create a falling ball
                root.addChild('ball')
                root.ball.addObject('EulerImplicitSolver')
                root.ball.addObject('CGLinearSolver')
                root.ball.addObject('MechanicalObject', name='BallMO', template='Rigid3')
                root.ball.addObject('UniformMass', totalMass=1.)

                # Add a visual model
                root.ball.addChild('visual')
                root.ball.visual.addObject('MeshObjLoader', name='Loader', filename='mesh/ball.obj')
                root.ball.visual.addObject('OglModel', name='BallOGL', src='@Loader')
                root.ball.visual.addObject('RigidMapping', input='@..', output='@.')

                # Create a new Visualizer and a new Factory (pay attention to offscreen flag)
                visualizer = VedoVisualizer(database_name='ball', remove_existing=True, offscreen=True)
                factory = VedoFactory(root=root, database=visualizer.get_database())
                factory.add_points(position_object='@ball.BallMO', animated=False,
                                   at=0, c='red4', point_size=8)
                factory.add_mesh(position_object='@ball.visual.BallOGL', cell_type='triangles', animated=True,
                                 at=0, c='green', alpha=0.8)
                factory.add_mesh(position_object='@ball.visual.BallOGL', cell_type='quads', animated=True,
                                 at=0, c='green', alpha=0.8)
                visualizer.init_visualizer()


.. hint::
    Only raw data of Data fields can be recorded with such a method, style variables will be constant by default.
    However, you can still use the ``SDD.Core`` API of the *Factory* to "manually" insert data.
    If you write your scene as a :guilabel:`Sofa.Core.Controller`, you will be able to update other data fields
    with event handlers (such as ``onAnimateBeginEvent`` or ``onAnimateEndEvent``).

    Example: **/example/SOFA/rendering/record.py** & **/example/SOFA/rendering-offscreen/record.py**
