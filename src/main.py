from pathlib import Path
import pandas as pd

BASE_DIR = Path(__file__).resolve().parents[1]
DATA_PATH = BASE_DIR / "data" / "sample_transactions.csv"
OUTPUT_DIR = BASE_DIR / "output"


def load_transactions(path: Path) -> pd.DataFrame:
    if not path.exists():
        raise FileNotFoundError(f"Data file not found: {path}")
    df = pd.read_csv(path)
    return df


def summarize_by_type(df: pd.DataFrame) -> pd.DataFrame:
    summary = (
        df.groupby("type", as_index=False)["amount"]
        .sum()
        .rename(columns={"amount": "total_amount"})
    )
    return summary


def summarize_by_account(df: pd.DataFrame) -> pd.DataFrame:
    summary = (
        df.groupby("account_code", as_index=False)["amount"]
        .sum()
        .rename(columns={"amount": "total_amount"})
    )
    return summary


def summarize_daily_net(df: pd.DataFrame) -> pd.DataFrame:
    pivot = (
        df.pivot_table(
            index="date",
            columns="type",
            values="amount",
            aggfunc="sum",
            fill_value=0.0,
        )
        .reset_index()
    )

    if "Income" not in pivot.columns:
        pivot["Income"] = 0.0
    if "Expense" not in pivot.columns:
        pivot["Expense"] = 0.0

    
    pivot["net_income"] = pivot["Income"] + pivot["Expense"]

    daily_summary = pivot[["date", "Income", "Expense", "net_income"]]
    return daily_summary


def save_summary(df: pd.DataFrame, filename: str) -> None:
    OUTPUT_DIR.mkdir(exist_ok=True)
    out_path = OUTPUT_DIR / filename
    df.to_csv(out_path, index=False)
    print(f"Saved: {out_path}")


def main() -> None:
    print("=== Starting script ===")
    print(f"Base dir: {BASE_DIR}")
    print(f"Data path: {DATA_PATH}")

    df = load_transactions(DATA_PATH)

    print("\n=== Raw data (head) ===")
    print(df.head())

    print("\n=== Summary by type ===")
    by_type = summarize_by_type(df)
    print(by_type)
    save_summary(by_type, "summary_by_type.csv")

    print("\n=== Summary by account_code ===")
    by_account = summarize_by_account(df)
    print(by_account)
    save_summary(by_account, "summary_by_account.csv")

    print("\n=== Daily net income summary ===")
    daily_net = summarize_daily_net(df)
    print(daily_net)
    save_summary(daily_net, "daily_summary.csv")

    print("\nDone.")


if __name__ == "__main__":
    main()
