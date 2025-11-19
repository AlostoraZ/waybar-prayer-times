# Waybar prayer times module
This script fetches Islamic prayer times from the AlAdhan API and displays the next upcoming prayer inside Waybar.

## Screenshot
![Prayer Times Module Screenshot](assets/screenshot.png)

## Requirements
- Python 3
- requests library
- datetime library
install libraries if needed:
```zsh
pip install requests
pip install datetime
```
or you can install with yay:
```zsh
yay -S python-requests python-datetime

```

## Installation
1. Download and copy prayerTimes.py into ~/.config/waybar/scripts/
2. Make the script executeable:
```zsh
chmod +x ~/.config/waybar/scripts/prayerTimes.py
```

## Configuration
Open the script and edit:

```python
address = "Dubai,UAE" # Add your location in the following format "City,Country"
method = "3"          # Choode your calculation method based on your location
```
You can find all available methods here:\
[text](https://api.aladhan.com/v1/methods)

Add this module to config.jsonc
```jsonc
"custom/prayerTime": {
    "format": "{}",
    "exec": "~/.config/waybar/scripts/prayerTimes.py",
    "interval": 60,
    "escape": true
  },
```

Add this to style.css
```css
#custom-prayerTime {
    /* Add your styling here */
}
```

## References
AlAdhan API: [AlAdhan API](https://aladhan.com/prayer-times-api)  
Calculation Methods: [AlAdhan API Calculation Methods](https://api.aladhan.com/v1/methods)
