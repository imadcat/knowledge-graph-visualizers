import requests

def test_query(qid):
    query = f"""
    SELECT ?c ?cLabel ?cDesc WHERE {{
      ?c wdt:P279 wd:{qid} .
      OPTIONAL {{ ?c schema:description ?cDesc . FILTER(LANG(?cDesc) = "en") }}
      SERVICE wikibase:label {{ bd:serviceParam wikibase:language "en". }}
    }} LIMIT 100
    """
    url = 'https://query.wikidata.org/sparql'
    headers = {'User-Agent': 'MyBot/1.0 (tom@example.com)'}
    r = requests.get(url, params={'query': query, 'format': 'json'}, headers=headers)
    data = r.json()
    bindings = data['results']['bindings']
    for b in bindings:
        label = b.get('cLabel', {}).get('value', 'No Label')
        label = label.encode('ascii', 'ignore').decode('ascii')
        print(f"{b['c']['value'].split('/')[-1]}: {label}")
    print(f"Total subclasses: {len(bindings)}")

test_query('Q8195619')
