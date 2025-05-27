import folium
import webbrowser

# Create the NYC map
nyc_map = folium.Map(location=[40.7831, -73.9712], zoom_start=12)

seinfeld_homes = [{
        "name": "Jerry's Apartment",
        "lat": 40.78381623917314,
        "lon": -73.97536769988461,
        "address": "129 W 81st St, Apartment 5A, New York, NY",
        #"image": "http://localhost:8000/images/JerryApt.jpeg",
        "image": "https://alexandersuglio.github.io/StreetSeins/images/Homes/JerryApt.jpeg",
        "blurb": "This is the real-life building used for exterior shots of Jerry’s apartment. In the show, it’s supposedly on the Upper West Side."
    },
    {
        "name": "Kramer's Apartment",
        "lat": 40.78413516391548,
        "lon": -73.97517536649656,
        "address": "129 W 81st St, Apartment 5B, New York, NY",
        #"image": "http://localhost:8000/images/KramerApt.jpeg",
        "image": "https://alexandersuglio.github.io/StreetSeins/images/Homes/KramerApt.jpeg",
        "blurb": "Home to the reverse peephole, the garbage disposal shower, and the final taping location of 'The Merv Griffin Show', directly across the hall from Jerry."
    },{
        "name": "Costanza Household",
        "lat": 40.7729219,
        "lon": -73.9108724,
        "address": "22-37 37th St, Queens, NY",
        #"image": "http://localhost:8000/images/ConstanzaHouse.jpeg",
        "image": "https://alexandersuglio.github.io/StreetSeins/images/Homes/ConstanzaHouse.jpeg",
        "blurb": "The Queens-based home of George’s eccentric parents, Frank and Estelle. Site of many legendary shouting matches."
    }]

seinfeld_food = [{
        "name": "Kenny Rodgers' Roasters",
        "lat": 40.78353455817639,
        "lon":-73.97556560187662,
        "address": "120 W 81st St (estimated), New York, NY",
        #"image": "http://localhost:8000/images/KennyRogersChicken.jpeg",
        "image": "https://alexandersuglio.github.io/StreetSeins/images/Food/KennyRogersChicken.jpeg",
        "blurb": "A Kenny Rogers' Roasters Chicken restaurant opens across the street from Jerry and Kramer's building. Complete with a gigantic red neon chicken atop the roof which beams directly into Kramer's apartment."
    },
    {
        "name": "Monk's aka 'The Coffee Shop' ",
        "lat": 40.805449,
        "lon": -73.965441,
        "address": "2880 Broadway, New York, NY",
        #"image": "http://localhost:8000/images/CoffeeShop.jpeg",
        "image": "https://alexandersuglio.github.io/StreetSeins/images/Food/TheCoffeeShop.jpeg",
        "blurb": "The iconic diner where Jerry, George, Elaine, and Kramer frequently meet. Known in real life as Tom’s Restaurant."
    },
    {
        "name": "Hunan 5th Avenue",
        "lat": 40.747576373863765,
        "lon": -73.98500770399465,
        "address": "323 5th Ave, New York, NY",
        #"image": "http://localhost:8000/images/ChineseRestaurant.jpeg",
        "image": "https://alexandersuglio.github.io/StreetSeins/images/Food/ChineseRestaurant.jpeg",
        "blurb": "The infamous spot where the gang waited endlessly for a table."
    },  {
        "name": "Paisano's Pizza",
        "lat": 40.73068669250866,
        "lon": -74.00190646908185,
        "address": "7 Carmine St, New York, NY",
        #"image": "http://localhost:8000/images/PaisanosPizza.jpeg",
        "image": "https://alexandersuglio.github.io/StreetSeins/images/Food/PaisanosPizza.jpeg",
        "blurb": "Pizzeria where George bought himself and Mr. Steinbrenner calzones until being banned from the store after being caught emptying the tip jar."
    },  {
        "name": "Soup Nazi's Restaurant",
        "lat": 40.761581,
        "lon": -73.981740,
        "address": "259 W 55th St, New York, NY",
        #"image": "http://localhost:8000/images/SoupNazi.jpeg",
        "image": "https://alexandersuglio.github.io/StreetSeins/images/Food/SoupNazi.jpeg",
        "blurb": "Inspired by a real soup stand, this is where the infamous Soup Nazi yelled 'No soup for you!'"
    }]

