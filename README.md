# KCL_AI

## Mac
```
sh setup.sh
```

## Windows

<!-- ```sh
amane1023@amane1023:~/KCL_AI$ sh setup.sh
The virtual environment was not created successfully because ensurepip is not
available.  On Debian/Ubuntu systems, you need to install the python3-venv
package using the following command.

    apt install python3.10-venv

You may need to use sudo with that command.  After installing the python3-venv
package, recreate your virtual environment.

Failing command: /home/amane1023/KCL_AI/venv/bin/python3

setup.sh: 2: .: cannot open ./venv/bin/activate: No such file
```
このようなエラーが出た場合は、以下のコマンドを実行する -->
WSL上のUbuntu環境で行う
```
sudo apt install python3.10-venv
sh setup.sh
```

