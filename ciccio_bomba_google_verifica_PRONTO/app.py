from flask import Flask, render_template, jsonify, send_from_directory

app = Flask(__name__)


# Google Search Console verification
@app.route("/google59ef8aeec5880dd8.html")
def google_site_verification():
    return send_from_directory(app.root_path, "google59ef8aeec5880dd8.html", mimetype="text/html")

# Dati Ristorante e Menu per Ciccio Bomba
INFO_RISTORANTE = {
    "nome": "Ciccio Bomba",
    "telefono": "314144212",
    "indirizzo": "via mongraal 2, Mauritius",
    "orario": "Tutti i giorni: 12:00 - 23:30"
}

MENU_ITEMS = [
    # PIZZE
    {
        "id": 1,
        "title": "Pizza Margherita Gourmet",
        "category": "pizze",
        "price": "€10.50",
        "image": "https://images.unsplash.com/photo-1604382354936-07c5d9983bd3?auto=format&fit=crop&w=800&q=80",
        "description": "Pomodoro San Marzano DOP, mozzarella di bufala campana fresca, basilico profumato e olio EVO.",
        "ingredients": "Farina tipo 00 macinata a pietra, lievito madre 48h, pomodoro biologico, mozzarella fresca, basilico.",
        "notes": "Cotta nel forno a legna secondo la classica tradizione napoletana."
    },
    {
        "id": 2,
        "title": "Pizza Diavola Piccante",
        "category": "pizze",
        "price": "€12.00",
        "image": "https://images.unsplash.com/photo-1628840042765-356cda07504e?auto=format&fit=crop&w=800&q=80",
        "description": "Salsa al pomodoro fresco, fior di latte, salame piccante calabrese e peperoncino biologico fresco.",
        "ingredients": "Farina italiana, fior di latte, spianata piccante, olio al peperoncino.",
        "notes": "Per chi ama i sapori decisi e intensi."
    },
    {
        "id": 3,
        "title": "Pizza Tartufata & Porcini",
        "category": "pizze",
        "price": "€15.50",
        "image": "https://images.unsplash.com/photo-1513104890138-7c749659a591?auto=format&fit=crop&w=800&q=80",
        "description": "Crema di tartufo nero di Norcia, funghi porcini trifolati, mozzarella fior di latte e scaglie di parmigiano.",
        "ingredients": "Tartufo nero, porcini freschi, fior di latte, parmigiano reggiano 24 mesi.",
        "notes": "Una vera prelibatezza per intenditori."
    },
    {
        "id": 4,
        "title": "Pizza Tropicale Mauritius",
        "category": "pizze",
        "price": "€13.50",
        "image": "https://images.unsplash.com/photo-1565299624946-b28f40a0ae38?auto=format&fit=crop&w=800&q=80",
        "description": "Specialità della casa con ananas fresco mauriziano, prosciutto cotto scelto e mozzarella filante.",
        "ingredients": "Ananas locale dolce, prosciutto di Parma, fiordilatte fresco.",
        "notes": "Specialità esotica rivisitata in chiave gourmet."
    },

    # PRIMI
    {
        "id": 5,
        "title": "Spaghetti allo Scoglio",
        "category": "primi",
        "price": "€16.00",
        "image": "https://images.unsplash.com/photo-1563379091339-03b21ab4a4f8?auto=format&fit=crop&w=800&q=80",
        "description": "Spaghetti trafilati al bronzo con gamberi, cozze, vongole veraci e calamari sfumati al vino bianco.",
        "ingredients": "Pasta di Gragnano, frutti di mare freschi del giorno, pomodorini pachino, prezzemolo.",
        "notes": "Piatto simbolo della cucina marinara."
    },
    {
        "id": 6,
        "title": "Risotto ai Funghi e Tartufo",
        "category": "primi",
        "price": "€15.00",
        "image": "https://images.unsplash.com/photo-1633964913295-ceb43826e7c9?auto=format&fit=crop&w=800&q=80",
        "description": "Risotto Carnaroli mantecato con burro d'alpeggio, porcini freschi e olio al tartufo bianco.",
        "ingredients": "Riso Carnaroli gran riserva, brodo vegetale, funghi porcini, parmigiano.",
        "notes": "Cremoso, avvolgente e profumato."
    },
    {
        "id": 7,
        "title": "Penne all'Arrabbiata con Burrata",
        "category": "primi",
        "price": "€11.50",
        "image": "https://images.unsplash.com/photo-1621996346565-e3d5d6281313?auto=format&fit=crop&w=800&q=80",
        "description": "Salsa di pomodoro fresco piccante, aglio, peperoncino e una morbida burrata fresca intera al centro.",
        "ingredients": "Penne rigate, pomodoro, peperoncino fresco, burrata pugliese.",
        "notes": "Il contrasto perfetto tra il piccante e la morbidezza della burrata."
    },

    # SECONDI
    {
        "id": 8,
        "title": "Grigliata Mista di Pesce",
        "category": "secondi",
        "price": "€22.00",
        "image": "https://images.unsplash.com/photo-1534422298391-e4f8c172dddb?auto=format&fit=crop&w=800&q=80",
        "description": "Gamberoni reali, filetto di orata, calamari e scampi grigliati serviti con insalatina esotica.",
        "ingredients": "Pesce fresco pescato del giorno, limone mauriziano, erbe aromatiche.",
        "notes": "Cottura alla brace per esaltare il sapore del mare."
    },
    {
        "id": 9,
        "title": "Bistecca alla Fiorentina",
        "category": "secondi",
        "price": "€26.00",
        "image": "https://images.unsplash.com/photo-1544025162-d76694265947?auto=format&fit=crop&w=800&q=80",
        "description": "Taglio pregiato di T-Bone steak frollata 30 giorni, cotta su pietra lavica con sale rosa.",
        "ingredients": "Carne bovina di alta qualità, rosmarino, sale rosa dell'Himalaya, olio EVO.",
        "notes": "Servita con patatine al forno croccanti."
    },

    # ANTIPASTI
    {
        "id": 10,
        "title": "Tagliere Ciccio Bomba",
        "category": "antipasti",
        "price": "€14.00",
        "image": "https://images.unsplash.com/photo-1541529086526-db283c563270?auto=format&fit=crop&w=800&q=80",
        "description": "Selezione di salumi italiani, formaggi stagionati, miele al tartufo, noci e bruschette calde.",
        "ingredients": "Prosciutto crudo, salame, pecorino, gorgonzola, confetture artigianali.",
        "notes": "Ottimo da condividere in 2 o più persone."
    },
    {
        "id": 11,
        "title": "Bruschette Miste della Casa",
        "category": "antipasti",
        "price": "€8.50",
        "image": "https://images.unsplash.com/photo-1572695157366-5e585ab2b69f?auto=format&fit=crop&w=800&q=80",
        "description": "Pane casereccio tostato con pomodoro e basilico, crema di avocado e gamberi, e paté di olive.",
        "ingredients": "Pane a lievitazione naturale, pomodorini, gamberetti, avocado.",
        "notes": "Fresche, croccanti e sfiziose."
    },

    # DRINK
    {
        "id": 12,
        "title": "Cocktail Ciccio Bomba Tropical",
        "category": "drink",
        "price": "€9.00",
        "image": "https://images.unsplash.com/photo-1551024709-8f23befc6f87?auto=format&fit=crop&w=800&q=80",
        "description": "Il nostro drink firma: Rum mauriziano, Curaçao blu, succo d'ananas, lime fresco e menta piperita.",
        "ingredients": "Rum locale, Blue Curaçao, Ananas, Lime, Soda.",
        "notes": "Fresco, fruttato e dal colore verde acqua cristallino."
    },
    {
        "id": 13,
        "title": "Mojito Tradizionale",
        "category": "drink",
        "price": "€8.00",
        "image": "https://images.unsplash.com/photo-1513558161293-cdaf765ed2fd?auto=format&fit=crop&w=800&q=80",
        "description": "Rum bianco, menta fresca pestata al momento, zucchero di canna mauriziano, lime e soda.",
        "ingredients": "Rum, menta, lime, zucchero di canna, ghiaccio tritato.",
        "notes": "Il dissetante ideale per la spiaggia e le sere calde."
    },
    {
        "id": 14,
        "title": "Aperol Spritz Classico",
        "category": "drink",
        "price": "€7.50",
        "image": "https://images.unsplash.com/photo-1560512823-829485b8bf24?auto=format&fit=crop&w=800&q=80",
        "description": "Prosecco DOC, Aperol e selz, servito con fetta d'arancia fresca e ghiaccio.",
        "ingredients": "Prosecco, Aperol, Soda, Arancia.",
        "notes": "L'aperitivo italiano per eccellenza."
    },

    # DOLCI
    {
        "id": 15,
        "title": "Tiramisù Tradizionale al Caffè",
        "category": "dolci",
        "price": "€6.50",
        "image": "https://images.unsplash.com/photo-1571877227200-a0d98ea607e9?auto=format&fit=crop&w=800&q=80",
        "description": "Savoiardi morbidi inzuppati nell'espresso, crema al mascarpone montata e cacao amaro in polvere.",
        "ingredients": "Mascarpone, uova fresche, caffè espresso, cacao amaro.",
        "notes": "Preparato ogni mattina secondo la ricetta della nonna."
    },
    {
        "id": 16,
        "title": "Cheesecake ai Frutti di Bosco",
        "category": "dolci",
        "price": "€7.00",
        "image": "https://images.unsplash.com/photo-1533134242443-d4fd215305ad?auto=format&fit=crop&w=800&q=80",
        "description": "Base croccante di biscotto, morbida crema al formaggio e coulis artigianale ai frutti rossi.",
        "ingredients": "Biscotti digestive, formaggio spalmabile, mirtilli, lamponi, fragole.",
        "notes": "Delizioso equilibrio tra dolcezza e note acidule."
    }
]

@app.route("/")
def home():
    return render_template("index.html", menu=MENU_ITEMS, info=INFO_RISTORANTE)

@app.route("/api/menu")
def get_menu():
    return jsonify(MENU_ITEMS)

if __name__ == "__main__":
    print("Avvio del server Ciccio Bomba su http://127.0.0.1:5000 ...")
    app.run(debug=True, port=5000)
