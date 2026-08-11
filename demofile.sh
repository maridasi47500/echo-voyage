
mkdir templates 
python3 scaffold.py country name
python3 scaffold.py user username email password phone country_id:references
python3 scaffold.py city name country_id:references
python3 scaffold.py carnetdevoyage title description user_id:references
python3 scaffold.py destination carnetdevoyage_id:references city_id:references
python3 scaffold.py son zik:file destination_id:references description user_id:references
python3 scaffold.py photo user_id:references pic:file destination_id:references
python3 scaffold.py street name city_id:references
python3 scaffold.py track composer_artist title street_id:references
python3 scaffold.py magasin street_id:references name
python3 scaffold.py article magasin_id:references name country_id:references pic:file
python3 scaffold.py ruby_gps lat lon street_id:references mood heure souvenir
python3 scaffold.py creation destination_id:references user_id:references title pic:file description
python3 scaffold.py limite_map lat1 lat2 lon1 lon2 city_id:references user_id:references
