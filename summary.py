import ollama

MODEL_NAME = "llama3"

def generate_prompt(text):
    prompt = f"""
You are a professional AI prompt engineer.

Read the input text carefully and convert it into a high-quality
cinematic image generation prompt with lighting, atmosphere,
visual details and artistic style. Keep under 80 words.

Input:
\"\"\"{text}\"\"\"

Return ONLY the final image prompt.
"""

    response = ollama.chat(
        model=MODEL_NAME,
        messages=[{"role": "user", "content": prompt}]
    )

    return response["message"]["content"].strip()