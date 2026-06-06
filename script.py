import os

# 1. png 폴더 안의 모든 파일 이름 가져오기
png_dir = "png"
image_files = [f for f in os.listdir(png_dir) if f.endswith('.png')]

# 2. HTML <img> 태그 형식으로 문자열 만들기
img_tags = ""
for img in image_files:
    # 경로를 png/파일명 으로 지정하고, 드래그 가능하도록 설정합니다.
    img_tags += f'      <img src="png/{img}" alt="" draggable="true" />\n'

# 3. 기존 index.html 파일 읽기
with open("index.html", "r", encoding="utf-8") as f:
    html_content = f.read()

# 4. <div class="cards container"> 내부의 기존 내용(예시 이미지들)을 찾아서 
# 우리가 만든 657개의 애니메이션 이미지 태그로 통째로 교체하기
start_marker = '<div class="cards container">'
end_marker = '</div>'

start_idx = html_content.find(start_marker)

if start_idx != -1:
    # 시작 마커 이후에 나오는 첫 번째 </div> 위치 찾기
    end_idx = html_content.find(end_marker, start_idx) 
    
    # 앞부분 + 새로운 이미지 태그들 + 뒷부분 이어붙이기
    new_html = (
        html_content[:start_idx + len(start_marker)] + "\n" +
        img_tags +
        "    " + html_content[end_idx:]
    )

    # 5. 완성된 내용을 index.html에 덮어쓰기
    with open("index.html", "w", encoding="utf-8") as f:
        f.write(new_html)
        
    print(f"✅ 성공! 총 {len(image_files)}개의 애니메이션 이미지가 index.html에 추가되었습니다.")
else:
    print("❌ index.html에서 '<div class=\"cards container\">'를 찾을 수 없습니다. 원본 파일이 맞는지 확인해주세요.")