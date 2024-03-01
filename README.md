# py-bashrc
## version 0.1.0
Environment development for python developer with bash or zsh profile\
by copying the content inside env.bashrc to ~/.bashrc or ~/.bash_profile or ~/.zshrc or others\
Copy these lines to your current theme base on your environment installation.
```
#-------------------------------#
# auth: masakokh                #
# note: python's dev avarialbles#
# year: 2023                    #
# version: 1.0.0                #
#-------------------------------#
## put it in bashrc
alias python3="python3.12"
alias pya="source .venv/bin/activate"
alias pyd="deactivate;rm -rf .venv;"
alias pyc="python3 -m venv .venv;"
alias pyi="pip install --upgrade pip;pip install -r requirements.txt;"
# mac is okay
# alias pye="pyc;pya;"
# both linux and mac
alias pye="python3 -m venv .venv;source .venv/bin/activate"
alias pyp="pip install --upgrade pip;pip install build;pip install twine;"
alias pyu="python -m twine upload dist/* --verbose;"
# mac is okay
# alias pyb="pyp;rm -rf build;rm -rf dist;python -m build;pyu;"
# both linux and mac
alias pyb="pip install --upgrade pip;pip install build;pip install twine;rm -rf build;rm -rf dist;python -m build;python -m twine upload dist/* --verbose;"
# run a startup file
alias pyr="python main.py;"
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

or
## 4. Run a startup file by default as main.py
Some of the editors, and projects create a default file as a startup file.
$ python main.py
```
$ pyr
```

Any way, 'env.json' is everything that stored all.
