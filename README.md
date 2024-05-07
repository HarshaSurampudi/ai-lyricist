# AI Lyricist (Telugu)

This project is an AI-based lyricist capable of generating Telugu lyrics in the style of the renowned lyricist Sirivennela Seetharama Sastry. The AI model is powered by Anthropic's Claude-3 language model and utilizes Qdrant, a vector database, to retrieve relevant examples based on the given instructions. It uses ollama to generate vector embeddings.

## Features

- Generates Telugu lyrics based on user-provided instructions
- Mimics the style of Sirivennela Seetharama Sastry
- Uses vector similarity search to retrieve relevant examples for guidance (Retrieval augmented generation)
- Provides a Gradio interface for easy interaction

## Samples

The full songs are not up to the mark. But some lines are good. Here are some good examples:

- A wife is questioning her husband if her happiness should only come from her motherhood. - `బిడ్డలున్నారనే  తల్లితనంతోనే  ఆనందంగా  
ఉండాలంటే  అది  తప్పేమో  తలపోసినావా`

- Motivating a person who just failed in exams - `పడినా లేచి నిలబడాలి. పరీక్షలో అయినా పాఠం నేర్చుకోవాలి`

So, I think it is useful for brainstorming and getting some ideas.

## Requirements

- Python 3.7 or higher
- Anthropic API key
- Qdrant server running locally
- Ollama server running locally

## Installation

1. Clone the repository:

```
git clone https://github.com/yourusername/ai-lyricist-telugu.git
cd ai-lyricist-telugu
```

2. Install the required dependencies:

```
pip install -r requirements.txt
```

3. Set up the Anthropic API key:

Replace `<api_key>` in the code with your actual Anthropic API key.

4. Set up the Qdrant server:

Make sure you have a Qdrant server running locally. Follow the Qdrant documentation for installation and configuration instructions.

5. Set up the Ollama server:

Make sure you have the ollama server running locally. Follow the Ollama documentation for installation and pulling the model. I used the [`nomic-embed-text`](https://ollama.com/library/nomic-embed-text) model for embeddings

## Data Preparation

1. Scrape the lyrics:

```
python scrape.py
```

This script will scrape the lyrics of Sirivennela Seetharama Sastry from the lyricstape.com website and save them in a CSV file named `sirivennela_lyrics.csv`.

2. Index the lyrics:

```
python index.py
```

This script will read the `sirivennela_lyrics.csv` file and index the lyrics using Qdrant. It will create a collection named "instructions" in Qdrant to store the indexed lyrics.

## Usage

1. Run the Gradio interface:

```
python app.py
```

2. Open the provided URL in your web browser.

3. Enter the desired instructions for generating the lyrics in the input field.

4. Click the "Submit" button to generate the lyrics.

5. The generated lyrics will be displayed in the output field.

## How it Works

1. The user provides instructions for generating the lyrics through the Gradio interface.

2. The `query_instructions` function retrieves relevant examples from the Qdrant database based on the provided instructions using vector similarity search.

3. The retrieved examples and user instructions are formatted into a prompt for the AI model.

4. The `generate_text` function sends the prompt to the Claude-3 language model via the Anthropic API to generate the lyrics.

5. The generated lyrics are returned and displayed in the Gradio interface.

## Future Scope

The current iteration of this project uses RAG with Claude-3. I want to fine-tune an OpenSource LLM such as LLAMA-3 or Gemma and see how well they perform.

## License

This project is licensed under the [MIT License](LICENSE).

## Acknowledgments

- [Anthropic](https://www.anthropic.com/) for the Claude-3 language model
- [Qdrant](https://qdrant.tech/) for the vector db
- [Gradio](https://gradio.app/) for the user interface
- [Ollama](https://ollama.com/) for the serving the embedding model.
- [Lyricstape](https://lyricstape.com/) for the lyrics data

**Note: This project is developed with the utmost respect for the late lyricist Sirivennela Seetharama Sastry and his incredible contributions to Telugu literature. The intention is to celebrate and learn from his unique style and not to disrespect or replace his exceptional talent. The lyrics are obtained from public sources and are used for educational and research purposes only. If you have any concerns or objections regarding the data used in this project, please create an issue, and I will address it promptly.**
