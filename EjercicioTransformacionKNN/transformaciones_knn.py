import sys
from pathlib import Path

def ensure_packages():
    try:
        import pandas as _p
        import numpy as _n
    except Exception:
        import subprocess
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'pandas', 'numpy'])
    try:
        from sklearn.preprocessing import StandardScaler as _scl
    except Exception:
        import subprocess
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'scikit-learn'])


ensure_packages()

import pandas as pd
import numpy as np
from typing import List, Tuple


class FeatureTransformer:
    def __init__(self):
        self.city_cols = None
        self.sex_cols = None
        self.edad_mean = None
        self.edad_std = None
        self.chol_map = {'bajo': 0, 'medio': 1, 'alto': 2, 'muy alto': 3}

    def fit(self, df: pd.DataFrame):
        # map cholesterol ordinal
        # one-hot encode ciudad and sexo
        city_dummies = pd.get_dummies(df['ciudad'], prefix='ciudad')
        sex_dummies = pd.get_dummies(df['sexo'].astype(str), prefix='sexo')
        self.city_cols = list(city_dummies.columns)
        self.sex_cols = list(sex_dummies.columns)
        # compute mean/std for edad (StandardScaler-like)
        self.edad_mean = df['edad'].mean()
        # use population std (ddof=0) to match StandardScaler
        self.edad_std = df['edad'].std(ddof=0) if df['edad'].std(ddof=0) != 0 else 1.0

    def transform(self, df: pd.DataFrame) -> pd.DataFrame:
        df = df.copy()
        # map colesterol
        df['colesterol_ord'] = df['colesterol'].map(self.chol_map).astype(float)
        # map sexo and ciudad to dummies, ensure same columns as training
        city_dummies = pd.get_dummies(df['ciudad'], prefix='ciudad')
        sex_dummies = pd.get_dummies(df['sexo'].astype(str), prefix='sexo')
        # reindex to stored columns
        for c in (self.city_cols or []):
            if c not in city_dummies:
                city_dummies[c] = 0
        for c in (self.sex_cols or []):
            if c not in sex_dummies:
                sex_dummies[c] = 0
        city_dummies = city_dummies.reindex(sorted(self.city_cols), axis=1)
        sex_dummies = sex_dummies.reindex(sorted(self.sex_cols), axis=1)

        # scale edad using fitted mean/std
        df['edad_scaled'] = (df['edad'] - self.edad_mean) / self.edad_std

        # final feature set: edad_scaled, colesterol_ord, sexo dummies, ciudad dummies
        features = pd.concat([
            df[['edad_scaled', 'colesterol_ord']].reset_index(drop=True),
            sex_dummies.reset_index(drop=True),
            city_dummies.reset_index(drop=True)
        ], axis=1)
        return features


def euclidean_distances(X: np.ndarray, x_new: np.ndarray) -> np.ndarray:
    # ensure numeric numpy arrays (avoid object-dtype issues)
    X_arr = np.asarray(X, dtype=float)
    x_arr = np.asarray(x_new, dtype=float)
    # broadcast subtraction
    diff = X_arr - x_arr
    return np.sqrt(np.sum(diff ** 2, axis=1))


def knn_predict(X_train: np.ndarray, y_train: np.ndarray, x_new: np.ndarray, k: int = 3) -> Tuple[List[int], List[float], int]:
    dists = euclidean_distances(X_train, x_new)
    idx_sorted = np.argsort(dists)
    neighbors_idx = idx_sorted[:k].tolist()
    neighbors_dists = dists[neighbors_idx].tolist()
    y_arr = np.asarray(y_train)
    votes = y_arr[neighbors_idx]
    # majority vote (ties -> choose 1 if tie and more 1s? here simple sum)
    pred = int(np.round(np.mean(votes)))
    return neighbors_idx, neighbors_dists, pred


def load_dataset(path: Path) -> pd.DataFrame:
    return pd.read_csv(path)


def main():
    base = Path(__file__).parent
    csv_path = base / 'data.csv'
    if not csv_path.exists():
        print(f"No se encuentra {csv_path}. Coloca el CSV en la misma carpeta.")
        return

    df = load_dataset(csv_path)

    # target mapping
    df['diabetes_bin'] = df['diabetes'].map({'no': 0, 'si': 1}).astype(int)

    transformer = FeatureTransformer()
    transformer.fit(df)
    X = transformer.transform(df)
    y = df['diabetes_bin'].to_numpy()

    # ejemplo de paciente nuevo
    nuevo = pd.DataFrame([{
        'sexo': 2,
        'ciudad': 'Cuenca',
        'colesterol': 'alto',
        'edad': 50
    }])

    x_new_feat = transformer.transform(nuevo)

    neighbors_idx, neighbors_dists, pred = knn_predict(X.to_numpy(), y, x_new_feat.to_numpy()[0], k=3)

    print('Distancias calculadas a cada vecino (k=3):')
    print(neighbors_dists)
    print('\nVecinos seleccionados (índices):')
    print(neighbors_idx)
    print('\nRegistros de los vecinos y su etiqueta diabetes:')
    for i in neighbors_idx:
        print(df.iloc[i].to_dict())
    print(f"\nPredicción final (0=no, 1=si): {pred}")


if __name__ == '__main__':
    main()
