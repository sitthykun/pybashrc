# py-bashrc
Environment development for python developer with bash or zsh profile\
by copying the content inside env.bashrc to ~/.bashrc or ~/.bash_profile or ~/.zshrc or others\

Copy these lines to your current theme base on your environment installation.
```
alias python3="python3.10"
alias pya="source venv/bin/activate"
alias pyd="deactivate"
alias pyc="python3 -m venv venv"
alias pye="pyc;pya;"
```

or just run this command:
```
$ python3.10 generate.py
```

Then try activating the update by use below command
```
$ source ~/.bashrc
```

## 1. Creating folder environment
```
$ pvev
```
Will run this "python3.10 -m venv venv"

## 2. Activating local environment
```
$ penv
```
This command is the same as "source venv/bin/activate"


or
## 3. Combining both of 1 and 2
```
$ peni
```

Any way, 'env.json' is everything that stored all.
