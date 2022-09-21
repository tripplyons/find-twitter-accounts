# Find Twitter Accounts
Find and classify Twitter accounts using a machine learning model

## Use cases

- Finding bot accounts
- Finding accounts of cryptocurrency projects
- Finding any other kind of account you can make a dataset for

## Installation

```bash
conda env create -f environment.yml
conda activate twitter
```

## Usage

### Labeling data

This will create or add to a dataset stored in `out.json`.

```bash
python labeling.py <hastag to find tweets> <number of tweets to label users>
```

### Training a classifier

This will train a linear classifier on transformer output embeddings.

It will use the dataset defined in `out.json` and save a model to `classifier.pkl`:

```bash
python classifier.py
```

### Finding accounts

This will find embeddings of scraped accounts and use the classifier to classify them.

It will output links to any accounts with a specified label.

```bash
python main.py <hashtag to find tweets> <number of tweets to find users> <label to search for>
```

## Details

### Input format for the model

```
Display Name (@username):
Profile description.
```

## Credits

- https://huggingface.co/sentence-transformers/all-mpnet-base-v2 (Model Used)
- https://github.com/JustAnotherArchivist/snscrape (Twitter Scraper)
