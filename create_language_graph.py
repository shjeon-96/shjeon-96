import matplotlib.pyplot as plt
import json

# 언어별 라인 수를 저장할 딕셔너리
languages = {}

# 언어 통계를 가져올 파일 (languages.json)
with open('languages.json', 'r') as f:
    data = json.load(f)

# 가져온 데이터를 언어별 라인 수로 변환
for language, lines in data.items():
    languages[language] = lines

# 언어별 라인 수 그래프 그리기
plt.figure(figsize=(10, 6))
plt.barh(list(languages.keys()), list(languages.values()), color='skyblue')
plt.xlabel('Line Count')
plt.title('Programming Languages by Line Count')
plt.gca().invert_yaxis()  # 상단이 가장 큰 값이 오도록 설정
plt.tight_layout()

# 이미지로 저장
plt.savefig('languages_graph.png')
