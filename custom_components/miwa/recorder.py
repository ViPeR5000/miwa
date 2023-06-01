"""Integration platform for recorder."""
from __future__ import annotations

from homeassistant.core import HomeAssistant, callback

from .const import ATTRS_TO_IGNORE_RECORDER


@callback
def exclude_attributes(hass: HomeAssistant) -> set[str]:
    """Exclude static attributes from being recorded in the database."""
    return ATTRS_TO_IGNORE_RECORDER
