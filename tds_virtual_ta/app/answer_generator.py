import openai
from app.vectorstore import search_relevant_content
from app.utils import extract_text_from_image

openai.api_key = "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"

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
