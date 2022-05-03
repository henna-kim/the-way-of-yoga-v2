
## Run Locally

Clone the project

```bash
  git clone git@github.com:henna-kim/the-way-of-yoga-v2.git
```

Go to the project directory

```bash
  cd the-way-of-yoga-v2
```

Install dependencies

```bash
  python3 -m venv venv
  source venv/bin/activate
  pip install --upgrade pip
  pip install -r requirements.txt
```

Start the server

```bash
  uvicorn app.main:app --reload --port=8080 --host=0.0.0.0
```

visit http://localhost:8080
