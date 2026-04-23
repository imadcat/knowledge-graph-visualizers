# Wikidata 3D Explorer

An interactive, live-updating 3D visualization tool for exploring the vast [Wikidata](https://www.wikidata.org) knowledge graph. Built with vanilla JavaScript, HTML/CSS, and powered by [3d-force-graph](https://github.com/vasturiano/3d-force-graph), this application lets you literally fly through the semantic web.
![alt text](image.png)

## 🌟 Features

- **Live SPARQL Integration:** There is no static database. Every time you click a node or run a search, the app constructs and executes live SPARQL queries against `query.wikidata.org` to fetch ontology trees and statements on the fly.
- **Infinite Traversal:** Start from seed concepts like "Human" or "Physical Object" and drill down infinitely into subclasses, instances, and related properties.
- **Smart Focus Mode:** Clicking any node engages "Focus Mode". The selected node is pinned in 3D space (becoming immune to physics explosions), and the camera smoothly swoops in to lock onto it while its ontology tree unfurls around it.
- **Rich Knowledge Panel:** Displays real-time metadata about the focused entity.
  - Dynamically populates parent classes (Inherits From) and sub-classes (Extended By).
  - Fetches up to 50 outgoing Wikidata statements (e.g., *instance of*, *discoverer*, *country*).
  - **Multimedia Aware:** Automatically detects if a property is an image (`.jpg`, `.png`), video (`.mp4`), or audio (`.mp3`) file and renders it directly inside the Knowledge Panel!
- **Graph Injection:** See an interesting statement or property value? Click it in the Knowledge Panel to instantly inject it into the 3D universe as a new node, complete with glowing relational links to its parent.
- **Live Autocomplete Search:** A built-in search bar queries the Wikidata API for entities. Click a result to instantly teleport it into your universe and fly the camera to it.
- **Dynamic Resource Management:** Includes a user-adjustable slider to throttle or expand the number of subclasses fetched (up to 500 per node). Features smart "exhaustion caching" to ensure the network is never queried redundantly once an entity's tree is fully loaded.

## 🚀 How to Run

Because this app uses modern browser `fetch` APIs to query external servers, it must be run through a local web server (opening the `.html` file directly from your filesystem via `file://` may trigger CORS or security blocks in some browsers).

1. Clone the repository.
2. Serve the directory using any basic HTTP server. For example, if you have Python installed:
   ```bash
   python -m http.server 8090
   ```
3. Open your browser and navigate to:
   ```
   http://localhost:8090/wikidata.html
   ```

## 🛠️ Architecture

- `wikidata.html`: The monolithic core containing the UI, the 3D rendering engine setup, and the SPARQL query engine.
- **Dependencies:** 
  - [3d-force-graph](https://github.com/vasturiano/3d-force-graph) via unpkg for hardware-accelerated WebGL graph rendering.

## 🤖 Robot Policy & Rate Limits

This application queries the public Wikidata SPARQL endpoint. The `fetch` calls are explicitly configured with an `Api-User-Agent` header to comply with Wikimedia's strict robot and scraping policies. 

If you plan on modifying the tool to scrape massive amounts of data concurrently, please be aware that Wikidata may temporarily IP block you (HTTP 403/429) if you exceed their fair-use thresholds.

## 📝 Other Files

- `schema.org.html`: An alternative visualizer template designed for exploring Schema.org vocabularies.
  
  <br>
  <img src="schema_demo.webp" width="600" alt="Schema Explorer Demo">

- `test_chain.py`: A Python utility script used for headless testing of SPARQL subclass crawling logic and debugging Wikidata hierarchy loops.
