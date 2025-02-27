# AutoBot

AutoBot is a Discord bot built using Python and the `discord.py` library. It offers various commands including ping, coin flip, joke, and AI chat functionalities using the TinyLlama model run locally using Ollama.

## Features

- **Ping**: Check the bot's latency.
- **Coin Flip**: Flip a coin to get heads or tails.
- **Joke**: Get a random joke.
- **AI Chat**: Ask the AI a question and get a response.
- **Custom Help Command**: Displays a list of available commands.

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/rshreeshabhat/AutoBot.git
    cd AutoBot
    ```

2. Install the required dependencies:
    ```sh
    pip install -r requirements.txt
    ```
    
    Run the following command to install Ollama:
    ```sh
    winget install Ollama.Ollama
    ```

    Verify the installation:
    ```sh
    ollama --version
    ```

    Pull the TinyLlama model using the following command:
    ```sh
    ollama pull tinyllama
    ```

    You can use any Ollama model, just make adjustments in the code to reflect the new model. Here I am using tinyllama as it is a very lightweight and CPU-friendly model.

    If you have a high performance PC with a good GPU you can also use Deepseek-R1:
    ```sh
    ollama pull deepseek-r1:8b
    ```



3. Create a `.env` file in the root directory and add your Discord bot token:
    ```env
    TOKEN=your_discord_bot_token
    ```
    You can create a bot token [here.](https://discord.com/developers/docs/quick-start/getting-started)
## Usage

Run the bot:
```sh
python main.py
```

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request.

## License

This project is licensed under the MIT License.

## Acknowledgements

- [discord.py](https://github.com/Rapptz/discord.py)
- [ollama](https://github.com/ollama/ollama)
- [pyjokes](https://github.com/pyjokes/pyjokes)
