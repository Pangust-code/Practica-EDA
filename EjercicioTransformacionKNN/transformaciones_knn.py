from pathlib import Path
import sys
from typing import List, Tuple


def ensure_packages():
    """Instala automáticamente las librerías necesarias si no están disponibles."""
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


class FeatureTransformer:
    """Convierte el DataFrame crudo en la matriz numérica para KNN."""

    def __init__(self):
        self.city_cols: List[str] = []
        self.sex_cols: List[str] = []
        self.edad_mean: float = 0.0
        self.edad_std: float = 1.0
        self.chol_map = {'bajo': 0, 'medio': 1, 'alto': 2, 'muy alto': 3}

    def fit(self, df: pd.DataFrame):
        city_dummies = pd.get_dummies(df['ciudad'], prefix='ciudad')
        sex_dummies = pd.get_dummies(df['sexo'].astype(str), prefix='sexo')

        self.city_cols = list(city_dummies.columns)
        self.sex_cols = list(sex_dummies.columns)
        self.edad_mean = float(df['edad'].mean())
        std = float(df['edad'].std(ddof=0))
        self.edad_std = std if std != 0 else 1.0

    def transform(self, df: pd.DataFrame) -> pd.DataFrame:
        """Transforma los datos crudos a un formato numérico listo para KNN."""
        df = df.copy()
        df['colesterol_ord'] = df['colesterol'].map(self.chol_map).astype(float)
        city_dummies = pd.get_dummies(df['ciudad'], prefix='ciudad')
        sex_dummies = pd.get_dummies(df['sexo'].astype(str), prefix='sexo')

        for c in (self.city_cols or []):
            if c not in city_dummies:
                city_dummies[c] = 0
        for c in (self.sex_cols or []):
            if c not in sex_dummies:
                sex_dummies[c] = 0

        city_dummies = city_dummies.reindex(sorted(self.city_cols), axis=1)
        sex_dummies = sex_dummies.reindex(sorted(self.sex_cols), axis=1)
        df['edad_scaled'] = (df['edad'] - self.edad_mean) / self.edad_std

        features = pd.concat([
            df[['edad_scaled', 'colesterol_ord']].reset_index(drop=True),
            sex_dummies.reset_index(drop=True),
            city_dummies.reset_index(drop=True)
        ], axis=1)
        return features


def euclidean_distances(X: np.ndarray, x_new: np.ndarray) -> np.ndarray:
    """Calcula la distancia euclidea entre un punto nuevo y cada fila de X."""
    X_arr = np.asarray(X, dtype=float)
    x_arr = np.asarray(x_new, dtype=float)
    diff = X_arr - x_arr
    return np.sqrt(np.sum(diff ** 2, axis=1))


def knn_predict(X_train: np.ndarray, y_train: np.ndarray, x_new: np.ndarray, k: int = 3) -> Tuple[List[int], List[float], int]:
    """Retorna indices de vecinos, distancias de vecinos y prediccion mayoritaria."""
    dists = euclidean_distances(X_train, x_new)
    idx_sorted = np.argsort(dists)
    neighbors_idx = idx_sorted[:k].tolist()
    neighbors_dists = dists[neighbors_idx].tolist()
    y_arr = np.asarray(y_train)
    votes = y_arr[neighbors_idx]
    pred = int(np.round(np.mean(votes)))
    return neighbors_idx, neighbors_dists, pred


def load_dataset(path: Path) -> pd.DataFrame:
    """Carga un archivo CSV y lo convierte en un DataFrame de pandas."""
    return pd.read_csv(path)


def main():
    """Funcion principal que coordina todo el flujo de KNN."""
    base = Path(__file__).parent
    csv_path = base / 'data.csv'

    if not csv_path.exists():
        print(f"No se encuentra {csv_path}. Coloca data.csv en la misma carpeta.")
        return

    print("\n" + "=" * 80)
    print("PASO 1: CARGAR DATOS")
    print("=" * 80)
    df = load_dataset(csv_path)
    print("Datos originales:")
    print(df)

    print("\n" + "=" * 80)
    print("PASO 2: PREPARAR ETIQUETA TARGET")
    print("=" * 80)
    df['diabetes_bin'] = df['diabetes'].map({'no': 0, 'si': 1}).astype(int)
    print("Etiqueta diabetes mapeada (no=0, si=1):")
    print(df[['diabetes', 'diabetes_bin']])

    print("\n" + "=" * 80)
    print("PASO 3: TRANSFORMAR CARACTERISTICAS")
    print("=" * 80)
    transformer = FeatureTransformer()
    transformer.fit(df)
    print("Parametros aprendidos:")
    print(f"  - Ciudades encontradas: {transformer.city_cols}")
    print(f"  - Sexos encontrados: {transformer.sex_cols}")
    print(f"  - Media de edad: {transformer.edad_mean:.2f}")
    print(f"  - Desv. Est. de edad: {transformer.edad_std:.2f}")

    X = transformer.transform(df)
    y = df['diabetes_bin'].to_numpy()

    print("\n" + "=" * 80)
    print("PASO 4: TABLA ESTANDARIZADA (Datos transformados)")
    print("=" * 80)
    print(X)

    print("\n" + "=" * 80)
    print("PASO 5: NUEVO PACIENTE A PREDECIR")
    print("=" * 80)
    nuevo = pd.DataFrame([{
        'sexo': 2,
        'ciudad': 'Cuenca',
        'colesterol': 'alto',
        'edad': 50
    }])
    print("Datos del nuevo paciente:")
    print(nuevo)

    x_new_feat = transformer.transform(nuevo)
    print("\nNuevo paciente transformado:")
    print(x_new_feat)

    print("\n" + "=" * 80)
    print("PASO 6: CALCULAR K-NEAREST NEIGHBORS (k=3)")
    print("=" * 80)
    neighbors_idx, neighbors_dists, pred = knn_predict(X.to_numpy(), y, x_new_feat.to_numpy()[0], k=3)

    print("\n" + "=" * 80)
    print("PASO 7: RESULTADOS")
    print("=" * 80)
    print("\nDistancias calculadas a cada vecino (k=3):")
    print(neighbors_dists)
    print("\nVecinos seleccionados (indices):")
    print(neighbors_idx)
    print("\nRegistros de los vecinos y su etiqueta diabetes:")
    for i, idx in enumerate(neighbors_idx, 1):
        vecino = df.iloc[idx].to_dict()
        print(f"\n  Vecino {i} (indice {idx}):")
        print(f"    - Sexo: {vecino['sexo']}")
        print(f"    - Ciudad: {vecino['ciudad']}")
        print(f"    - Colesterol: {vecino['colesterol']}")
        print(f"    - Edad: {vecino['edad']}")
        print(f"    - Diabetes: {vecino['diabetes']} ({vecino['diabetes_bin']})")

    print(f"\n{'=' * 80}")
    print(f"PREDICCION FINAL (0=no diabetes, 1=si diabetes): {pred}")
    print(f"{'=' * 80}\n")


if __name__ == '__main__':
    main()
