import os
from pathlib import Path
from google import genai

def main():
    api_key = os.getenv("GEMINI_API_KEY")

    if not api_key:
        raise RuntimeError("GEMINI_API_KEY is missing")

    client = genai.Client(api_key=api_key)

    topic = os.getenv(
        "VIDEO_TOPIC",
        "Forex Day Trading: Market Structure for Beginners"
    )

    prompt = f"""
Write an original educational YouTube video script.

Topic: {topic}
Language: Natural spoken Sinhala with English trading terms.
Audience: Beginner Forex day traders.
Duration: 5-8 minutes.

Include:
1. Interesting introduction
2. Detailed explanation
3. Practical Forex examples
4. Risk management
5. Summary
6. YouTube title and description

Rules:
- Use natural Sinhala.
- Do not invent live market prices or news.
- Do not promise profits.
- Do not give guaranteed trading signals.
- Keep the content educational.
"""

    response = client.models.generate_content(
        model="gemini-3.8-flash",
        contents=prompt
    )

    if not response.text:
        raise RuntimeError("Gemini returned an empty response")

    output = Path("output")
    output.mkdir(exist_ok=True)

    (output / "video_script.md").write_text(
        response.text,
        encoding="utf-8"
    )

    print("SUCCESS: Sinhala script generated!")

if __name__ == "__main__":
    main()
