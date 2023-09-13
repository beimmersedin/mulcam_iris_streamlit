import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# 한글폰트 적용
# 폰트 적용
import os
import matplotlib.font_manager as fm  # 폰트 관련 용도 as fm
fpath = os.path.join(os.getcwd(), "Nanum_Gothic/NanumGothic-Bold.ttf")
prop = fm.FontProperties(fname=fpath)

# Windows
plt.rcParams['font.family'] = "NanumGothic"
plt.rcParams['axes.unicode_minus'] = False


# 한글 폰트 설정
# plt.rcParams['font.family'] = "AppleGothic"


# DataFrame 생성
data = pd.DataFrame({
    '이름': ['영식', '철수', '영희'],
    '나이': [22, 31, 25],
    '몸무게': [75.5, 80.2, 55.1]
})

fig, ax = plt.subplots()

def run_graph_1():
    fig, ax = plt.subplots()
    ax.bar(data['이름'], data['나이'])
    # st.pyplot(fig)

    barplot = sns.barplot(x='이름', y='나이', data=data, ax=ax, palette='Set2')
    fig = barplot.get_figure()


st.dataframe(data, use_container_width=True)
st.pyplot(fig)

#############

# labels = ['G1', 'G2', 'G3', 'G4', 'G5']
# men_means = [20, 35, 30, 35, 27]
# women_means = [25, 32, 34, 20, 25]
# men_std = [2, 3, 4, 1, 2]
# women_std = [3, 5, 2, 3, 3]
# width = 0.35       # the width of the bars: can also be len(x) sequence

# fig, ax = plt.subplots()

# ax.bar(labels, men_means, width, yerr=men_std, label='Men')
# ax.bar(labels, women_means, width, yerr=women_std, bottom=men_means,
#        label='Women')

# ax.set_ylabel('Scores')
# ax.set_title('Scores by group and gender')
# ax.legend()

# st.pyplot(fig)
