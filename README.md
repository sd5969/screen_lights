# screen_lights

This project attempts to create a tool that screenshots the active desktop
and then outputs (perhaps via web?) a set of color values usable by HomeAssistant.

## Installation

Add something similar to the following to your HomeAssistant `configuration.yaml`:

```
sensor:
- platform: scrape
  resource: http://10.0.0.91:1111/image_url.html
  select: "span"
  name: "Game Screenshot URL"


template:
- binary_sensor:
    name: "Game Color Sync Active"
    state: "{{ states('input_boolean.sync_game_to_lights') }}"
    attributes:
      entity_picture: >
        {% if states('input_boolean.sync_game_to_lights') == 'on' %}
        {{ states('sensor.game_screenshot_url') }}
        {% else %}

        {% endif %}
```

Install required packages:

```
pip3 install -r requirements.txt
```

Update your AppDaemon configuration of [this script](https://github.com/sdlynx/appdaemon_config/blob/master/apps/music_lights.py)
to include `binary_sensor.game_color_sync_active` in `apps.yaml`:

```
music_lights:
  media_players:
    - "binary_sensor.game_color_sync_active"
```

## Usage

Run the python script from this directory with `python main.py` (Python 3).
This loops forever so end with Ctrl + C when needed.

Open up an http server to serve the results. You can run the `run_http_server.ps1` PowerShell script.
