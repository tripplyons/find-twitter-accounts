# Find Twitter Accounts

Find and classify Twitter accounts using text embeddings

## Use cases

- Finding bot accounts
- Finding accounts of cryptocurrency projects ([example output and dataset](https://gist.github.com/tripplyons/eb5977dcf788ca408f4fe542daeb914e))
- Finding any other kind of account you can make a dataset for

## Installation

```bash
conda env create -f environment.yml
conda activate twitter
```

## Usage

### Labeling data

This will create or add to a dataset stored in `dataset.json`.

```bash
python labeling.py <search query> <number of users to label>
```

### Training a classifier

This will train a linear classifier on embeddings.

It will use the dataset defined in `dataset.json` and save a model to `classifier.pkl`:

```bash
python classifier.py
```

### Finding accounts

This will find embeddings of scraped accounts and use the classifier to classify them.

It will output links to any accounts with a specified label.

```bash
python main.py <search query> <number of tweets to find users> <label to search for>
```

## Details

### Input format for the model

```
Display Name, Username, Profile description
```

## Credits

- https://platform.openai.com/docs/guides/embeddings (Embeddings)
- https://github.com/JustAnotherArchivist/snscrape (Twitter Scraper)
