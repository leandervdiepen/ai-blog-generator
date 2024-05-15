import os
from generate_blog_post import generate_blog_post
from audit_blog_post import audit_blog_post
from generate_image import generate_image_description, generate_image
from keywords import KEYWORDS_LIST
import uuid


def save_to_file(directory, filename, content):
    with open(os.path.join(directory, filename), 'w', encoding='utf-8') as file:
        file.write(content)


def main():
    base_directory = "blog_posts"

    if not os.path.exists(base_directory):
        os.makedirs(base_directory)

    for item in KEYWORDS_LIST:
        topic = item['topic']
        keywords = item['keywords']

        # Create directory for the topic 
        random_hash = uuid.uuid4().hex[:8]
        topic_directory = os.path.join(
            base_directory, f"{topic.replace(' ', '_')}_{random_hash}")
        if not os.path.exists(topic_directory):
            os.makedirs(topic_directory)

        # Generate blog post
        blog_post = generate_blog_post(topic, keywords)
        save_to_file(topic_directory, "original_post.txt", blog_post)
        print(f"Generated Blog Post for '{topic}':")
        print(blog_post)

        # Audit and optimize blog post
        optimized_post = audit_blog_post(blog_post)
        save_to_file(topic_directory, "optimized_post.txt", optimized_post)
        print(f"\nOptimized Blog Post for '{topic}':")
        print(optimized_post)

        # Generate image description
        image_description = generate_image_description(topic)
        save_to_file(topic_directory, "image_description.txt",
                     image_description)
        print(f"\nImage Description for '{topic}':")
        print(image_description)

        # Generate image
        image_url = generate_image(image_description)
        save_to_file(topic_directory, "image_url.txt", image_url)
        print(f"Generated Image URL for '{topic}':")
        print(image_url)
        print("\n" + "="*50 + "\n")


if __name__ == "__main__":
    main()
