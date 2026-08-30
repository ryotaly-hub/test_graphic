import os, sys, base64
from google import genai
from google.genai.types import GenerateContentConfig, Modality

def generate_image(prompt: str, out_path: str):
    client = genai.Client(api_key=os.environ["GEMINI_API_KEY"])
    response = client.models.generate_content(
        model="gemini-3.1-flash-image",  # 通称 Nano Banana 2
        contents=prompt,
        config=GenerateContentConfig(response_modalities=[Modality.TEXT, Modality.IMAGE]),
    )
    for part in response.candidates[0].content.parts:
        if part.inline_data:
            with open(out_path, "wb") as f:
                f.write(part.inline_data.data)
            print(f"saved: {out_path}")
            return
    raise RuntimeError("画像が生成されませんでした")

if __name__ == "__main__":
    generate_image(sys.argv[1], sys.argv[2])