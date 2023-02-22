isort -y --skip __init__.py
black .
tree -a -I '.git|.vscode|__pycache__|run|static_cdn|static' > dir.tree
pipenv graph > graph.txt