from twitter import Twitter
import sys
import json
import getch
import os

if __name__ == '__main__':
    t = Twitter()\

    dataset = {}
    if os.path.exists('dataset.json'):
        with open('dataset.json', 'r') as f:
            dataset = json.load(f)

    query = sys.argv[1]
    num_tweets = int(sys.argv[2])
    profiles = t.profiles_from_search(query, num_tweets)

    for profile in profiles:
        text = str(profile)
        if text not in dataset:
            print('-' * 64)
            print(text)
            print('-' * 64)
            print('Enter a label (0-9):')
            char = getch.getche()
            while char not in '0123456789':
                char = getch.getche()
            dataset[text] = int(char)

    with open('dataset.json', 'w') as f:
        json.dump(dataset, f, indent=4)
