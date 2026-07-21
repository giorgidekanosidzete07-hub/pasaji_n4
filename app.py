from flask import Flask, render_template

app = Flask(__name__, template_folder='.', static_folder='.')

PRODUCTS = [
    {
        "id": 1,
        "title": "Tommy Jeans T-Shirt",
        "category": "კაცის · მაისური",
        "badge": "ახალი",
        "badge_class": "badge-black",
        "sizes": "S · M · L · XL · XXL",
        "price": "70",
        "image": "https://images.unsplash.com/photo-1521572267360-ee0c2909d518?w=500"
    },
    {
        "id": 2,
        "title": "Slim Tailored Trousers",
        "category": "შარვლები · კლასიკური",
        "badge": "BEST SELLER",
        "badge_class": "badge-gold",
        "sizes": "S · M · L · XL · XXL",
        "price": "80",
        "image": "https://images.unsplash.com/photo-1624378439575-d8705ad7ae80?w=500"
    },
    {
        "id": 3,
        "title": "Linen Relaxed Trousers",
        "category": "შარვლები · ლოფერი",
        "badge": "BEST SELLER",
        "badge_class": "badge-gold",
        "sizes": "XS · S · M · L · XL",
        "price": "80",
        "image": "https://images.unsplash.com/photo-1594633312681-425c7b97ccd1?w=500"
    },
    {
        "id": 4,
        "title": "Jil Sander Oversized Tee",
        "category": "კაცის · მაისური",
        "badge": "BEST SELLER",
        "badge_class": "badge-gold",
        "sizes": "S · M · L · XL · XXL",
        "price": "70",
        "image": "https://images.unsplash.com/photo-1583743814966-8936f5b7be1a?w=500"
    }
]

@app.route('/')
def home():
    return render_template('pasaji_n4_v4.html', products=PRODUCTS)

if __name__ == '__main__':
    app.run(debug=True)
