# DocSimilarity

A simple Python script to find similarity between documents using Gemini embeddings.

## Setup

1. Add your API key to a `.env` file:
   ```
   GOOGLE_API_KEY=your_key_here
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

- Run `python similarity.py` to compare a query against a small list of strings.
- Run `python list_models.py` to see available embedding models.

## How it Works

- **Embeddings**: These convert text into a list of numbers (vectors) that represent the "meaning" of the words.
- **Cosine Similarity**: This is a math calculation used to measure how close two vectors are—helping find which documents are most similar to your query.

## Docker (Optional)

If you prefer Docker:
```bash
docker compose up --build
```
