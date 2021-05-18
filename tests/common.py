from pathlib import Path
from typing import Any, Dict

from manifestoo.addon import Addon, Manifest
from manifestoo.addons_selection import AddonsSelection
from manifestoo.addons_set import AddonsSet


def populate_addons_dir(addons_dir: Path, addons: Dict[str, Dict[str, Any]]):
    if not addons_dir.is_dir():
        addons_dir.mkdir()
    for addon_name, manifest in addons.items():
        addon_path = addons_dir / addon_name
        addon_path.mkdir()
        manifest_path = addon_path / "__manifest__.py"
        manifest_path.write_text(repr(manifest))


def mock_addons_set(addons: Dict[str, Manifest]) -> AddonsSet:
    addons_set = AddonsSet()
    for addon_name, manifest in addons.items():
        addons_set[addon_name] = Addon(
            manifest, Path("/tmp/fake-addons-dir") / addon_name / "__manifest__.py"
        )
    return addons_set


def mock_addons_selection(addon_names: str) -> AddonsSelection:
    addons_selection = AddonsSelection()
    addons_selection.add_addon_names(addon_names)
    return addons_selection