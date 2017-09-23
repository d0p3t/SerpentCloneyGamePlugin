from serpent.game import Game

from .api.api import CloneyAPI

from serpent.utilities import Singleton


class SerpentCloneyGame(Game, metaclass=Singleton):

    def __init__(self, **kwargs):
        kwargs["platform"] = "steam"

        kwargs["window_name"] = "Cloney"

        kwargs["app_id"] = "400030"
        kwargs["app_args"] = None

        super().__init__(**kwargs)

        self.api_class = CloneyAPI
        self.api_instance = None

    @property
    def screen_regions(self):
        regions = {
            # "SCREEN_REGION": (y1, x1, y2, x2)
            "MAIN_MENU_PLAY": (413, 307, 490, 534),
            "GAME_OVER_PLAY": (421, 307, 498, 534),
            "GAME_PAUSE": (6, 943, 81, 1018)
        }

        return regions

    @property
    def ocr_presets(self):
        presets = {
            "SAMPLE_PRESET": {
                "extract": {
                    "gradient_size": 1,
                    "closing_size": 1
                },
                "perform": {
                    "scale": 10,
                    "order": 1,
                    "horizontal_closing": 1,
                    "vertical_closing": 1
                }
            }
        }

        return presets
