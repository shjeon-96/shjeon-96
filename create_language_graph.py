import json
import matplotlib.pyplot as plt
import os

# languages.json 파일 읽기
with open("languages.json", "r") as f:
    data = json.load(f)

# 데이터 변환
languages = {}
for language, lines in data.items():
    try:
        languages[language] = int(lines)  # 문자열을 정수로 변환
    except ValueError:
        print(f"⚠️ Skipping invalid entry: {language} -> {lines}")

# 언어별 코드 라인 수 정렬
sorted_languages = sorted(languages.items(), key=lambda x: x[1], reverse=True)

# 데이터 분리
langs, counts = zip(*sorted_languages) if sorted_languages else ([], [])

# 그래프 생성
plt.figure(figsize=(10, 5))
plt.barh(langs, counts, color="skyblue")
plt.xlabel("Lines of Code")
plt.ylabel("Programming Languages")
plt.title("Language Usage Statistics")
plt.gca().invert_yaxis()

# 그래프 저장
plt.savefig("language_graph.png", bbox_inches="tight")

# 저장된 파일 확인
if os.path.exists("language_graph.png"):
    print("✅ language_graph.png 파일 생성 완료!")
else:
    print("❌ language_graph.png 파일 생성 실패!")