seinfeld_work = [{
        "name": "The Improv Comedy Club",
        "lat": 40.7594,
        "lon": -73.9914,
        "address": "358 W 44th St, New York, NY",
        #"image": "http://localhost:8000/images/Improv.jpeg",
        "image": "https://alexandersuglio.github.io/StreetSeins/images/Work/JerryWorkImprov.jpeg",
        "blurb": "The Improv Comedy Club serves as the spot where Jerry shares his observations about nothing with the world. Also famous for being the location where nearly every Seinfeld episode begins."
    }, {
        "name": "George's Office (Yankee Stadium)",
        "lat": 40.829643,
        "lon": -73.926175,
        "address": "1 E 161st St, Bronx, NY",
        #"image": "http://localhost:8000/images/GeorgeWork.jpeg",
        "image": "https://alexandersuglio.github.io/StreetSeins/images/Work/GeorgeWorkYankees.jpeg",
        "blurb": "George worked for the New York Yankees under George Steinbrenner. Hilariously unqualified for most of his duties."
    }]

seinfeld_myth = [{
        "name": "George's House in the Hamptons",
        "lat": 41.0712212003619,
        "lon": -71.8554901136782,
        "address": "Easternmost Point of Long Island",
        #"image": "http://localhost:8000/images/HamptonsGeorge.jpeg",
        "image": "https://alexandersuglio.github.io/StreetSeins/images/Meta%20Mythological/HamptonsGeorge.jpeg",
        "blurb": "Location of George's fictional house, complete with a master bedroom, two solariums, and enough room for Snoopy and Prickly Pete"
    }, {
        "name": "Nexus of the Universe",
        "lat": 40.72339920606251,
        "lon": -73.98840737449171,
        "address": "East 1st Street &, 1st Ave, New York, NY",
        #"image": "http://localhost:8000/images/NexusOfUniverse.jpeg",
        "image": "https://alexandersuglio.github.io/StreetSeins/images/Meta%20Mythological/NexusOfTheUniverse.jpeg",
        "blurb": "Located deep downtown, spot where the same street intersects with itself."
    }]

seinfeld_yada = []




# Add custom markers
for loc in seinfeld_homes:
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
        icon=folium.Icon(color="blue", icon="home")
    ).add_to(nyc_map)


# Add custom markers
for loc in seinfeld_food:
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
        icon=folium.Icon(color="blue", icon="cutlery")
    ).add_to(nyc_map)

# Add custom markers
for loc in seinfeld_work:
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
        icon=folium.Icon(color="blue", icon="briefcase")
    ).add_to(nyc_map)

# Add custom markers
for loc in seinfeld_myth:
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
        icon=folium.Icon(color="blue", icon='question', prefix='fa')
    ).add_to(nyc_map)


