import os
import pkgutil
import importlib

_registry = {}


def register(
    name,
    controls="Arrows/WASD",
    description="Arcade Game"
):

    def decorator(func):

        _registry[name] = {
            "entry": func,
            "controls": controls,
            "description": description
        }

        return func

    return decorator


def discover_games():

    games_dir = "games"

    if not os.path.isdir(games_dir):
        return

    for _, modname, _ in pkgutil.iter_modules(
        [games_dir]
    ):

        if modname.startswith("_"):
            continue

        try:

            importlib.import_module(
                f"games.{modname}"
            )

        except Exception as e:

            print(
                f"⚠️ Failed to load {modname}: {e}"
            )


def get_games():

    return [
        {
            "name": name,
            **data
        }
        for name, data in _registry.items()
    ]


def run_game(
    name,
    screen,
    clock
):

    if name not in _registry:

        raise ValueError(
            f"Game '{name}' not found"
        )

    return _registry[name]["entry"](
        screen,
        clock
    )
