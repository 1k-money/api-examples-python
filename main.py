import requests

def main():
    print('- - - - - - - - - - - - - - - - - - - - - - - - - ')
    print('The full list of products')
    print()

    response = requests.get('https://1k.money/api/v1/products')
    print(response.json())

    print('- - - - - - - - - - - - - - - - - - - - - - - - - ')
    print('More details on a product, including recent price info')
    print()

    group_key = 'commodities'
    product_key = 'coffee'
    response = requests.get(f'https://1k.money/api/v1/products/{group_key}/{product_key}')
    print(response.json()) 


if __name__ == "__main__":
    main()