# WhatsAppSpamBot

## Description
WhatsAppSpamBot is a Python tool for automating the process of sending spam messages and stickers on WhatsApp Web. This tool can be used for testing or fun purposes.

## Features
- Send a specified number of spam messages to a given WhatsApp contact.
- Send a specified number of stickers to a given WhatsApp contact.
- Utilizes Selenium for web automation.

## Requirements
- Python 3.x
- Selenium
- Google Chrome
- ChromeDriver

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/WhatsAppSpamBot.git
    cd WhatsAppSpamBot
    ```

2. Install the required Python packages:
    ```sh
    pip install selenium
    ```

3. Download ChromeDriver:
    - Go to the [ChromeDriver download page](https://developer.chrome.com/docs/chromedriver/downloads) for general versions.
    - If you are using Chrome version 115 or above, download ChromeDriver from [here](https://googlechromelabs.github.io/chrome-for-testing/).
    - Download the version that matches your installed version of Google Chrome.
    - Extract the downloaded file and place `chromedriver.exe` in a directory of your choice.
    - Update the path to `chromedriver.exe` in `fun1.py` and `fun2.py` as needed.

4. Update Chrome profile settings:
    - Change the name of the Chrome profile and the directory of Chrome according to your need in `fun1.py` and `fun2.py`.
    - You can see the Chrome profile details by navigating to `chrome://version` in your Chrome browser.

## Usage

1. **Important Notes:**
    - Make sure you are already logged in to your WhatsApp Web before you start running the Python file.
    - Ensure you are logged in to the Chrome profile mentioned in the code.

2. Run the `main.py` file:
    ```sh
    python main.py
    ```

3. Follow the prompts:
    - Enter `1` for message spam or `2` for sticker spam.
    - For message spam, enter the recipient's mobile number, the number of messages, and the message text.
    - For sticker spam, enter the recipient's mobile number, the folder path where the stickers are located, and the number of stickers to send.

    **Note:** In the sticker spam section, ensure that the folder path you enter contains the stickers you want to use for sticker spam.

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License
[MIT](LICENSE)
