import numpy as np
import pickle
from datetime import datetime

from sklearn.linear_model import Ridge

dane = np.array([
    2015,
    "Volvo",
    "S60",
    "T5",
    "Sedan",
    "automatic",
    "yv1612tb4f1310987",
    "ca",
    4.1,
    14282,
    "white",
    "black",
    "volvo na rep/world omni",
    27500,
    datetime.now
    ])

model: Ridge = pickle.load(open('../../autocarml/data/03_models/kedro_best_model.pkl', 'rb'))
print(model.n_features_in_)
print(model)

model.predict(dane)
