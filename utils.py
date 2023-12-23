import numpy as np
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
import seaborn as sns
import pandas as pd
from sklearn.metrics import mean_absolute_error


def get_mae_graficos(X, y, model):
    # Lista de valores para test_size
    test_size_values = [0.25, 0.3]

    # Lista de valores para random_state
    random_state_values = [42, 50, 101, 150]

    # Lista de los resultados para la visualización posterior
    results = []

    # Colores para las líneas
    colors = ['orange', 'green']
    
    fig, axs = plt.subplots(1, 2, figsize=(16, 5))

    # Bucle para probar las diferentes combinaciones de test_size y random_state
    for test_size_val in test_size_values:
        for random_state_val in random_state_values:
            # División del conjunto de datos
            X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size_val, random_state=random_state_val)

            # Escalamiento de las variables 
            scaler = StandardScaler()

            scaler.fit(X_train)

            #Aplicacion de la transformación
            X_train = scaler.transform(X_train)
            X_test = scaler.transform(X_test)

            # Entrenamiento del modelo utilizando el conjunto de entrenamiento
            model.fit(X_train, y_train)

            # Realizar predicciones utilizando el conjunto de prueba
            y_pred = model.predict(X_test)
            
            # Calcular el error (MAE)
            mae = mean_absolute_error(y_test, y_pred)

            # Almacena los resultados para la visualización posterior
            results.append({'test_size': test_size_val, 'random_state': random_state_val, 'mae': mae})

    # -Visualización de los resultados en una gráfica con líneas y leyenda-
    # Se itera sobre los valores de test_size_values y se filtran los resultados para cada valor específico de test_size, luego se extraen los valores de random_state y mae

    for i, test_size_val in enumerate(test_size_values): 
           
        subset_results = [result for result in results if result['test_size'] == test_size_val]
        random_states = [result['random_state'] for result in subset_results]
        maes = [result['mae'] for result in subset_results]

        # Se Agregan etiquetas a cada punto en la gráfica
        for j, txt in enumerate(maes):
            axs[i].annotate(f"{txt:.2f}", (random_states[j], maes[j]), textcoords="offset points", xytext=(0, -11), ha='center', fontsize=7)

        axs[i].plot(random_states, maes, marker='o', label=f'Test Size: {test_size_val}', color=colors[i])
        axs[i].set_xlabel("Random State")
        axs[i].set_ylabel("MAE")
        axs[i].set_title(f"MAE para Test Size: {test_size_val}")
        axs[i].legend()
        
    # Encontrar el menor MAE y los resultados asociados
    min_mae_result = min(results, key=lambda x: x['mae'])
        
    results_all = {
        'mae':  min_mae_result['mae'],
        'test_size': min_mae_result['test_size'],
        'random_state':  min_mae_result['random_state']
    }
    
    return results_all
