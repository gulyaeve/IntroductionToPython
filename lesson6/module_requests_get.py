import requests
from PIL import Image
from io import BytesIO


r = requests.get("https://api.thecatapi.com/v1/images/search")


if __name__ == '__main__':
    if r.ok:
        answer = r.json()
        print(answer)
        with open("../lesson7/test.json", "w") as file:
            file.write(str(answer[0]))
        r_dict = dict(answer[0])
        for key, value in r_dict.items():
            print(f"{key} --- {value}")

        cat = requests.get(r_dict['url'])
        cat_image = Image.open(BytesIO(cat.content))
        # cat_image.show()
        cat_image.save(r_dict['url'].split('/')[-1])
        # print(answer[0])
