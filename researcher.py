# agents/researcher.py

import os
import requests
from sentence_transformers import SentenceTransformer, util
import numpy as np
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))
embedding_model = SentenceTransformer("all-MiniLM-L6-v2")


def search_semantic_scholar(query: str, limit=5):
    print("🔎 Searching papers for:", query)
    url = f"https://api.semanticscholar.org/graph/v1/paper/search?query={query}&limit={limit}&fields=title,abstract,url"
    response = requests.get(url)
    data = response.json()
    return data.get("data", [])


def embed_documents(docs: list[str]):
    return embedding_model.encode(docs, convert_to_tensor=True)


def call_groq(prompt: str):
    response = client.chat.completions.create(
        model="llama3-70b-8192",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7,
    )
    return response.choices[0].message.content.strip()


def summarize_relevant_papers(query: str, top_k=3):
    papers = search_semantic_scholar(query, limit=10)
    abstracts = [p["abstract"] for p in papers if p.get("abstract")]

    if not abstracts:
        return "❌ No abstracts found for this topic."

    embeddings = embed_documents(abstracts)
    query_embedding = embed_documents([query])[0]

    # Compute similarity
    cosine_scores = util.pytorch_cos_sim(query_embedding, embeddings)[0].cpu().numpy()
    top_indices = np.argsort(cosine_scores)[::-1][:top_k]

    context = "\n\n".join([f"Title: {papers[i]['title']}\nAbstract: {papers[i]['abstract']}" for i in top_indices])
    prompt = f"""
You are an AI research assistant. Based on the following paper abstracts, summarize the key methods used and how they relate to the research topic: "{query}"

{context}
"""

    return call_groq(prompt)
