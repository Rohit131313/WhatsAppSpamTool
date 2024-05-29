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

3. Download ChromeDriver and place it in a directory of your choice. Update the path in `fun1.py` and `fun2.py`.

## Usage

1. Run the `main.py` file:
    ```sh
    python main.py
    ```

2. Follow the prompts:
    - Enter `1` for message spam or `2` for sticker spam.
    - For message spam, enter the recipient's mobile number, the number of messages, and the message text.
    - For sticker spam, enter the recipient's mobile number, the folder path where the stickers are located, and the number of stickers to send.

    **Note:** In the sticker spam section, ensure that the folder path you enter contains the stickers you want to use for sticker spam.

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License
[MIT](LICENSE)
