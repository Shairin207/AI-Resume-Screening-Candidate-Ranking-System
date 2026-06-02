import pandas as pd


def export_candidates(data):

    df = pd.DataFrame(data)

    df.to_csv(
        "shortlisted/shortlisted_candidates.csv",
        index=False
    )

    return "shortlisted/shortlisted_candidates.csv"