import openai
from app.vectorstore import search_relevant_content
from app.utils import extract_text_from_image

openai.api_key = "your-openai-key"

def generate_answer(question, image_b64):
    if image_b64:
        question += "\n" + extract_text_from_image(image_b64)

    context = search_relevant_content(question)

    messages = [
        {"role": "system", "content": "You are a helpful TA for the IITM TDS course."},
        {"role": "user", "content": f"Context:\n{context}\n\nQuestion:\n{question}"}
    ]

    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo-0125",
        messages=messages
    )

    answer = completion["choices"][0]["message"]["content"]
    links = extract_links(context)

    return answer, links

def extract_links(context):
    import re
    matches = re.findall(r"(https?://[^\s]+)", context)
    return [{"url": link, "text": "Reference"} for link in matches]