# List of key Seinfeld locations with detailed popups
# seinfeld_locations = [
#     {
#         "name": "Jerry's Apartment",
#         "lat": 40.78381623917314,
#         "lon": -73.97536769988461,
#         "address": "129 W 81st St, Apartment 5A, New York, NY",
#         #"image": "http://localhost:8000/images/JerryApt.jpeg",
#         "image": "https://alexandersuglio.github.io/StreetSeins/images/JerryApt.jpeg",
#         "blurb": "This is the real-life building used for exterior shots of Jerry’s apartment. In the show, it’s supposedly on the Upper West Side."
#     },
#     {
#         "name": "Kramer's Apartment",
#         "lat": 40.78413516391548,
#         "lon": -73.97517536649656,
#         "address": "129 W 81st St, Apartment 5B, New York, NY",
#         #"image": "http://localhost:8000/images/KramerApt.jpeg",
#         "image": "https://alexandersuglio.github.io/StreetSeins/images/KramerApt.jpeg",
#         "blurb": "Home to the reverse peephole, the garbage disposal shower, and the final taping location of 'The Merv Griffin Show', directly across the hall from Jerry."
#     },
#     {
#         "name": "Kenny Rodgers' Roasters",
#         "lat": 40.78353455817639,
#         "lon":-73.97556560187662,
#         "address": "120 W 81st St (estimated), New York, NY",
#         #"image": "http://localhost:8000/images/KennyRogersChicken.jpeg",
#         "image": "https://alexandersuglio.github.io/StreetSeins/images/KennyRogersChicken.jpeg",
#         "blurb": "A Kenny Rogers' Roasters Chicken restaurant opens across the street from Jerry and Kramer's building. Complete with a gigantic red neon chicken atop the roof which beams directly into Kramer's apartment."
#     },
#     {
#         "name": "Monk's aka 'The Coffee Shop' ",
#         "lat": 40.805449,
#         "lon": -73.965441,
#         "address": "2880 Broadway, New York, NY",
#         #"image": "http://localhost:8000/images/CoffeeShop.jpeg",
#         "image": "https://alexandersuglio.github.io/StreetSeins/images/CoffeeShop.jpeg",
#         "blurb": "The iconic diner where Jerry, George, Elaine, and Kramer frequently meet. Known in real life as Tom’s Restaurant."
#     },
#     {
#         "name": "Hunan 5th Avenue",
#         "lat": 40.747576373863765,
#         "lon": -73.98500770399465,
#         "address": "323 5th Ave, New York, NY",
#         #"image": "http://localhost:8000/images/ChineseRestaurant.jpeg",
#         "image": "https://alexandersuglio.github.io/StreetSeins/images/ChineseRestaurant.jpeg",
#         "blurb": "The infamous spot where the gang waited endlessly for a table."
#     },
#     {
#         "name": "The Improv Comedy Club",
#         "lat": 40.7594,
#         "lon": -73.9914,
#         "address": "358 W 44th St, New York, NY",
#         #"image": "http://localhost:8000/images/Improv.jpeg",
#         "image": "https://alexandersuglio.github.io/StreetSeins/images/Improv.jpeg",
#         "blurb": "The Improv Comedy Club serves as the spot where Jerry shares his observations about nothing with the world. Also famous for being the location where nearly every Seinfeld episode begins."
#     },
#     {
#         "name": "Costanza Household",
#         "lat": 40.7729219,
#         "lon": -73.9108724,
#         "address": "22-37 37th St, Queens, NY",
#         #"image": "http://localhost:8000/images/ConstanzaHouse.jpeg",
#         "image": "https://alexandersuglio.github.io/StreetSeins/images/ConstanzaHouse.jpeg",
#         "blurb": "The Queens-based home of George’s eccentric parents, Frank and Estelle. Site of many legendary shouting matches."
#     },
#     {
#         "name": "Paisano's Pizza",
#         "lat": 40.73068669250866,
#         "lon": -74.00190646908185,
#         "address": "7 Carmine St, New York, NY",
#         #"image": "http://localhost:8000/images/PaisanosPizza.jpeg",
#         "image": "https://alexandersuglio.github.io/StreetSeins/images/PaisanosPizza.jpeg",
#         "blurb": "Pizzeria where George bought himself and Mr. Steinbrenner calzones until being banned from the store after being caught emptying the tip jar."
#     },
#     {
#         "name": "Nexus of the Universe",
#         "lat": 40.72339920606251,
#         "lon": -73.98840737449171,
#         "address": "East 1st Street &, 1st Ave, New York, NY",
#         #"image": "http://localhost:8000/images/NexusOfUniverse.jpeg",
#         "image": "https://alexandersuglio.github.io/StreetSeins/images/NexusOfUniverse.jpeg",
#         "blurb": "Located deep downtown, spot where the same street intersects with itself."
#     },
#     {
#         "name": "George's House in the Hamptons",
#         "lat": 41.0712212003619,
#         "lon": -71.8554901136782,
#         "address": "Easternmost Point of Long Island",
#         #"image": "http://localhost:8000/images/HamptonsGeorge.jpeg",
#         "image": "https://alexandersuglio.github.io/StreetSeins/images/HamptonsGeorge.jpeg",
#         "blurb": "Location of George's fictional house, complete with a master bedroom, two solariums, and enough room for Snoopy and Prickly Pete"
#     },
#     {
#         "name": "Soup Nazi's Restaurant",
#         "lat": 40.761581,
#         "lon": -73.981740,
#         "address": "259 W 55th St, New York, NY",
#         #"image": "http://localhost:8000/images/SoupNazi.jpeg",
#         "image": "https://alexandersuglio.github.io/StreetSeins/images/SoupNazi.jpeg",
#         "blurb": "Inspired by a real soup stand, this is where the infamous Soup Nazi yelled 'No soup for you!'"
#     },
#     {
#         "name": "George's Office (Yankee Stadium)",
#         "lat": 40.829643,
#         "lon": -73.926175,
#         "address": "1 E 161st St, Bronx, NY",
#         #"image": "http://localhost:8000/images/GeorgeWork.jpeg",
#         "image": "https://alexandersuglio.github.io/StreetSeins/images/GeorgeWork.jpeg",
#         "blurb": "George worked for the New York Yankees under George Steinbrenner. Hilariously unqualified for most of his duties."
#     },
# ]


# Add custom markers
# for loc in seinfeld_locations:
#     html = f"""
#     <div style="background-color: rgba(255, 255, 255, 0.3);, font-family: arial;">
#     <h4>{loc['name']}</h4>
#     <p><strong>Address:</strong> {loc['address']}</p>
#     <img src="{loc['image']}" width="200"><br>
#     <p>{loc['blurb']}</p>
#     </div>
#     """
#     iframe = folium.IFrame(html=html, width=250, height=300)
#     popup = folium.Popup(iframe, max_width=300)
#     folium.Marker(
#         location=[loc["lat"], loc["lon"]],
#         popup=popup,
#         icon=folium.Icon(color="blue", icon="info-sign")
#     ).add_to(nyc_map)

# Save and open the map
map_file = "street_seins.html"
nyc_map.save(map_file)
webbrowser.open(map_file)
