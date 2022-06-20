import asyncio
from pyppeteer import launch
from string import Template

async def scrape_inbox(email):
    try:
        browser = await launch(headless=True)
        page = await browser.newPage()
        await page.goto('https://yopmail.com/en/')

        data = await page.evaluate(Template('document.querySelectorAll("input.ycptinput")[0].value="$value"')
            .substitute(value=email));

        button = await page.querySelector('#refreshbut > button')        
        await button.click()
        await page.waitForNavigation();
        # await page.screenshot({'path': 'output.png'})

        # inbox is loaded so read all emails
        data = await page.evaluate('''() => {
                return Array.from(document.querySelectorAll("#ifinbox")[0].contentWindow.document.querySelectorAll
                ("html > body > div.mctn > div.m")).map(elem => elem.innerText);
            }
        ''') 
        # print(data)
        
        await browser.close()
        return data
    except Exception as e:
        raise e
    
async def scrape_single_email(email,email_index):
    try:
        browser = await launch(headless=True)
        page = await browser.newPage()
        await page.goto('https://yopmail.com/en/')

        await page.evaluate(Template('document.querySelectorAll("input.ycptinput")[0].value="$value"')
            .substitute(value=email));

        button = await page.querySelector('#refreshbut > button')        
        await button.click()
        await page.waitForNavigation();
        # await page.screenshot({'path': 'output.png'})

        # inbox is loaded so read all emails
        emailtext = await page.evaluate(Template('''() => {
                const elems =  Array.from(document.querySelectorAll("#ifinbox")[0].contentWindow.document.querySelectorAll
                ("html > body > div.mctn > div.m"));
                
                elems[$index].click();

                return document.querySelectorAll("#ifmail")[0].contentWindow.document.querySelectorAll
                ("html > body > main")[0].innerText;
            }
        ''').substitute(index=email_index)) 
        # print(data)
        
        await browser.close()
        return emailtext
    except Exception as e:
        raise e


def read_inbox(email):
    return asyncio.get_event_loop().run_until_complete(scrape_inbox(email))
    # return ["Email 1","Email 1","Email 1","Email 1"]

def read_single_email(email,index):
    return asyncio.get_event_loop().run_until_complete(scrape_single_email(email,index))