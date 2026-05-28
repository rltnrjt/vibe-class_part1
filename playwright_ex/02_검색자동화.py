"""
예제 2: 네이버에서 자동으로 검색하기
- 네이버 접속
- 검색창에 키워드 입력
- 엔터 눌러서 검색
- 검색 결과 제목들 출력
"""

from playwright.sync_api import sync_playwright

SEARCH_KEYWORD = "파이썬 playwright"

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False, slow_mo=500)  # slow_mo: 동작 사이 0.5초 딜레이
    page = browser.new_page()

    # 네이버 접속
    page.goto("https://www.naver.com")
    print("네이버 접속 완료")

    # 검색창 클릭 후 키워드 입력
    page.click("#query")  # 검색창 클릭
    page.type("#query", SEARCH_KEYWORD)  # 키워드 입력
    print(f"검색어 입력: {SEARCH_KEYWORD}")

    # 엔터 눌러 검색
    page.press("#query", "Enter")
    page.wait_for_load_state("networkidle")  # 페이지 로딩 완료 대기
    print("검색 완료!")

    # 현재 URL 출력
    print("현재 URL:", page.url)

    # 스크린샷 저장
    page.screenshot(path="search_result.png")
    print("검색결과 스크린샷 저장: search_result.png")

    input("아무 키나 누르면 종료됩니다...")  # 결과 확인용 대기
    browser.close()
