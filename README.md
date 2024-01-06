# Subway Surfers Data Collection

## Setup

-   **Requirements**: Python 3, Selenium, ChromeDriver, pynput, Pillow
-   **Installation**: `pip install -r requirements.txt`
-   **ChromeDriver**: Download from [ChromeDriver](https://sites.google.com/chromium.org/driver/)

## Running the Script

-   Run `python data_extraction.py` from the script directory.

## Collecting Data

-   Play Subway Surfers in the opened browser window.
-   The script captures screenshots on arrow key actions and after 1 second of inactivity.
-   Press **Spacebar** to start a new data collection round.
-   Press **Escape** to stop the script.
