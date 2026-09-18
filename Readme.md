# TechShop - IAP1 Assignment: Shopping Cart

Descriere
Aplicatie web de tip e-commerce construita cu Flask si Bootstrap 5. Utilizatorul poate naviga printre produse, le poate adauga intr-un cos de cumparaturi si poate plasa o comanda prin completarea unui formular de checkout.
Tehnologii folosite

Flask - framework web Python, ales pentru simplitate si integrarea nativa cu Jinja2
Jinja2 - template engine integrat in Flask, folosit pentru a evita duplicarea codului HTML
Bootstrap 5 (via CDN) - framework CSS pentru design responsive, fara dependinte locale
Python stdlib - json, os, datetime pentru salvarea comenzilor, fara librarii extra

Rulare locala
bashpython -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python server.py
Acceseaza: http://localhost:5000
Rulare cu Docker
bashdocker build -t iap1-tema ./
docker run -p 5000:5000 -it iap1-tema
Functionalitati implementate
Cerinte de baza

Pagina principala cu produse randate dinamic din products.py folosind Jinja2
Imagini thumbnail pentru fiecare produs
Cos de cumparaturi persistent prin sesiunea Flask (session)
Adaugare produs: GET /cart/add-item?id=<id>
Stergere produs: GET /cart/remove-item?id=<id>
Pagina cos: GET /cart cu tabel produse, cantitati, subtotaluri si total
Badge in navbar cu numarul de produse din cos
Checkout: GET /checkout (formular) si POST /checkout (procesare)
Campuri checkout: full_name, email, phone, address, payment_method
Datele comenzii sunt printate in consola Flask si salvate ca JSON in submitted-orders/
Pagina de contact cu detalii firma
Toate paginile mostenesc base.html (navbar comun, link activ evidentiat)

Bonusuri

Search - cautare dupa nume si descriere produs
Filtrare pe categorie - dropdown cu categoriile disponibile
Sortare - dupa pret crescator/descrescator sau nume alfabetic
Pagina individuala per produs (/product/<id>) cu sectiune "Produse similare"
Butoane +/- pentru modificarea cantitatii direct din pagina cosului
Formular contact functional - mesajele sunt salvate in submitted-messages/ ca JSON
Flash messages - confirmare vizuala dupa trimiterea mesajului de contact
Breadcrumb pe pagina produsului individual

Decizii de design

Produsele sunt definite intr-un fisier separat (products.py) pentru a pastra server.py curat
Cosul este stocat in session Flask ca dictionar {product_id: cantitate}, persistent la refresh
Comenzile sunt salvate cu numele clientului in filename pentru identificare usoara
Pozele sunt URL-uri externe (Unsplash) pentru a mentine arhiva sub limita de 20MB