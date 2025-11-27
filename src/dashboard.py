from pathlib import Path

import pandas as pd
import matplotlib.pyplot as plt



BASE_DIR = Path(__file__).resolve().parents[1]
OUTPUT_DIR = BASE_DIR / "output"
IMAGES_DIR = BASE_DIR / "images"


def load_csv(filename: str) -> pd.DataFrame:
    
    path = OUTPUT_DIR / filename
    if not path.exists():
        raise FileNotFoundError(f"File not found: {path}")
    return pd.read_csv(path)


def ensure_images_dir() -> None:
    
    IMAGES_DIR.mkdir(exist_ok=True)


def plot_daily_net_income() -> None:
    
    df = load_csv("daily_summary.csv")

    
    df["date"] = pd.to_datetime(df["date"])

    plt.figure()
    plt.plot(df["date"], df["net_income"])
    plt.xlabel("Date")
    plt.ylabel("Net income")
    plt.title("Daily Net Income")
    plt.xticks(rotation=45)
    plt.tight_layout()

    out_path = IMAGES_DIR / "daily_net_income.png"
    plt.savefig(out_path)
    plt.close()
    print(f"Saved: {out_path}")


def plot_total_by_type() -> None:
    
    df = load_csv("summary_by_type.csv")

    plt.figure()
    plt.bar(df["type"], df["total_amount"])
    plt.xlabel("Type")
    plt.ylabel("Total amount")
    plt.title("Total by Type (Income vs Expense)")
    plt.tight_layout()

    out_path = IMAGES_DIR / "total_by_type.png"
    plt.savefig(out_path)
    plt.close()
    print(f"Saved: {out_path}")


def plot_total_by_account() -> None:
    
    df = load_csv("summary_by_account.csv")

    plt.figure()
    plt.bar(df["account_code"].astype(str), df["total_amount"])
    plt.xlabel("Account code")
    plt.ylabel("Total amount")
    plt.title("Total by Account Code")
    plt.xticks(rotation=45)
    plt.tight_layout()

    out_path = IMAGES_DIR / "total_by_account.png"
    plt.savefig(out_path)
    plt.close()
    print(f"Saved: {out_path}")


def main() -> None:
    print("=== Generating dashboard charts ===")
    print(f"Base dir:   {BASE_DIR}")
    print(f"Output dir: {OUTPUT_DIR}")
    print(f"Images dir: {IMAGES_DIR}")

    ensure_images_dir()

    plot_daily_net_income()
    plot_total_by_type()
    plot_total_by_account()

    print("\nAll charts generated.")


if __name__ == "__main__":
    main()
