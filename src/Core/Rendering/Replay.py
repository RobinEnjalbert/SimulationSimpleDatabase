from SSD.Core.Storage.Database import Database
from SSD.Core.Rendering.backend.BaseReplay import BaseReplay
from SSD.Core.Rendering.backend.Vedo.VedoReplay import VedoReplay
from SSD.Core.Rendering.backend.Open3d.Open3dReplay import Open3dReplay


class Replay:

    def __init__(self,
                 database_name: str,
                 database_dir: str = '',
                 backend: str = 'vedo',
                 fps: int = 20):
        """
        Replay a simulation from saved visual data.

        :param database_name: Name of the Database.
        :param database_dir: Directory of the Database.
        :param backend: The name of the Visualizer to use (either 'vedo' or 'open3d').
        :param fps: Max frame rate.
        """

        # Check backend
        if backend.lower() not in (available := {'vedo': VedoReplay, 'open3d': Open3dReplay}):
            raise ValueError(f"The backend '{backend}' is not available. Must be in {available}")

        # Load the Database
        database = Database(database_dir=database_dir, database_name=database_name).load()

        # Create the Visualizer
        self.__replay: BaseReplay = available[backend.lower()](database=database,
                                                               fps=fps)

    def launch(self):
        """
        Initialize the Visualizer: create all Actors and render them in a Plotter.
        """

        self.__replay.start_replay()
