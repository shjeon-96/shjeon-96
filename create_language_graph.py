import matplotlib.pyplot as plt
import json
from collections import defaultdict

# 언어별 라인 수를 저장할 딕셔너리
languages = defaultdict(int)

# 언어 통계를 가져올 파일 (languages.json)
with open('languages.json', 'r') as f:
    data = json.load(f)

# API 응답이 올바른 데이터인지 확인
if "message" in data:
    print(f"❌ API 오류 발생: {data['message']}")
    exit(1)  # 오류 발생 시 종료

# 가져온 데이터를 언어별 라인 수로 변환 (중복 언어 라인 수 합산)
for language, lines in data.items():
    try:
        languages[language] += int(lines)  # 문자열을 정수로 변환
    except ValueError:
        print(f"⚠️ 변환 오류 발생: {language} -> {lines}")
        continue  # 변환 실패 시 해당 데이터 무시

# 언어별 라인 수 정렬 (내림차순)
sorted_languages = sorted(languages.items(), key=lambda x: x[1], reverse=True)
if not sorted_languages:
    print("⚠️ 언어 데이터가 없습니다.")
    exit(1)

langs, counts = zip(*sorted_languages)

# 언어별 라인 수 그래프 그리기
plt.figure(figsize=(12, 6))
plt.barh(langs, counts, color='skyblue')
plt.xlabel('Line Count')
plt.ylabel('Languages')
plt.title('Programming Languages by Line Count')
plt.gca().invert_yaxis()  # 가장 큰 값이 위에 오도록 설정
plt.tight_layout()

# 이미지로 저장
plt.savefig('languages_graph.png')
