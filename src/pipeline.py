import cleaning
import pandas as pd

FILE_PATH = "../data/King_County_House_prices_dataset.csv"
OUTPUT_PATH = "../data/cleaned_data.csv"

def main(input_path: str = FILE_PATH, output_path: str = OUTPUT_PATH):
    df = pd.read_csv(input_path)
    df = cleaning.drop_bedroom_outliers(df)
    df = cleaning.recalculate_sqft_basement(df)
    df = cleaning.fill_na_with_most_common_value(df)
    df = cleaning.last_known_change(df)
    df = cleaning.drop_columns(df)
    df.to_csv(output_path, index=False)

if __name__ == "__main__":
    main()