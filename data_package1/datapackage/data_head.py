import pandas as pd


def _check_csv_file(filename: str):
    if not filename.endswith(".csv"):
        raise NameError("Podany plik nie jest csv!")


def show_csv_head(filename: str, row_count=5) -> None:
    _check_csv_file(filename)
    reader = pd.read_csv(filename, sep=',', chunksize=row_count)
    chunk = next(reader)
    print(chunk.head())


def get_csv_headers(filename: str):
    _check_csv_file(filename)
    reader = pd.read_csv(filename, sep=',', index_col=0, nrows=0)
    return list(reader.columns)
