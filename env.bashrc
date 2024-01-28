## put it in bashrc
alias python3="python3.12"
alias pya="source .venv/bin/activate"
alias pyd="deactivate;rm -rf .venv;"
alias pyc="python3 -m venv .venv;"
alias pyr="pip install --upgrade pip;pip install -r requirements.txt;"
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
