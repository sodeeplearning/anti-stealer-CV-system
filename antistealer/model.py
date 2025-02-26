from openai import OpenAI

from .credentials import api_key
from .config import system_prompt
from .config import model_name


client = OpenAI(api_key=api_key)


def model_request(images: list[str]) -> str:
    """Make request to a ChatGPT model.

    :param images: String-bytes of images frames.
    :return: Model's response
    """
    user_content = [{"type": "image_url", "image_url": {"url": f"data:image/jpeg;base64,{current}"}} for current in images]
    response = client.chat.completions.create(
        model=model_name,
        messages=[
            {"role": "system", "text": system_prompt},
            {"role": "user", "content": user_content}
        ],

    )
    return response["choices"][0]["message"]["content"]
