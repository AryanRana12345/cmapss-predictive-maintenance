import pandas as pd

COLUMNS = (["engine", "cycle"]
           + [f"setting_{i}" for i in range(1, 4)]
           + [f"s{i}" for i in range(1, 22)])


def load_fd(subset="FD001", folder="data"):
    """Read the train, test and true-RUL files of one C-MAPSS subset."""
    train = pd.read_csv(f"{folder}/train_{subset}.txt", sep=r"\s+", header=None, names=COLUMNS)
    test = pd.read_csv(f"{folder}/test_{subset}.txt", sep=r"\s+", header=None, names=COLUMNS)
    rul = pd.read_csv(f"{folder}/RUL_{subset}.txt", sep=r"\s+", header=None, names=["rul"])
    return train, test, rul