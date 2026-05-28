"""
예제 1: 네이버 접속 후 스크린샷 찍기
- 브라우저를 열고 네이버에 접속
- 페이지 타이틀 출력
- 스크린샷 저장
"""

from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    # 브라우저 열기 (headless=False → 브라우저 창이 보임)
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()

    # 네이버 접속
    page.goto("https://www.naver.com")

    # 페이지 타이틀 출력
    print("페이지 제목:", page.title())

    # 스크린샷 저장
    page.screenshot(path="naver_screenshot.png")
    print("스크린샷 저장 완료: naver_screenshot.png")

    browser.close()
