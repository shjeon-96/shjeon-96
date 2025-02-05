import json
import matplotlib.pyplot as plt
import os

# GitHub 스타일 설정
plt.style.use("ggplot")  # GitHub와 잘 어울리는 스타일 적용

# JSON 파일 읽기
with open("languages.json", "r") as f:
    data = json.load(f)

# 데이터 변환 및 정렬
languages = {}
for language, lines in data.items():
    try:
        languages[language] = int(lines)  # 문자열을 정수로 변환
    except ValueError:
        print(f"⚠️ Skipping invalid entry: {language} -> {lines}")

sorted_languages = sorted(languages.items(), key=lambda x: x[1], reverse=True)

# 데이터 분리
langs, counts = zip(*sorted_languages) if sorted_languages else ([], [])

# GitHub 다크/라이트 모드 대응 색상
colors = ["#58A6FF" if i % 2 == 0 else "#6E7681" for i in range(len(langs))]  # GitHub 블루 + 회색

# 그래프 생성
plt.figure(figsize=(10, 5), dpi=100)
bars = plt.barh(langs, counts, color=colors, edgecolor="none")

# 막대 모서리 둥글게 만들기
for bar in bars:
    bar.set_linewidth(1.5)
    bar.set_edgecolor("white")  # 다크 모드에서도 보이게 설정
    bar.set_alpha(0.9)

# 텍스트 스타일
plt.xlabel("Lines of Code", fontsize=12, fontweight="bold", color="#C9D1D9")  # GitHub 스타일 색상
plt.ylabel("Programming Languages", fontsize=12, fontweight="bold", color="#C9D1D9")
plt.title("Language Usage Statistics", fontsize=14, fontweight="bold", color="#C9D1D9")
plt.gca().invert_yaxis()  # 값이 큰 언어를 위쪽으로 정렬

# 배경색 투명하게 설정 (GitHub Markdown에서 자연스럽게 보이도록)
plt.gca().set_facecolor("none")
plt.savefig("language_graph.png", bbox_inches="tight", transparent=True)

# 생성된 파일 확인
if os.path.exists("language_graph.png"):
    print("✅ language_graph.png 파일 생성 완료!")
else:
    print("❌ language_graph.png 파일 생성 실패!")


# GitHub 스타일 설정
plt.style.use("ggplot")

# JSON 파일 읽기
with open("languages.json", "r") as f:
    data = json.load(f)

# 데이터 변환 및 정렬
languages = {}
for language, lines in data.items():
    try:
        languages[language] = int(lines)
    except ValueError:
        print(f"⚠️ Skipping invalid entry: {language} -> {lines}")

sorted_languages = sorted(languages.items(), key=lambda x: x[1], reverse=True)

# 데이터 분리
langs, counts = zip(*sorted_languages) if sorted_languages else ([], [])

# GitHub 다크/라이트 모드 대응 색상
colors = [
    "#58A6FF", "#6E7681", "#8B949E", "#D2A8FF", "#F778BA",
    "#A5D6FF", "#FFDD73", "#79C0FF", "#E34C26", "#6F42C1"
]

# 원형 그래프 생성
plt.figure(figsize=(8, 8), dpi=100)
plt.pie(counts, labels=langs, autopct="%1.1f%%", colors=colors[:len(langs)], 
        startangle=140, wedgeprops={"edgecolor": "white", "linewidth": 1.5})

# 타이틀 설정
plt.title("Language Usage Statistics", fontsize=14, fontweight="bold", color="#C9D1D9")

# 배경 투명 설정 (GitHub Markdown에 자연스럽게 표시되도록)
plt.gca().set_facecolor("none")

# 그래프 저장
plt.savefig("language_pie_chart.png", bbox_inches="tight", transparent=True)

# 생성된 파일 확인
if os.path.exists("language_pie_chart.png"):
    print("✅ language_pie_chart.png 파일 생성 완료!")
else:
    print("❌ language_pie_chart.png 파일 생성 실패!")
