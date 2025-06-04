import matplotlib.pyplot as plt
import numpy as np

# Data
months = ['07/2019', '08/2019', '09/2019', '10/2019', '11/2019']
searches = [50, 53, 59, 56, 62]
direct = [39, 47, 42, 51, 51]
social_media = [70, 80, 90, 87, 92]

# Bar positions
x = np.arange(len(months))
width = 0.25

# Plot
plt.figure(figsize=(10, 6))
bars1 = plt.bar(x - width, searches, width=width, label='Searches', color='dodgerblue')
bars2 = plt.bar(x, direct, width=width, label='Direct', color='lightcoral')
bars3 = plt.bar(x + width, social_media, width=width, label='Social Media', color='orange')

# Add labels on top of each bar
for bar in bars1:
    plt.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 1, str(bar.get_height()),
             ha='center', va='bottom', fontsize=8)
for bar in bars2:
    plt.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 1, str(bar.get_height()),
             ha='center', va='bottom', fontsize=8)
for bar in bars3:
    plt.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 1, str(bar.get_height()),
             ha='center', va='bottom', fontsize=8)

# Axes and labels
plt.xticks(x, months)
plt.ylabel("visitors in thousands")
plt.title("Visitors by web traffic sources")

# Move legend below the plot
plt.legend(loc='upper center', bbox_to_anchor=(0.5, -0.1), ncol=3)

# Tight layout and show
plt.tight_layout()
plt.show()
