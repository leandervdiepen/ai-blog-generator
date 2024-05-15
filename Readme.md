# Blog Post Generator with GPT-4o and DALL-E 3

This project utilizes OpenAI's GPT-4o model to generate and audit blog posts and DALL-E 3 to generate images for the blog posts. The program automates the creation of SEO-optimized content and relevant images, ensuring high-quality, engaging blog posts.

## Features

- **Blog Post Generation:** Creates detailed blog posts optimized for SEO.
- **Content Auditing:** Optimizes the generated content for readability and simplicity.
- **Image Generation:** Produces relevant images to accompany each blog post.
- **File System Storage:** Saves the original and optimized blog posts, image descriptions, and image URLs to the file system.

## Prerequisites

- Python 3.6+
- OpenAI API key

## Installation

### Clone the Repository

```
git clone https://github.com/yourusername/blog-post-generator.git
cd blog-post-generator
```

## Updating the Keywords List

To generate blog posts, the `keywords.py` file must be populated with topics and their associated keywords. This list is crucial as it directs the content generation process for each blog post.

### Structure of `KEYWORDS_LIST`
The `KEYWORDS_LIST` is an array of dictionaries, where each dictionary represents a blog topic and its related keywords. Here's the structure:

```
KEYWORDS_LIST = [
{"topic": "Topic Name", "keywords": ["keyword1", "keyword2", "keyword3"]},
]
```

To add a new blog post topic along with its keywords, append a new dictionary to the `KEYWORDS_LIST` with the topic and an array of keywords.

Note that with every program run all blogs in the keywords list will be generated so remove the ones you do not want to generate.


### Guidelines for Keywords
- **Relevance:** Ensure that the keywords are highly relevant to the topic to maintain the focus and quality of the generated content.
- **Variety:** Use a mix of broad and specific keywords to cover the topic comprehensively.
- **Limitation:** While it's important to include multiple keywords, avoid overstuffing to keep the content natural and engaging.

By carefully selecting topics and corresponding keywords, you can tailor the content generation to meet specific themes and focus areas, enhancing the relevance and quality of your blog posts.


### Install Required Libraries

```
pip install openai requests
```

### Set Up Your OpenAI API Key
Replace 'your-openai-api-key' in the `config.py` file with your actual OpenAI API key.

### Run the Main Script
Navigate to your project directory in the terminal and execute:
```
python main.py
```

This will generate blog posts, audit them, create image descriptions, generate images, and save all these contents into their respective directories on the file system.


## Cost Estimation
- **DALL-E 3:** Approximately $0.08 per image.
- **GPT-4o:** Approximately $0.01 per blog post.
