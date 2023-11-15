# KCL_AI/scripts

https://zenn.dev/microsoft/articles/ad14d45121abe7#2.2.-%E6%97%A5%E6%9C%AC%E8%AA%9E

https://qiita.com/tmiyata25/items/e8866dfed6dd4b9a02ad

1. make .env
   ```
    AOAIDeploymentId=
    AOAIEndpoint=
    AOAIKey=
    SearchEndpoint=
    SearchIndex=
    SearchKey=
   ```
2. run `export $(cat .env| grep -v "#" | xargs)` in shell
3. run `export` and check env
    ```
    ...
    AOAIDeploymentId=xxx
    AOAIEndpoint=xxx
    AOAIKey=xxx
    ...
    SearchEndpoint=xxx
    SearchIndex=xxx
    SearchKey=xxx
    ...
    ```
4. run `python source.py`
