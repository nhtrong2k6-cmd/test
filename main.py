from src.data_loader import run_data_pipeline

from src.model_train import train_models
from src.predict import predict_email


def main() -> None:
    import argparse

    parser = argparse.ArgumentParser(description="Spam email classifier utilities.")
    sub = parser.add_subparsers(dest="command")

    sub.add_parser("data", help="Run data pipeline (download/prepare datasets)")

    t = sub.add_parser("train", help="Train baseline model")
    t.add_argument("--sample-frac", type=float, default=1.0, help="Fraction of data to use")
    t.add_argument("--no-save", action="store_true", help="Do not save model to disk")

    p = sub.add_parser("predict", help="Predict a single email text")
    p.add_argument("text", nargs="+", help="Email text to classify")

    args = parser.parse_args()

    if args.command == "data":
        run_data_pipeline()
    elif args.command == "train":
        train_models(sample_frac=args.sample_frac, save=not args.no_save)
    elif args.command == "predict":
        text = " ".join(args.text)
        print(predict_email(text))
    else:
        parser.print_help()


if __name__ == "__main__":
    main()

