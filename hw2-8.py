import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import warnings
warnings.filterwarnings('ignore')

df = pd.read_csv('GBvideos.csv')
objects=["likes","dislikes"]
y_pos = np.arange(len(objects))
like_len=df["likes"].sum()
dislike_len=df["dislikes"].sum()
performance = [like_len,dislike_len]

plt.bar(y_pos, performance, align='center', alpha=0.5)
plt.xticks(y_pos, objects)
plt.ylabel('sayılar')
plt.title('like/dislike in GB')
plt.show()
# plt.figure(figsize=(10, 5))
# plt.subplot(1, 2, 1)
# plt.plot(df['likes'], color='purple')
# plt.ylabel('Değerler')
# plt.title('Rastgele Diziler')
#
# plt.subplot(1, 2, 2)
# plt.plot(df['dislikes'], color='green')
# plt.ylabel('Ötelenmiş Değerler')
# plt.title('Ötelenmiş Diziler')
# plt.show()




