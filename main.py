from modules.processor import TextProcessor


def main():
    with open("data/sample.txt", "r", encoding="utf-8") as f:
        text = f.read()

    processor = TextProcessor()
    results = processor.analyze_text(text)

    print("--- Analysis results ---")
    for item in results:
        print(f"Word: {item['word']:15} | Pos: {item['pos']}")


if __name__ == "__main__":
    main()
