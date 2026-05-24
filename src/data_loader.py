from posixpath import sep

import pandas as pd


REQUIRED_COLUMNS = [
    "TotalPremium",
    "TotalClaims",
    "Province",
    "VehicleType",
    "Gender",
    "TransactionMonth"
]


def load_data(path):
    """
    Load insurance dataset safely with validation.
    """

    try:
        # Try normal CSV first
        df = pd.read_csv(path,
                          sep="|",
                          low_memory=False)

        # Validate required columns
        missing_cols = [
            col for col in REQUIRED_COLUMNS
            if col not in df.columns
        ]

        if missing_cols:
            raise ValueError(
                f"Missing required columns: {missing_cols}"
            )

        return df

    except FileNotFoundError:
        print(f"Error: File not found -> {path}")
        return None

    except pd.errors.ParserError:
        print("Error: Malformed CSV file.")
        return None

    except UnicodeDecodeError:
        print("Error: Encoding issue while reading CSV.")
        return None

    except Exception as e:
        print(f"Unexpected error: {e}")
        return None