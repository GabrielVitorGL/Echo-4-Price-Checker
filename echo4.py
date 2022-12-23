import requests
from bs4 import BeautifulSoup
import pyshorteners



encurtar=1
paginas_para_pesquisar=8





shortner=pyshorteners.Shortener()
print('\n')
desde = 1
numeracao = 1
for x in range(paginas_para_pesquisar+1):
    url = "https://lista.mercadolivre.com.br/eletronicos-audio-video/audio/assistentes-pessoais/echo-4th-gen_Desde_"+str(desde)+"_OrderId_PRICE_PriceRange_150-0_NoIndex_True"
    page = requests.get(url)

    # Utilize o módulo BeautifulSoup para parsear o conteúdo da página
    soup = BeautifulSoup(page.content, 'html.parser')

    # Encontre todas as tags HTML
    a_tags = soup.find_all('a', {'class': 'ui-search-result__content ui-search-link'})

    product_tags = [a_tag.find('div', {'class': 'ui-search-result__content-wrapper shops__result-content-wrapper'}) for a_tag in a_tags]

    title_tags = [product_tag.find('h2', {'class': 'ui-search-item__title ui-search-item__group__element shops__items-group-details shops__item-title'}) for product_tag in product_tags]
    price_tags = [product_tag.find('span', {'class': 'price-tag-fraction'}) for product_tag in product_tags]

    links = [str(i+10) + ' - ' + a_tag['href'] for i, a_tag in enumerate(a_tags)]
    titles = [str(i+10) + ' - ' + title_tag.text for i, title_tag in enumerate(title_tags)]
    prices = [str(i+10) + ' - ' + price_tag.text for i, price_tag in enumerate(price_tags)]

    new_titles = [
        item for item in titles if 'dot' not in item.lower()
    ]

    new_links = []
    new_prices = []
    for title in new_titles:
        new_prices.append(tuple(item for item in prices if item.lower().startswith(title[0:3])))
        new_links.append(tuple(item for item in links if item.lower().startswith(title[0:3])))

    for i in range(len(new_titles)):
        formated_title = str(new_titles[i])
        print(str(numeracao) + ' - ' + formated_title[5:])

        formated_price = str(new_prices[i])
        print(str(numeracao) + ' - ' + formated_price[7:-3])

        formated_link = str(new_links[i])
        if encurtar == 1:
            print(str(numeracao) + ' - ' + shortner.tinyurl.short(formated_link[7:-3]))
        else:
            print(str(numeracao) + ' - ' + formated_link[7:-3])

        numeracao += 1
        print('\n')

    desde += 48