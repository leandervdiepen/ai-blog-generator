# audit_blog_post.py

from config import OPENAI_API_KEY
from prompts import AUDIT_BLOG_POST_PROMPT
from keywords import KEYWORDS_LIST
from generate_blog_post import generate_blog_post
from openai import OpenAI

client = OpenAI(api_key=OPENAI_API_KEY)


def audit_blog_post(blog_post):
    prompt = AUDIT_BLOG_POST_PROMPT.format(blog_post=blog_post)
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[{"role": "system", "content": "You are an expert editor."},
                  {"role": "user", "content": prompt}],
        max_tokens=4096
    )
    return response.choices[0].message.content


if __name__ == "__main__":
    for item in KEYWORDS_LIST:
        topic = item['topic']
        keywords = item['keywords']
        blog_post = generate_blog_post(topic, keywords)
        optimized_post = audit_blog_post(blog_post)
        print(f"Optimized Blog Post for '{topic}':")
        print(optimized_post)
        print("\n" + "="*50 + "\n")
