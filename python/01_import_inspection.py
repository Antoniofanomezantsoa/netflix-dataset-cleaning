import marimo

__generated_with = "0.25.0"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo

    return (mo,)


@app.cell
def _():
    import pandas as pd
    from pathlib import Path

    return Path, pd


@app.cell
def _(Path):
    chemin = Path(__file__).resolve().parent.parent / "data" / "raw" / "netflix_titles.csv"
    chemin.exists()
    return (chemin,)


@app.cell
def _(chemin, pd):
    df_brut = pd.read_csv(chemin)
    return (df_brut,)


@app.cell
def _(df_brut):
    df_brut.shape
    return


@app.cell
def _(mo):
    _df = mo.sql(
        f"""
        df_brut.head()
        """
    )
    return


@app.cell
def _(df_brut):
    df_brut.dtypes.to_frame("type")
    return


@app.cell
def _(df_brut):
    df_brut.info()
    return


@app.cell
def _(df_brut):
    df_brut.isna().sum().sort_values(ascending=False).to_frame("manquants")
    return


@app.cell
def _(df_brut):
    df_brut.duplicated().sum()
    return


@app.cell
def _(df_brut):
    df_brut.nunique().to_frame("valeurs_uniques")
    return


@app.cell
def _(df_brut):
    df_brut["rating"].value_counts()
    return


@app.cell
def _(df_brut):
    df_brut["date_added"].dropna().head(10).tolist()
    return


@app.cell
def _(df_brut):
    df_brut["type"].value_counts(dropna=False) 
    return


@app.cell
def _(df_brut):
    df_brut["rating"].value_counts(dropna=False)
    return


@app.cell
def _(df_brut):
    shifted_rows = df_brut[df_brut["rating"].isin(["74 min", "84 min", "66 min"])]
    shifted_rows
    return


@app.cell
def _(df_brut):
    shift_mask = df_brut["rating"].isin(["74 min", "84 min", "66 min"])
    shift_mask.value_counts()
    return (shift_mask,)


@app.cell
def _(df_brut, shift_mask):
    df_brut.loc[shift_mask, "duration"] = df_brut.loc[shift_mask, "rating"]
    df_brut.loc[shift_mask, "rating"] = None
    return


@app.cell
def _(df_brut, shift_mask):
    df_brut.loc[shift_mask]
    return


@app.cell
def _(df_brut):
    df_brut["rating"].value_counts(dropna=False)
    return


@app.cell
def _(df_brut):
    df_brut.groupby("type")["rating"].value_counts()
    return


@app.cell
def _(df_brut):
    df_brut["rating"] = df_brut["rating"].fillna(df_brut["rating"].mode()[0])
    return


@app.cell
def _(df_brut):
    df_brut["rating"].isna().sum()
    return


@app.cell
def _(df_brut):
    df_brut.isna().sum()
    return


@app.cell
def _(df_brut):
    for col in ['director', 'cast', 'country']:
        df_brut[col] = df_brut[col].fillna('Unknown') 
    return


@app.cell
def _(df_brut):
    df_brut[['director', 'cast', 'country']].isna().sum()
    return


@app.cell
def _(df_brut):
    (df_brut["director"] == 'Unknown').sum(), ((df_brut["director"] == 'Unknown') & (df_brut["cast"] == 'Unknown')).sum()
    return


if __name__ == "__main__":
    app.run()
