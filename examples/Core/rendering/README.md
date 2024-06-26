# Examples - SSD.Core.Rendering

This repository contains a few examples that give a great overviews of the **rendering** features.

It is recommended to inspect and run the python scripts following this order:

* ``visualization.py``: discover all visual object types (how to create and update them).
* ``replay.py``: how to replay a simulation from a *Database*.
* ``offscreen.py``: an example of off-screen rendering.
* ``several_factories.py``: how to manage several *Factories* with a single *Visualizer*.
* ``several_factories_offsceen.py``: how to manage several *Factories* with a single *Visualizer* in off-screen mode.

Run the examples using ``python3 <example_name>.py <backend>`` with backend being either 'vedo' (by default) or 'open3d'.
