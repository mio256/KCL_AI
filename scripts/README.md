# KCL_AI/scripts

## setup

```sh
cp .envrc_base .envrc
# .envrcにAPI_KEYを入力する
direnv
python3 -m venv venv
. ./venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
```
