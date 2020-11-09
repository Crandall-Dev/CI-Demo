##
#   Logic and calcuations for generating metrics of a board
#    - Determines both attackers and defender stats
#    - Normally is used with then weighting for AI decision making
#
#   @author Aaron S. Crandall <crandall@gonzaga.edu>
#   @copyright 2020
#

import logging
from Location import Location
# from BoardLocations import CORNERS, THRONE, KING_TILES, NORTH_EDGE
from BoardLocations import THRONE


# *************************************************************************** #
class BoardMetrics:
    def __init__(self):
        self._log = logging.getLogger(__class__.__name__)       # noqa: F821
        self._log.debug("Created board metrics class")

        # Metrics
        self.throne_occupied = True

        # Lookup values
        self._throne_loc = Location(3, 3)
        self._corners = [Location(0, 0), Location(6, 0),
                         Location(0, 6), Location(6, 6)]

    def update_metrics(self, pieces):
        self._log.debug("Updating board metrics")
        self._pieces = pieces

        self._calc_throne_occupied()

    def _calc_throne_occupied(self):
        self.throne_occupied = \
            (self._pieces.get_king().get_location() == THRONE)

    def __str__(self):
        ret = ""
        ret += "Throne Occupied: {0}".format(self._throne_occupied)
        return ret
