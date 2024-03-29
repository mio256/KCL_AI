import os
import requests
import pprint

# APIの設定
api_base = "https://oai1-0.openai.azure.com/"
api_key = os.environ["OPENAI_API_KEY"]
deployment_id = "deploy0123"
search_endpoint = "https://search0123.search.windows.net"
search_key = os.environ["SEARCH_KEY"]
search_index = "index0206-mitani-tel"

# ヘッダー
headers = {
    "Content-Type": "application/json",
    "api-key": api_key
}

user_request = {
    "role": "user",
    "content": "KCLってなんですか"
}

# リクエストデータ
data = {
    "dataSources": [
        {
            "type": "AzureCognitiveSearch",
            "parameters": {
                "endpoint": search_endpoint,
                "indexName": search_index,
                "semanticConfiguration": None,
                "queryType": "simple",
                "fieldsMapping": {
                    "contentFieldsSeparator": "\n",
                    "contentFields": ["content"],
                    "filepathField": "metadata_storage_name",
                    "titleField": None,
                    "urlField": "metadata_storage_path",
                    "vectorFields": []
                },
                "inScope": True,
                "roleInformation": "",
                "filter": None,
                "strictness": 3,
                "topNDocuments": 5,
                "key": search_key
            }
        }
    ],
    "messages": [
        {
            "role": "system",
            "content": "あなたは九州工業大学のホームページに埋め込まれたチャットボットです。データソースに基づき、ユーザーからの問い合わせに対して日本語で応答してください。"
        },
        user_request,
        user_request,
        user_request,
    ],
    "deployment": deployment_id,
    "temperature": 0.5,
    "top_p": 0.95,
    "max_tokens": 800,
    "stop": None,
    "stream": False
}

pprint.pprint(data)

# POSTリクエストの実行
response = requests.post(f"{api_base}/openai/deployments/{deployment_id}/extensions/chat/completions?api-version=2023-12-01-preview", json=data, headers=headers)

# 応答の表示
pprint.pprint(response.json())
print(response.json()['choices'][0]['message']['content'])
