# Alien Theme & Cards for Home Assistant

A comprehensive Home Assistant integration that brings the iconic Weyland-Yutani Corporation aesthetic and MU/TH/UR 6000 terminal interface from the Alien movie franchise to your smart home.

[![hacs_badge](https://img.shields.io/badge/HACS-Custom-orange.svg)](https://github.com/custom-components/hacs)
[![GitHub release](https://img.shields.io/github/release/loryanstrant/ha-alien-theme-cards.svg)](https://github.com/loryanstrant/ha-alien-theme-cards/releases)

## Features

### 🎨 Weyland-Yutani Theme
- Authentic Alien movie-inspired dark theme
- Custom Thedus font family (from the actual Alien films)
- Retro-futuristic terminal aesthetics
- Green phosphor CRT-inspired color scheme

### 🖥️ MU/TH/UR 6000 Terminal Cards
Eleven custom Lovelace cards with classic terminal styling:

- **Status Card** - Display system status in terminal format
- **Sensor Card** - Show sensor data with CRT aesthetics  
- **Button Card** - Control entities with terminal-style buttons
- **Text Card** - Display text messages in authentic terminal format
- **Gauge Card** - Visualize numeric sensors with terminal gauges
- **Clock Card** - Show current time in MU/TH/UR style
- **Glance Card** - Compact multi-entity overview
- **Light Card** - Control lights with terminal interface
- **Picture Card** - Display images with terminal framing
- **Weather Card** - Weather information in terminal format
- **Alarm Card** - Control alarm systems with terminal keypad

## Installation

### HACS (Recommended)

1. Add this repository as a custom repository in HACS:
   - Open HACS in Home Assistant
   - Click the three dots in the top right
   - Select "Custom repositories"
   - Add `https://github.com/loryanstrant/ha-alien-theme-cards`
   - Select category: "Integration"

2. Install the integration through HACS

3. Add to your `configuration.yaml`:
   ```yaml
   alien_theme_cards:
   ```

4. Restart Home Assistant

5. Refresh your browser (hard refresh: Ctrl+Shift+R or Cmd+Shift+R)

6. Select the Weyland-Yutani theme in your profile settings

### Manual Installation

1. Download the latest release from GitHub

2. Copy the `custom_components/alien_theme_cards` directory to your Home Assistant `config/custom_components/` directory

3. Add to your `configuration.yaml`:
   ```yaml
   alien_theme_cards:
   ```

4. Restart Home Assistant

5. Refresh your browser (hard refresh: Ctrl+Shift+R or Cmd+Shift+R)

## Usage

### Applying the Theme

1. Go to your profile (click your username in the bottom left)
2. Under "Theme", select "Weyland-Yutani"
3. The theme will be applied immediately

### Using the Cards

The MU/TH/UR 6000 cards will automatically appear in the card picker when adding cards to your dashboard:

1. Edit your dashboard
2. Click "Add Card"
3. Search for "MU/TH/UR" or "Alien"
4. Select any of the eleven available cards
5. Configure as needed

All cards support real-time previews and come with sensible defaults.

## Typography

This integration uses the authentic **Thedus** font family from the Alien films, as documented in the excellent [Typeset in the Future: Alien](https://typesetinthefuture.com/2014/12/01/alien/) article. The fonts are properly licensed for use in this project.

### Font Variants

- **Thedus Wide** - Primary display font
- **Thedus Condensed** - Body text and compact displays
- **Thedus Stencil** - Special emphasis and headers
- Fallbacks: Orbitron, Courier New, monospace

## Credits

### Original Components

This integration combines:
- **MU/TH/UR 6000 Cards** by [@loryanstrant](https://github.com/loryanstrant/ha-MU-TH-UR-6000-cards)
- **Weyland-Yutani Theme** by [@loryanstrant](https://github.com/loryanstrant/ha-weylandyutani)

### Inspiration

- The Alien film franchise by 20th Century Studios
- [Typeset in the Future: Alien](https://typesetinthefuture.com/2014/12/01/alien/) by Dave Addey
- Thedus font by Dharma Type

## License

MIT License - see [LICENSE](LICENSE) file for details.

**Note**: The Thedus fonts are licensed separately and included with permission. Alien franchise trademarks are property of 20th Century Studios.

## Support

For issues, questions, or suggestions:
- [GitHub Issues](https://github.com/loryanstrant/ha-alien-theme-cards/issues)
- [Home Assistant Community](https://community.home-assistant.io/)

---

**"Building Better Worlds"** - Weyland-Yutani Corporation
