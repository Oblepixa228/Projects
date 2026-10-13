import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import cv2
from PIL import Image

image_path = 'photo.jpg'

image_bgr = cv2.imread(image_path)
image_rgb = cv2.cvtColor(image_bgr, cv2.COLOR_BGR2RGB)

image_gray = cv2.cvtColor(image_bgr, cv2.COLOR_BGR2GRAY)

fig, axes = plt.subplots(1, 2, figsize=(12, 6))
fig.suptitle('Загрузка и отображение изображения', fontsize=16, fontweight='bold')

axes[0].imshow(image_rgb)
axes[0].set_title('Цветное изображение (RGB)', fontsize=12)
axes[0].axis('off')

axes[1].imshow(image_gray, cmap='gray')
axes[1].set_title('Градации серого (Grayscale)', fontsize=12)
axes[1].axis('off')

plt.tight_layout()
plt.show()

print(f"Размер изображения: {image_rgb.shape}")
print(f"Размер в градациях серого: {image_gray.shape}")

x = np.arange(-2*np.pi, 2*np.pi + 0.1, 0.1)
y = np.arange(-2*np.pi, 2*np.pi + 0.1, 0.1)

X, Y = np.meshgrid(x, y)

Z = X * Y**2

fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(111, projection='3d')

ax.plot_wireframe(X, Y, Z, color='blue', linewidth=0.5, alpha=0.8)

ax.set_title('Трёхмерный график функции f(x, y) = x·y²', fontsize=14, fontweight='bold')
ax.set_xlabel('X', fontsize=12)
ax.set_ylabel('Y', fontsize=12)
ax.set_zlabel('Z', fontsize=12)

surf = ax.plot_surface(X, Y, Z, cmap='coolwarm', alpha=0.3, linewidth=0, antialiased=True)
fig.colorbar(surf, ax=ax, shrink=0.5, aspect=10, label='Значение функции')

plt.tight_layout()
plt.show()

fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(111, projection='3d')

ax.plot_wireframe(X, Y, Z, color='darkblue', linewidth=0.7, 
                  rstride=2, cstride=2, alpha=0.9)

ax.set_title('Wireframe: f(x, y) = x·y²', fontsize=14, fontweight='bold')
ax.set_xlabel('Ось X', fontsize=12)
ax.set_ylabel('Ось Y', fontsize=12)
ax.set_zlabel('Ось Z', fontsize=12)

ax.view_init(elev=25, azim=-60)

plt.tight_layout()
plt.show()

print("\n" + "="*50)
print("ИНФОРМАЦИЯ О ДАННЫХ ДЛЯ ГРАФИКА")
print("="*50)
print(f"Размер сетки: {X.shape[0]} x {X.shape[1]} точек")
print(f"Диапазон X: от {np.min(X):.2f} до {np.max(X):.2f}")
print(f"Диапазон Y: от {np.min(Y):.2f} до {np.max(Y):.2f}")
print(f"Диапазон Z: от {np.min(Z):.2f} до {np.max(Z):.2f}")
print(f"Среднее значение Z: {np.mean(Z):.2f}")
print(f"Максимальное значение Z: {np.max(Z):.2f}")
print(f"Минимальное значение Z: {np.min(Z):.2f}")