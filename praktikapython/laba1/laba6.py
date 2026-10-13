import numpy as np

v1 = np.array([1, 2, 3])
v2 = np.array([1, 4, 9])
v3 = np.array([1, 8, 27])

print("Вектор v1:", v1)
print("Вектор v2:", v2)
print("Вектор v3:", v3)
print()

matrix = np.vstack([v1, v2, v3])

print("Матрица 3x3 (векторы как строки):")
print(matrix)
print()

try:
    inverse_matrix = np.linalg.inv(matrix)
    print("Обратная матрица:")
    print(inverse_matrix)
    print()
    
    identity_matrix = np.dot(matrix, inverse_matrix)
    print("Проверка: A * A^(-1) =")
    print(identity_matrix)
    print()
    
    identity_matrix_rounded = np.round(identity_matrix, decimals=5)
    print("Проверка (округлено до 5 знаков):")
    print(identity_matrix_rounded)
    
except np.linalg.LinAlgError:
    print("Ошибка: матрица вырожденная (определитель равен 0), обратной матрицы не существует!")

print("\n" + "="*50)
print("ДОПОЛНИТЕЛЬНАЯ ИНФОРМАЦИЯ")
print("="*50)

det = np.linalg.det(matrix)
print(f"Определитель матрицы: {det:.6f}")

if det != 0:
    print("✓ Матрица обратима (определитель ≠ 0)")
else:
    print("✗ Матрица вырожденная (определитель = 0)")

print(f"Размерность матрицы: {matrix.shape}")
print(f"Тип данных: {matrix.dtype}")