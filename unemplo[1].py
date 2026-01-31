import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("Unemployment in India.csv")
df.columns = df.columns.str.strip()
df = df.dropna()

df["Date"] = pd.to_datetime(df["Date"])
df = df.sort_values("Date")

print(df.head())
print("\n✅ Rows:", df.shape[0], "Columns:", df.shape[1])

plt.figure(figsize=(10,5))
plt.plot(df["Date"], df["Estimated Unemployment Rate (%)"])
plt.title("Unemployment Rate Over Time (India)")
plt.xlabel("Date")
plt.ylabel("Unemployment Rate (%)")
plt.xticks(rotation=45)
plt.grid(True)
plt.show()
