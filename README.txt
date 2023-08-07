# create venv
python3 -m venv .venv

# activate venv (*nix)
source .venv/bin/activate

# activate venv (win)
.venv\Scripts\activate

# install dependencies
pip install -r requirements.txt

# run locally
flask run

#open browser ->
http://127.0.0.1:5000/api/v1.0/generations/1980

# create docker image
docker build --tag rest-example .

# execute docker
docker run --name generations -p 5995:5000 rest-example

# open browser ->
http://localhost:5995/api/v1.0/generations/1980
http://localhost:5995/api/v1.0/generations/1900
http://localhost:5995/api/v1.0/generations/2000

http://localhost:5995/api/v1.0/generations/3000
