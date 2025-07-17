# Shopping Agent

A simple FastAPI shopping agent.

## Features
- Checks if a product is available
- Shows product price
- Uses CSV as data source

# folder must be like this

shopping_agent/
├── static/
│   └── script.js
├── templates/
│   └── index.html
├── main.py
├── products.csv

# after this open the terminal 
- cd "your folder direction"
- enter this "pip install fastapi uvicorn"
- enter this "pip freeze > requirements.txt"
- "uvicorn main:app --reload
"
- visit this "http://127.0.0.1:8000/"


