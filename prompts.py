# prompts.py

import random

# Different templates for generating an SEO-optimized blog post
SEO_BLOG_POST_PROMPTS = [
    """
    Write a comprehensive blog post on the topic "{topic}" optimized for SEO. The post should include the following keywords: {keywords}. 
    Start with an engaging introduction that highlights the importance of the topic. 
    Follow with detailed sections including:

    1. Background and Context
    2. Key Benefits and Features
    3. Practical Tips and Strategies
    4. Case Studies or Examples
    5. Conclusion with a call to action.

    Make sure to structure the content with headings, subheadings, and bullet points where appropriate.
    """,
    """
    Create an in-depth blog post about "{topic}" focusing on SEO optimization. Include relevant keywords such as {keywords}. 
    Organize the content with the following sections:

    1. Introduction: Provide an overview of the topic and its significance.
    2. Detailed Analysis: Discuss the main points in detail with supporting data and research.
    3. Implementation Strategies: Offer actionable advice and best practices.
    4. Benefits and Challenges: Highlight the advantages and potential obstacles.
    5. Conclusion: Summarize the key takeaways and encourage reader engagement.

    Ensure clarity with headings, subheadings, and lists to enhance readability.
    """,
    """
    Generate a detailed and SEO-friendly blog post on the topic "{topic}". Use the keywords {keywords} strategically throughout the post. 
    Structure the post with the following outline:

    1. Introduction: Captivate the reader with the relevance of the topic.
    2. Main Content: 
        a. Historical Context or Background
        b. Current Trends and Developments
        c. Detailed Insights and Analysis
    3. Practical Applications: Provide real-world examples and case studies.
    4. Future Prospects: Discuss upcoming trends and predictions.
    5. Conclusion: Recap the main points and suggest next steps or actions.

    Improve clarity by using sections and bullet points where appropriate.
    """
]

# Template for auditing and optimizing a blog post for readability
AUDIT_BLOG_POST_PROMPT = """
Audit and optimize the following blog post for readability and simple language. Ensure the content is easy to understand for a general audience:

{blog_post}
---
only output the optimized blog post and nothing else
"""

# Template for generating image descriptions
IMAGE_PROMPT = """
Generate a detailed description for an image that should accompany the blog post on "{topic}". The image should be visually appealing and relevant to the content.
"""

def get_random_seo_blog_post_prompt():
    return random.choice(SEO_BLOG_POST_PROMPTS)
