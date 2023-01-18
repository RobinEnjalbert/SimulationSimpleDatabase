from typing import Optional

from SSD.SOFA.Storage.Database import Database
from SSD.Core.Rendering.Visualizer import Visualizer as _Visualizer


class Visualizer(_Visualizer):

    def __init__(self,
                 backend: str = 'vedo',
                 database: Optional[Database] = None,
                 database_dir: str = '',
                 database_name: Optional[str] = None,
                 remove_existing: bool = False,
                 offscreen: bool = False,
                 fps: int = 20,
                 nb_clients: int = 1):
        """
        The Visualizer is used to launch either the VedoVisualizer either the Open3dVisualizer.
        It is recommended to launch the visualizer with UserAPI.launch_visualizer() method.

        :param backend: The name of the Visualizer to use (either 'vedo' or 'open3d').
        :param database: Database to connect to.
        :param database_dir: Directory which contains the Database file (used if 'database' is not defined).
        :param database_name: Name of the Database (used if 'database' is not defined).
        :param remove_existing: If True, overwrite a Database with the same path.
        :param offscreen: If True, visual data will be saved but not rendered.
        :param fps: Max frame rate.
        """

        _Visualizer.__init__(self,
                             backend=backend,
                             database=database,
                             database_dir=database_dir,
                             database_name=database_name,
                             remove_existing=remove_existing,
                             offscreen=offscreen,
                             fps=fps,
                             nb_clients=nb_clients)
