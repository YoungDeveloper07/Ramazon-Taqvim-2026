import aiohttp
from bs4 import BeautifulSoup


# Funksiyani 'async' (asinxron) qildik
async def hamma_vaqtlar(viloyat):
    url = f"https://namozvaqti.uz/shahar/{viloyat}"

    try:
        # aiohttp orqali saytga ulanamiz (bu botni qotirmaydi)
        async with aiohttp.ClientSession() as session:
            async with session.get(url, timeout=5) as response:
                if response.status == 200:
                    html = await response.text()
                    soup = BeautifulSoup(html, "html.parser")

                    times = soup.select(".time")
                    if not times:
                        return None

                    data = {
                        "shahar": soup.select(".vil")[0].text.strip(),
                        "bomdod": times[0].text,
                        "quyosh": times[1].text,
                        "peshin": times[2].text,
                        "asr": times[3].text,
                        "shom": times[4].text,
                        "xufton": times[5].text
                    }
                    return data
                else:
                    return None
    except Exception as e:
        print(f"Xatolik: {e}")
        return None