rm -rf venv

python3.12 -m venv venv

source venv/bin/activate

pip install --upgrade pip

# pip install --upgrade setuptools

# pip install wheel

pip install -r requirements.txt