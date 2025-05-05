import folium
import webbrowser


# List of key Seinfeld locations with detailed popups
seinfeld_locations = [
  {
        "name": "Jerry's Apartment",
        "lat": 40.78381623917314,
        "lon": -73.97536769988461,
        "address": "129 W 81st St, Apartment 5A, New York, NY",
        #"image": "http://localhost:8000/images/JerryApt.jpeg",
        "image": "images/JerryApt.jpeg",
        "blurb": "This is the real-life building used for exterior shots of Jerry’s apartment. In the show, it’s supposedly on the Upper West Side."
    },

    {
        "name": "Kramer's Apartment",
        "lat": 40.78413516391548,
        "lon": -73.97517536649656,
        "address": "129 W 81st St, Apartment 5B, New York, NY",
        #"image": "http://localhost:8000/images/KramerApt.jpeg",
        "image": "images/KramerApt.jpeg",
        "blurb": "Home to the reverse peephole, the garbage disposal shower, and the final taping location of 'The Merv Griffin Show', directly across the hall from Jerry."
    },

        {
        "name": "Kenny Rodgers' Roasters",
        "lat": 40.78353455817639,
        "lon":-73.97556560187662,
        "address": "120 W 81st St (estimated), New York, NY",
        #"image": "http://localhost:8000/images/KennyRogersChicken.jpeg",
        "image": "images/KennyRogersChicken.jpeg",
        "blurb": "A Kenny Rogers' Roasters Chicken restaurant opens across the street from Jerry and Kramer's building. Complete with a gigantic red neon chicken atop the roof which beams directly into Kramer's apartment."
    },
    
    {
        "name": "Monk's aka 'The Coffee Shop' ",
        "lat": 40.805449,
        "lon": -73.965441,
        "address": "2880 Broadway, New York, NY",
        #"image": "http://localhost:8000/images/CoffeeShop.jpeg",
        "image": "images/CoffeeShop.jpeg",
        "blurb": "The iconic diner where Jerry, George, Elaine, and Kramer frequently meet. Known in real life as Tom’s Restaurant."
    },
        {
        "name": "Hunan 5th Avenue",
        "lat": 40.747576373863765,
        "lon": -73.98500770399465,
        "address": "323 5th Ave, New York, NY",
        #"image": "http://localhost:8000/images/ChineseRestaurant.jpeg",
        "image": "images/ChineseRestaurant.jpeg",
        "blurb": "The infamous spot where the gang waited endlessly for a table."
    },
        {
        "name": "The Improv Comedy Club",
        "lat": 40.7594,
        "lon": -73.9914,
        "address": "358 W 44th St, New York, NY",
        #"image": "http://localhost:8000/images/Improv.jpeg",
        "image": "images/Improv.jpeg",
        "blurb": "The Improv Comedy Club serves as the spot where Jerry shares his observations about nothing with the world. Also famous for being the location where nearly every Seinfeld episode begins."
    },
    {
        "name": "Costanza Household",
        "lat": 40.7729219,
        "lon": -73.9108724,
        "address": "22-37 37th St, Queens, NY",
        #"image": "http://localhost:8000/images/ConstanzaHouse.jpeg",
        "image": "images/ConstanzaHouse.jpeg",
        "blurb": "The Queens-based home of George’s eccentric parents, Frank and Estelle. Site of many legendary shouting matches."
    },
    {
        "name": "Soup Nazi's Restaurant",
        "lat": 40.761581,
        "lon": -73.981740,
        "address": "259 W 55th St, New York, NY",
        #"image": "http://localhost:8000/images/SoupNazi.jpeg",
        "image": "images/SoupNazi.jpeg",
        "blurb": "Inspired by a real soup stand, this is where the infamous Soup Nazi yelled 'No soup for you!'"
    },
    {
        "name": "George's Office (Yankee Stadium)",
        "lat": 40.829643,
        "lon": -73.926175,
        "address": "1 E 161st St, Bronx, NY",
        #"image": "http://localhost:8000/images/GeorgeWork.jpeg",
        "image": "images/GeorgeWork.jpeg",
        "blurb": "George worked for the New York Yankees under George Steinbrenner. Hilariously unqualified for most of his duties."
    },
]

# Create the NYC map
nyc_map = folium.Map(location=[40.7831, -73.9712], zoom_start=12)

# Add custom markers
for loc in seinfeld_locations:
    html = f"""
    <div style="background-color: rgba(255, 255, 255, 0.3);, font-family: arial;">
    <h4>{loc['name']}</h4>
    <p><strong>Address:</strong> {loc['address']}</p>
    <img src="{loc['image']}" width="200"><br>
    <p>{loc['blurb']}</p>
    </div>
    """
    iframe = folium.IFrame(html=html, width=250, height=300)
    popup = folium.Popup(iframe, max_width=300)
    folium.Marker(
        location=[loc["lat"], loc["lon"]],
        popup=popup,
        icon=folium.Icon(color="blue", icon="info-sign")
    ).add_to(nyc_map)

# Save and open the map
map_file = "street_seins.html"
nyc_map.save(map_file)
webbrowser.open(map_file)
