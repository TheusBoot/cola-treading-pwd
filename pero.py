



def run1(context):
    page = context.new_page()
    page.goto('https://page1')
    page.wait_for_timeout(5000)
    page.close()

def run2(context):
    page = context.new_page()
    page.goto('https://page2')
    page.wait_for_timeout(1000)
    page.close()

def main():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        context = browser.new_context()
        t=Thread(target=run1,args=(context,))
        t1=Thread(target=run2,args=(context,))
        t.start()
        t1.start()
        t.join()
        t1.join()
        context.close()
        browser.close()
