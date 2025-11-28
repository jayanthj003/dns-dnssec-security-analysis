import pandas as pd
import matplotlib.pyplot as plt
import os

# Map each CSV file to the number of ZSKs it represents
file_key_map = {
    'keys_50.csv': '50 Keys',
    'keys_100.csv': '100 Keys',
    'keys_175.csv': '175 Keys'
}

max_cpu_usage = []
key_labels = []

# Process each file
for file, label in file_key_map.items():
    if not os.path.exists(file):
        print(f"File not found: {file}")
        continue

    df = pd.read_csv(file)
    dns_df = df[df['Container'] == 'local-dns-10.9.0.53'].copy()
    dns_df['CPU%'] = dns_df['CPU%'].str.replace('%', '').astype(float)

    max_cpu = dns_df['CPU%'].max()
    max_cpu_usage.append(max_cpu)
    key_labels.append(label)

# Plotting
colors = ['skyblue', 'orange', 'green', 'violet']
plt.figure(figsize=(10, 6))
bars = plt.bar(key_labels, max_cpu_usage, color=colors)

plt.title("Max Local DNS CPU Usage vs Number of ZSKs")
plt.xlabel("Number of ZSKs")
plt.ylabel("Max CPU Usage (%)")
plt.grid(axis='y', linestyle='--', alpha=0.6)
plt.tight_layout()

# Add value labels on top of bars
for bar in bars:
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2., height + 0.002,
             f'{height:.2f}%', ha='center', va='bottom')

plt.show()

