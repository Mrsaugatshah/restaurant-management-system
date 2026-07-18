# ---------------------------------
# Kitchen Stations
# ---------------------------------

KITCHEN_STATIONS = {

    # Breakfast preparation area
    "BREAKFAST": "Breakfast Station",

    # Momo preparation area
    "MOMO": "Momo Station",

    # Chowmein/noodles area
    "NOODLES": "Noodles Station",

    # Main food preparation
    "MAIN": "Main Kitchen",

    # Curry preparation
    "CURRY": "Curry Station",

    # Snacks/frying area
    "SNACK": "Snack Station",

    # Beverage area
    "DRINK": "Bar Station",

    # Dessert area
    "DESSERT": "Dessert Station",
}



# ---------------------------------
# Restaurant Menu Data
# ---------------------------------

RESTAURANT_MENU = {


    # ---------------------------------
    # Breakfast Items
    # ---------------------------------

    "Breakfast": [

        {
            "name": "Sel Roti",
            "price": 80,
            "description": "Traditional homemade rice bread",
            "priority": "2",
            "est_time": 10,
            "station": KITCHEN_STATIONS["BREAKFAST"],
        },


        {
            "name": "Aloo Tama",
            "price": 120,
            "description": "Potato and bamboo shoot curry",
            "priority": "2",
            "est_time": 15,
            "station": KITCHEN_STATIONS["MAIN"],
        },


        {
            "name": "Chiura with Curd",
            "price": 100,
            "description": "Beaten rice served with fresh curd",
            "priority": "1",
            "est_time": 5,
            "station": KITCHEN_STATIONS["BREAKFAST"],
        },

    ],



    # ---------------------------------
    # Snacks Items
    # ---------------------------------

    "Snacks": [

        {
            "name": "Chicken Momo",
            "price": 180,
            "description": "Steamed dumplings",
            "priority": "3",
            "est_time": 20,
            "station": KITCHEN_STATIONS["MOMO"],
        },


        {
            "name": "Buff Momo",
            "price": 170,
            "description": "Traditional buffalo dumplings",
            "priority": "3",
            "est_time": 20,
            "station": KITCHEN_STATIONS["MOMO"],
        },


        {
            "name": "Veg Momo",
            "price": 160,
            "description": "Vegetable dumplings",
            "priority": "3",
            "est_time": 15,
            "station": KITCHEN_STATIONS["MOMO"],
        },


        {
            "name": "Chicken Chowmein",
            "price": 190,
            "description": "Stir-fried noodles",
            "priority": "3",
            "est_time": 15,
            "station": KITCHEN_STATIONS["NOODLES"],
        },


        {
            "name": "Buff Chowmein",
            "price": 180,
            "description": "Noodles with buffalo meat",
            "priority": "3",
            "est_time": 15,
            "station": KITCHEN_STATIONS["NOODLES"],
        },


        {
            "name": "Samosa",
            "price": 40,
            "description": "Crispy potato pastry",
            "priority": "2",
            "est_time": 10,
            "station": KITCHEN_STATIONS["SNACK"],
        },


        {
            "name": "Pakoda",
            "price": 90,
            "description": "Mixed vegetable fritters",
            "priority": "2",
            "est_time": 10,
            "station": KITCHEN_STATIONS["SNACK"],
        },

    ],




    # ---------------------------------
    # Lunch and Dinner Items
    # ---------------------------------

    "Lunch & Dinner": [

        {
            "name": "Veg Dal Bhat Tarkari",
            "price": 250,
            "description": "Rice, lentils, vegetables, pickle",
            "priority": "2",
            "est_time": 20,
            "station": KITCHEN_STATIONS["MAIN"],
        },


        {
            "name": "Chicken Dal Bhat",
            "price": 350,
            "description": "Dal Bhat with chicken curry",
            "priority": "2",
            "est_time": 25,
            "station": KITCHEN_STATIONS["MAIN"],
        },


        {
            "name": "Buff Dal Bhat",
            "price": 330,
            "description": "Dal Bhat with buffalo curry",
            "priority": "2",
            "est_time": 25,
            "station": KITCHEN_STATIONS["MAIN"],
        },


        {
            "name": "Mutton Khana Set",
            "price": 480,
            "description": "Rice with mutton curry",
            "priority": "2",
            "est_time": 35,
            "station": KITCHEN_STATIONS["MAIN"],
        },


        {
            "name": "Fish Curry Set",
            "price": 420,
            "description": "Rice with fish curry",
            "priority": "2",
            "est_time": 30,
            "station": KITCHEN_STATIONS["CURRY"],
        },


        {
            "name": "Thakali Khana Set",
            "price": 450,
            "description": "Traditional Thakali meal",
            "priority": "2",
            "est_time": 30,
            "station": KITCHEN_STATIONS["MAIN"],
        },

    ],



    # ---------------------------------
    # Curry Items
    # ---------------------------------

    "Curries": [

        {
            "name": "Chicken Curry",
            "price": 280,
            "description": "Spicy Nepali chicken curry",
            "priority": "3",
            "est_time": 25,
            "station": KITCHEN_STATIONS["CURRY"],
        },


        {
            "name": "Buff Curry",
            "price": 260,
            "description": "Buffalo meat curry",
            "priority": "3",
            "est_time": 30,
            "station": KITCHEN_STATIONS["CURRY"],
        },


        {
            "name": "Mutton Curry",
            "price": 420,
            "description": "Traditional mutton curry",
            "priority": "3",
            "est_time": 40,
            "station": KITCHEN_STATIONS["CURRY"],
        },


        {
            "name": "Paneer Curry",
            "price": 240,
            "description": "Cottage cheese curry",
            "priority": "2",
            "est_time": 20,
            "station": KITCHEN_STATIONS["CURRY"],
        },

    ],



    # ---------------------------------
    # Drinks Items
    # ---------------------------------

    "Drinks": [

        {
            "name": "Milk Tea",
            "price": 40,
            "description": "Hot Nepali chiya",
            "priority": "1",
            "est_time": 5,
            "station": KITCHEN_STATIONS["DRINK"],
        },


        {
            "name": "Black Tea",
            "price": 30,
            "description": "Fresh black tea",
            "priority": "1",
            "est_time": 5,
            "station": KITCHEN_STATIONS["DRINK"],
        },


        {
            "name": "Coffee",
            "price": 80,
            "description": "Fresh brewed coffee",
            "priority": "1",
            "est_time": 7,
            "station": KITCHEN_STATIONS["DRINK"],
        },


        {
            "name": "Lassi",
            "price": 120,
            "description": "Sweet yogurt drink",
            "priority": "1",
            "est_time": 5,
            "station": KITCHEN_STATIONS["DRINK"],
        },


        {
            "name": "Lemon Soda",
            "price": 90,
            "description": "Refreshing soda with lemon",
            "priority": "1",
            "est_time": 5,
            "station": KITCHEN_STATIONS["DRINK"],
        },


        {
            "name": "Mineral Water",
            "price": 30,
            "description": "500ml bottled water",
            "priority": "1",
            "est_time": 1,
            "station": KITCHEN_STATIONS["DRINK"],
        },


        {
            "name": "Coca-Cola",
            "price": 70,
            "description": "Soft drink",
            "priority": "1",
            "est_time": 1,
            "station": KITCHEN_STATIONS["DRINK"],
        },


        {
            "name": "Sprite",
            "price": 70,
            "description": "Soft drink",
            "priority": "1",
            "est_time": 1,
            "station": KITCHEN_STATIONS["DRINK"],
        },

    ],



    # ---------------------------------
    # Dessert Items
    # ---------------------------------

    "Desserts": [

        {
            "name": "Juju Dhau",
            "price": 150,
            "description": "King curd from Bhaktapur",
            "priority": "1",
            "est_time": 5,
            "station": KITCHEN_STATIONS["DESSERT"],
        },


        {
            "name": "Kheer",
            "price": 120,
            "description": "Rice pudding",
            "priority": "1",
            "est_time": 10,
            "station": KITCHEN_STATIONS["DESSERT"],
        },


        {
            "name": "Gulab Jamun",
            "price": 100,
            "description": "Sweet milk dumplings",
            "priority": "1",
            "est_time": 5,
            "station": KITCHEN_STATIONS["DESSERT"],
        },

    ],

}