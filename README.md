# find-twitter-accounts
Finds twitter accounts and classifies them using a BERT model

## Installation

```bash
conda env create -f environment.yml
conda activate twitter
```

## Usage

Labeling data (saves model in `out.json`):

```bash
python labeling.py <hastag to find tweets> <number of tweets to label users>
```

Training the linear model on BERT embeddings (from `out.json` and saves model to `classifier.pkl`):

```bash
python classifier.py
```

Finding accounts that are likely to be of a predicted label:

```bash
python main.py <hashtag to find tweets> <number of tweets to find users> <label to search for>
```

## Credits

- https://huggingface.co/microsoft/xtremedistil-l6-h256-uncased
- https://github.com/JustAnotherArchivist/snscrape
