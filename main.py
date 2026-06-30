import spacy


def main():
    print("Loading the model...")
    nlp = spacy.load("en_core_web_sm")

    with open("data/sample.txt", "r", encoding="utf-8") as f:
        text = f.read()

    doc = nlp(text)

    print("\n--- Analysis results ---")
    for token in doc:
        print(f"Word: {token.text:15} | POS: {token.pos_}")


if __name__ == "__main__":
    main()
