import anthropic
from qdrant_client import QdrantClient
from embedding import get_embedding
import gradio as gr

anthropic_client = anthropic.Anthropic(api_key="<api_key>")
qdrant_client = QdrantClient(url="http://localhost:6333")

def query_instructions(query, limit=10):
    search_result = qdrant_client.search(
        collection_name="instructions",
        query_vector=get_embedding(query),
        limit=limit
    )
    return [result.payload for result in search_result]

def generate_text(system_prompt, user_prompt):
    message = anthropic_client.messages.create(
        model="claude-3-opus-20240229",
        max_tokens=1024,
        system=system_prompt,
        messages=[{"role": "user", "content": user_prompt}]
    )
    return message.content[0].text

system_prompt = (
    "You are a Telugu lyricist AI, capable of generating lyrics in the style of "
    "Sirivennela Seetharama Sastry according to the given instructions. You must "
    "also make sure that the song rhymes well and is in the same style as the "
    "examples provided."
)

def generate_song(instructions):
    results = query_instructions(instructions)
    examples_prompt = "INSTRUCTIONS: {}\nLYRICS: {}\n"
    user_prompt = (
        "Consider the following examples:\n{}\n"
        "Generate a song with the following instructions.\n"
        "INSTRUCTIONS: {}\nLYRICS: "
    )
    user_prompt = user_prompt.format(
        "\n".join([examples_prompt.format(result['instructions'], result['lyrics']) for result in results]),
        instructions
    )
    return generate_text(system_prompt, user_prompt)

demo = gr.Interface(
    fn=generate_song,
    inputs=["text"],
    outputs=["text"],
    title="AI Lyricist (Telugu)",
    description="Generate Telugu lyrics in the style of Sirivennela Seetharama Sastry.",
)

demo.launch(share=True)