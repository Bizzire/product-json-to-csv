import json
import csv

f = open('productObject.json', "r")

productData = json.loads(f.read())

with open('product-variant-data.csv','w') as csvfile:
    fieldnames = ['title','sku','variant_id']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    
    writer.writeheader()

    if 'products' in productData:
        for products in productData['products']:
            if 'variants' in products:
                for variants in products['variants']:
                    if 'id' in variants:
                        if (variants['title'] == "Default Title"):
                            productTitle = (products['title'])
                        else:
                            productTitle = (products['title'] + " - " + variants['title'])
                        writer.writerow({'title': productTitle, 'sku': variants['sku'], 'variant_id': variants['id']})

print("Writing was completed succesfully")

f.close()