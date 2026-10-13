import numpy as np
import matplotlib.pyplot as plt

social_networks = ['Одноклассники', 'ВКонтакте', 'RuTube', 'YouTube', 'Яндекс Дзен']
users = [35, 85, 15, 95, 45]
colors = ['#FF6B6B', '#4ECDC4', '#45B7D1', '#FFA07A', '#98D8C8']

plt.figure(figsize=(10, 6))
bars = plt.bar(social_networks, users, color=colors, edgecolor='black', linewidth=1.5)
plt.title('Популярность социальных сетей в России', fontsize=14, fontweight='bold')
plt.xlabel('Социальная сеть', fontsize=12)
plt.ylabel('Количество пользователей (млн)', fontsize=12)
plt.grid(True, axis='y', linestyle='--', alpha=0.7)

for bar, value in zip(bars, users):
    plt.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 1, 
             f'{value} млн', ha='center', va='bottom', fontsize=10)

plt.tight_layout()
plt.show()

plt.figure(figsize=(8, 8))
plt.pie(users, labels=social_networks, colors=colors, autopct='%1.1f%%', 
        startangle=90, explode=[0, 0.05, 0, 0.05, 0], shadow=True)
plt.title('Распределение пользователей по социальным сетям', fontsize=14, fontweight='bold')
plt.tight_layout()
plt.show()

np.random.seed(42)
n_points = 1000
mean = -0.5
variance = 10
std_dev = np.sqrt(variance)

x = np.random.normal(mean, std_dev, n_points)
y = np.random.normal(mean, std_dev, n_points)

plt.figure(figsize=(10, 8))
plt.scatter(x, y, alpha=0.6, s=20, c='blue', edgecolors='black', linewidth=0.5)

plt.title('Распределение 1000 случайных точек (Гауссовское распределение)', fontsize=14, fontweight='bold')
plt.xlabel('X', fontsize=12)
plt.ylabel('Y', fontsize=12)
plt.grid(True, linestyle='--', alpha=0.6)

plt.axhline(y=0, color='red', linestyle='-', linewidth=1, alpha=0.5)
plt.axvline(x=0, color='red', linestyle='-', linewidth=1, alpha=0.5)

plt.text(0.05, 0.95, f'Математическое ожидание: {mean}\nДисперсия: {variance}', 
         transform=plt.gca().transAxes, fontsize=10, 
         bbox=dict(boxstyle="round,pad=0.3", facecolor='white', alpha=0.8))

plt.tight_layout()
plt.show()

fig, axes = plt.subplots(2, 2, figsize=(14, 10))
fig.suptitle('Лабораторная работа: Визуализация данных', fontsize=16, fontweight='bold')

axes[0, 0].bar(social_networks, users, color=colors, edgecolor='black', linewidth=1.5)
axes[0, 0].set_title('Популярность социальных сетей', fontsize=12)
axes[0, 0].set_ylabel('Пользователи (млн)')
axes[0, 0].grid(True, axis='y', linestyle='--', alpha=0.5)
for bar, value in zip(axes[0, 0].patches, users):
    axes[0, 0].text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.5, 
                   f'{value} млн', ha='center', va='bottom', fontsize=9)

axes[0, 1].pie(users, labels=social_networks, colors=colors, autopct='%1.1f%%', 
               startangle=90, explode=[0, 0.03, 0, 0.03, 0])
axes[0, 1].set_title('Доля каждой сети', fontsize=12)

axes[1, 0].scatter(x, y, alpha=0.5, s=15, c='blue')
axes[1, 0].set_title('Гауссовское распределение точек', fontsize=12)
axes[1, 0].set_xlabel('X')
axes[1, 0].set_ylabel('Y')
axes[1, 0].grid(True, linestyle='--', alpha=0.5)
axes[1, 0].axhline(y=0, color='red', linestyle='-', linewidth=1, alpha=0.3)
axes[1, 0].axvline(x=0, color='red', linestyle='-', linewidth=1, alpha=0.3)
axes[1, 0].text(0.05, 0.95, f'μ = {mean}, σ² = {variance}', 
                transform=axes[1, 0].transAxes, fontsize=9,
                bbox=dict(boxstyle="round,pad=0.3", facecolor='white', alpha=0.8))

fig.delaxes(axes[1, 1])

plt.tight_layout()
plt.show()