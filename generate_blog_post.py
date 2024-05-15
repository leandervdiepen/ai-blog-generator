# generate_blog_post.py
from config import OPENAI_API_KEY
from prompts import get_random_seo_blog_post_prompt
from keywords import KEYWORDS_LIST
from openai import OpenAI
client = OpenAI(api_key=OPENAI_API_KEY)

def generate_blog_post(topic, keywords):
    prompt_template = get_random_seo_blog_post_prompt()
    prompt = prompt_template.format(topic=topic, keywords=", ".join(keywords))
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[{"role": "system", "content": "You are a professional blog writer."},
                  {"role": "user", "content": prompt}],
        max_tokens=4096
    )
    print(response)
    return response.choices[0].message.content

if __name__ == "__main__":
    for item in KEYWORDS_LIST:
        topic = item['topic']
        keywords = item['keywords']
        blog_post = generate_blog_post(topic, keywords)
        print(f"Generated Blog Post for '{topic}':")
        print(blog_post)
        print("\n" + "="*50 + "\n")
