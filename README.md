# py-bashrc
Environment development for python developer with bash or zsh profile\
by copying the content inside env.bashrc to ~/.bashrc or ~/.bash_profile or ~/.zshrc
```
alias penv="source venv/bin/activate"
alias pvev="python3.10 -m venv venv"
alias peni="pvev;penv;"
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


or\
## 3. Combining both of 1 and 2
```
$ peni
```
