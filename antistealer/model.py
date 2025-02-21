import openai

from credentials import api_key
from config import system_prompt
from config import model_name


openai.api_key = api_key


def model_request(images: list[bytes]) -> str:
    user_content = [{"type": "image", "image": current} for current in images]
    response = openai.ChatCompletion.create(
        model=model_name,
        messages=[
            {"role": "system", "text": system_prompt},
            {"role": "user", "content": user_content}
        ]
    )
    return response["choices"][0]["message"]["content"]
