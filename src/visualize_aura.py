import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/aura_simulation.csv")
plt.plot(df["Day"], df["Wellbeing_With_AURA"], label="With AURA")
plt.plot(df["Day"], df["Wellbeing_Without_AURA"], label="Without AURA")
plt.xlabel("Day")
plt.ylabel("User Wellbeing")
plt.legend()
plt.savefig("docs/aura_wellbeing.png")
plt.show()
