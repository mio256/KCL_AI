import os
import openai
openai.api_type = "azure"
openai.api_key = os.getenv('OPENAI_API_KEY')
openai.api_base = "https://oai1-0.openai.azure.com/"
openai.api_version = "2023-05-15"
deployment_id = "deploy0123"

response = openai.ChatCompletion.create(
    engine=deployment_id,
    temperature=0.5,
    top_p=0.95,
    max_tokens=800,
    messages=[
        {"role": "system", "content": "あなたは九州工業大学のホームページに埋め込まれたチャットボットです。ユーザーからの問い合わせに対して日本語で応答してください。"},
        {"role": "user", "content": "三谷康範について教えてください。"}
    ]
)

print(response)
print(response['choices'][0]['message']['content'])
