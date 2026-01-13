"""
The Alien Theme & Cards integration for Home Assistant.

This integration provides:
- Weyland-Yutani themed UI (inspired by the Alien movie franchise)
- Eleven custom Lovelace cards with retro terminal styling
- Authentic Alien/Thedus font integration
- Automatic installation of all dependencies
- Automatic Lovelace resource registration

For more details about this integration, please refer to the documentation at
https://github.com/loryanstrant/ha-alien-theme-cards
"""
from __future__ import annotations

import logging
from pathlib import Path
import shutil

from homeassistant.core import HomeAssistant
from homeassistant.config_entries import ConfigEntry
from homeassistant.helpers.typing import ConfigType
from homeassistant.components import frontend
import homeassistant.helpers.config_validation as cv

_LOGGER = logging.getLogger(__name__)

DOMAIN = "alien_theme_cards"

__version__ = "1.0.0"

CARDS_URL = "/local/weylandyutani/mu-th-ur-6000-cards.js"

# Define CONFIG_SCHEMA - this integration requires no configuration
CONFIG_SCHEMA = cv.empty_config_schema(DOMAIN)


async def async_setup(hass: HomeAssistant, config: ConfigType) -> bool:
    """Set up the Alien Theme & Cards integration."""
    _LOGGER.info("Setting up Alien Theme & Cards integration")
    
    # Get the integration directory
    integration_dir = Path(__file__).parent
    
    # Set up paths
    config_dir = Path(hass.config.path())
    themes_dir = config_dir / "themes"
    www_dir = config_dir / "www"
    www_weylandyutani_dir = www_dir / "weylandyutani"
    
    # Run file operations in executor to avoid blocking
    def install_files():
        """Install theme and www files."""
        try:
            # Ensure directories exist
            themes_dir.mkdir(exist_ok=True)
            www_weylandyutani_dir.mkdir(parents=True, exist_ok=True)
            
            # Copy theme files
            source_themes_dir = integration_dir / "themes"
            if source_themes_dir.exists():
                for theme_file in source_themes_dir.glob("*.yaml"):
                    dest_file = themes_dir / theme_file.name
                    _LOGGER.info(f"Installing theme file: {theme_file.name}")
                    shutil.copy2(theme_file, dest_file)
            
            # Copy www files (fonts and cards)
            source_www_dir = integration_dir / "www"
            if source_www_dir.exists():
                # Copy all files from www/weylandyutani to config/www/weylandyutani
                # Note: This replaces the entire directory to ensure clean installation
                # If you have custom files, store them elsewhere
                source_weylandyutani = source_www_dir / "weylandyutani"
                if source_weylandyutani.exists():
                    _LOGGER.info("Installing fonts and cards to www/weylandyutani")
                    if www_weylandyutani_dir.exists():
                        _LOGGER.debug("Removing existing www/weylandyutani directory")
                        shutil.rmtree(www_weylandyutani_dir)
                    shutil.copytree(source_weylandyutani, www_weylandyutani_dir)
        except PermissionError as err:
            _LOGGER.error(
                "Permission denied while installing files. Please check directory permissions: %s",
                err
            )
            return False
        except OSError as err:
            _LOGGER.error(
                "Failed to install files. Check disk space and permissions: %s",
                err
            )
            return False
        except Exception as err:
            _LOGGER.error(
                "Unexpected error during file installation: %s",
                err
            )
            return False
        
        return True
    
    # Run in executor to avoid blocking
    result = await hass.async_add_executor_job(install_files)
    
    if not result:
        _LOGGER.error("Alien Theme & Cards integration setup failed")
        return False
    
    _LOGGER.info("Alien Theme & Cards integration setup complete")
    _LOGGER.info("Themes installed to: %s", themes_dir)
    _LOGGER.info("Cards and fonts installed to: %s", www_weylandyutani_dir)
    
    # Register the Lovelace resource
    _LOGGER.info("Registering Lovelace resource: %s", CARDS_URL)
    
    # Note: Files in config/www/ are automatically served via /local/ by Home Assistant
    # The cards JavaScript file will self-register via window.customCards
    
    # Register the resource with the frontend so it loads automatically
    try:
        frontend.add_extra_js_url(hass, CARDS_URL)
        _LOGGER.info("Lovelace resource registered successfully")
        _LOGGER.info("Alien MU/TH/UR 6000 cards are now automatically available in Lovelace")
    except Exception as err:
        _LOGGER.warning(
            "Could not automatically register Lovelace resource: %s. "
            "The cards JavaScript file is available at %s. "
            "You may need to add it manually via Settings > Dashboards > Resources",
            err,
            CARDS_URL
        )
    
    return True


async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Set up from a config entry."""
    return True


async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Unload a config entry."""
    return True
