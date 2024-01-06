# py-bashrc
Environment development for python developer with bash or zsh profile\
by copying the content inside env.bashrc to ~/.bashrc or ~/.bash_profile or ~/.zshrc or others\

Copy these lines to your current theme base on your environment installation.
```
alias python3="python3.12"
alias pya="source venv/bin/activate"
alias pyd="deactivate;rm -rf venv;"
alias pyc="python3 -m venv venv;"
alias pyr="pip install --upgrade pip;pip install -r requirements.txt;"
alias pye="pyc;pya;"
# pypi
alias pyp="pip install --upgrade pip;pip install build;pip install twine;"
alias pyu="python -m twine upload dist/* --verbose;"
alias pyb="pyp;rm -rf build;rm -rf dist;python -m build;pyu;"
```

or just run this command:
```
$ python3.12 generate.py
```

Then try activating the update by use below command
```
$ source ~/.bashrc
```

## 1. Creating folder environment
```
$ pyc
```
Will run this "python3.10 -m venv .venv"

## 2. Activating local environment
```
$ pya
```
This command is the same as "source .venv/bin/activate"


or
## 3. Combining both of 1 and 2
```
$ pye
```

Any way, 'env.json' is everything that stored all.
