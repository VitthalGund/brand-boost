from typing import List
from llama_cpp import Llama
import argparse
import re
from ..constants.index import keyWordsPrompt, brandingPrompt
from ..constants.index import MAX_INPUT_LENGTH
from ..utils.input import validate_input_length


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", "-i", type=str, required=True)
    args = parser.parse_args()
    user_input = args.input

    print(f"User input: {user_input}")
    if validate_input_length(user_input):
        generate_branding_snippet(user_input)
        generate_keywords(user_input)
    else:
        raise ValueError(
            f"Input length is too long. Must be under {MAX_INPUT_LENGTH}. Submitted input is {user_input}"
        )


def generate_keywords(prompt: str) -> List[str]:
    enriched_prompt = f"Generate related branding keywords for {prompt}: "
    print(enriched_prompt)

    response = Llama(
        model_path="path/to/llama-2/llama-model.gguf", chat_format="llama-2"
    )
    response = response.create_chat_completion(
        messages=[
            {"role": "system", "content": keyWordsPrompt},
            {"role": "user", "content": enriched_prompt},
        ],
        response_format={
            "type": "json_object",
        },
    )

    # Extract output text.
    keywords_text: str = response["choices"][0]["text"]

    # Strip whitespace.
    keywords_text = keywords_text.strip()
    keywords_array = re.split(",|\n|;|-", keywords_text)
    keywords_array = [k.lower().strip() for k in keywords_array]
    keywords_array = [k for k in keywords_array if len(k) > 0]

    print(f"Keywords: {keywords_array}")
    return keywords_array


def generate_branding_snippet(prompt: str) -> str:
    # Load your API key from an environment variable or secret management service
    enriched_prompt = (
        brandingPrompt + f"Generate upbeat branding snippet for {prompt}: "
    )

    response = response.create_chat_completion(
        messages=[
            {"role": "system", "content": brandingPrompt},
            {"role": "user", "content": enriched_prompt},
        ],
        response_format={
            "type": "json_object",
        },
    )

    # Extract output text.
    branding_text: str = response["choices"][0]["text"]

    # Strip whitespace.
    branding_text = branding_text.strip()

    # Add ... to truncated statements.
    last_char = branding_text[-1]
    if last_char not in {".", "!", "?"}:
        branding_text += "..."

    print(f"Snippet: {branding_text}")
    return branding_text


if __name__ == "__main__":
    main()
