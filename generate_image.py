# generate_image.py
from config import OPENAI_API_KEY
from prompts import IMAGE_PROMPT
from openai import OpenAI

client = OpenAI(api_key=OPENAI_API_KEY)

def generate_image_description(topic):
    prompt = IMAGE_PROMPT.format(topic=topic)
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[{"role": "system", "content": "You are a professional image description writer."},
                  {"role": "user", "content": prompt}],
        max_tokens=300
    )
    return response.choices[0].message.content


def generate_image(image_description):
    response = client.images.generate(
        model="dall-e-3",
        prompt=image_description,
        n=1,
        size="1792x1024",
        quality="standard"
    )
    image_url = response.data[0].url
    return image_url


if __name__ == "__main__":
    topic = "The Benefits of a Plant-Based Diet"
    image_description = generate_image_description(topic)
    print(image_description)
