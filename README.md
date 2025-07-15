# Shopping Agent

A simple FastAPI shopping agent.

## Features
- Checks if a product is available
- Shows product price
- Uses CSV as data source
- Dockerized
- Ready for Cloud Run or Fly.io

## Run locally
```bash
uvicorn main:app --reload

docker build -t shopping-agent .
docker run -p 8080:8080 shopping-agent

Check it

http://localhost:8080/

http://localhost:8080/check?name=apple