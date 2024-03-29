Install
=======

Prerequisites
-------------

The **SSD** project has the following dependencies:

.. table::
    :widths: 20 20 10 30

    +------------------------+-----------------------+--------------+----------------------------------------------------+
    | **Package**            | **Dependency**        | **Type**     | **Install**                                        |
    +========================+=======================+==============+====================================================+
    | ``SSD.Core.Storage``   | :Peewee:`Peewee <>`   | **Required** | :guilabel:`pip install peewee`                     |
    |                        +-----------------------+--------------+----------------------------------------------------+
    |                        | :Numpy:`Numpy <>`     | **Required** | :guilabel:`pip install numpy`                      |
    +------------------------+-----------------------+--------------+----------------------------------------------------+
    | ``SSD.Core.Rendering`` | :Vedo:`Vedo <>`       | **Required** | :guilabel:`pip install vedo`                       |
    |                        +-----------------------+--------------+----------------------------------------------------+
    |                        | :Open3D:`Open3D <>`   | **Required** | :guilabel:`pip install open3d`                     |
    +------------------------+-----------------------+--------------+----------------------------------------------------+
    | ``SSD.SOFA``           | :SP3:`SofaPython3 <>` | Optional     | :SP3:`Follow instructions <menu/Compilation.html>` |
    +------------------------+-----------------------+--------------+----------------------------------------------------+

.. warning::
    The :SOFA:`SOFA <>` Python bindings are not required to use the ``SSD.Core`` packages, but they are obviously
    required to use the ``SSD.SOFA.Storage`` and ``SSD.SOFA.rendering`` packages. Those two packages will be ignored
    during the installation process if :SOFA:`SOFA <>` Python bindings are not found by the interpreter.

Install
-------

Install with pip
""""""""""""""""

The **SSD** project is registered on :PyPi:`PyPi <>`, thus it can easily be installed using :guilabel:`pip`:

.. code-block:: bash

    $ pip3 install SimulationSimpleDatabase

Then, you should be able to run:

.. code-block:: bash

    $ pip3 show SimulationSimpleDatabase

.. code-block:: python

    import SSD


Install from sources
""""""""""""""""""""

Start by cloning the **SSD** source code from its Github repository:

.. code-block:: bash

    $ git clone https://github.com/RobinEnjalbert/SimulationSimpleDatabase.git
    $ cd SimpleSimulationDatabase

Then, you have two options to install the project:

 * (USERS) either by using :guilabel:`pip` to install it as non-editable in the site-packages;

    .. code-block:: bash

        $ pip3 install .

 * (DEVELOPERS) either by running the ``setup_dev.py`` script to link it as editable in the site-packages.

    .. code-block:: bash

        # Create a link to SSD packages in the site-packages
        $ python3 setup_dev.py set

        # Remove the link to SSD packages in the site-packages
        $ python3 setup_dev.py del

Then, you should be able to run:

.. code-block:: bash

    # Only if installed with pip
    $ pip3 show SimulationSimpleDatabase

.. code-block:: python

    # In both options
    import SSD
