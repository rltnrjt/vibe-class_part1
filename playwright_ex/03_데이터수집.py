"""
예제 3: 웹에서 데이터 수집 (스크래핑)
- 네이버 뉴스에서 헤드라인 뉴스 제목 수집
- 수집한 데이터 출력 및 파일 저장
"""

from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)  # headless=True → 창 안 보이고 백그라운드 실행
    page = browser.new_page()

    # 네이버 뉴스 접속
    page.goto("https://news.naver.com/")
    page.wait_for_load_state("networkidle")
    print("네이버 뉴스 접속 완료\n")

    # 뉴스 제목 요소들 찾기
    news_items = page.query_selector_all(".sa_text_title")  # 뉴스 제목 선택자

    if not news_items:
        # 대안 선택자 시도
        news_items = page.query_selector_all(".nclicks")

    print("=" * 50)
    print("수집된 뉴스 제목")
    print("=" * 50)

    titles = []
    for i, item in enumerate(news_items[:10], 1):  # 최대 10개
        title = item.inner_text().strip()
        if title:
            titles.append(title)
            print(f"{i}. {title}")

    print("=" * 50)
    print(f"총 {len(titles)}개 수집 완료")

    # 결과를 파일로 저장
    with open("news_titles.txt", "w", encoding="utf-8") as f:
        f.write("네이버 뉴스 헤드라인\n")
        f.write("=" * 50 + "\n")
        for i, title in enumerate(titles, 1):
            f.write(f"{i}. {title}\n")

    print("파일 저장 완료: news_titles.txt")
    browser.close()
