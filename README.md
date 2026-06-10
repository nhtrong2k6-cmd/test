# Spam Email Classifier

This repository provides a simple data pipeline and a baseline spam classifier.

Quick commands:

- Prepare data:

```bash
python main.py data
```

- Train baseline model (TF-IDF + LogisticRegression):

```bash
python main.py train --sample-frac 1.0
```

- Predict a single email text:

```bash
python main.py predict "This is an example email body"
```

Models are saved into the `models/` directory.

Requirements: see `requirements.txt`.
