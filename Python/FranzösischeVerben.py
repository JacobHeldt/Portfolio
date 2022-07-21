from statistics import mean

class Verb:
    def __init__(self, translation, FS, SS, TS, FP, SP, TP, activation):
        self.translation = translation
        self.FS = FS
        self.SS = SS
        self.TS = TS
        self.FP = FP
        self.SP = SP
        self.TP = TP
        self.activation = activation

    def __str__(self):
        return "\nTranslation: " + self.translation +  "\nJe " + self.FS + "\nTu " + self.SS + "\nIl/elle/on " + self.TS + "\nNous " + self.FP + "\nVous " + self.SP + "\nIls/elles " + self.TP + "\n\n" 


chose = (input("If you want to conjugate a verb, type c. If you want to translate a word, type t: "))


dictionary = {
# Farben
"Farbe":"la couleur", "rot":"rouge", "gruen":"vert", "gelb":"jaune", "blau":"bleu", "schwarz":"noir", "weiß":"blanc", "lila":"violet",
"braun":"brun", "rosa":"rose", "grau":"gris", "orange":"orange", "silber":"argent", "gold":"doré", "magenta":"magenta",    

# Essen
"Fleisch":"viande", "Ente":"le canard", "Fett":"la gras", "Filet":"le filet", "Fisch":"le poisson", "Fluegel":"l'aile", "Geflügel":"la volaille", "Hackfleisch":"la viande hachée",
"Hering":"le hareng", "Huhn":"le poulet", "Kalbfleisch":"le veau", "Lachs":"le saumon", "Lamm":"l'agneau", "Meeresfrüchte":"les fruits de mer", "Pute":"la dinde",
"Rindfleisch":"le viande de bœuf", "Salami":"le salami", "Schinken":"le jambon", "Schweinefleisch":"la viande de porc", "Speck":"le lard", "Steak":"le steak",
"Thunfisch":"le thon", "Wurst":"la saucisse", "Geschirr":"la vaisselle", "Besteck":"les couverts", "Essstäbchen":"les baguettes", "Gabel":"la fourchette","Gabel":"la fourchette",
"Gabel":"la fourchette", "Glas":"le verre", "Löffel":"la cuillère", "Messer":"le couteau", "Schüssel":"le bol", "Tasse":"la tasse", "Teller":"l'assiette",
"Bier":"la bière", "Kaffee":"le café", "Limonade":"la limonade", "Milch":"le lait", "Wasser":"l'eau", "Saft":"le jus", "Tee":"le thé", "Wein":"le vin", "Getreide":"la céréale",
"Brot":"le pain", "Broetchen":"le petit pain", "Mais":"le maïs", "Mehl":"la farine", "Muesli":"muesli", "Nudeln":"les pâtes", "Reis":"le riz", "Toast":"le toast",
"Weizen":"le blé", "braten":"faire griller", "Fast Food":"la restauration rapide", "glutenfrei":"sans gluten", "vegan":"végétalien", "vegetarisch":"végétarien",
"Obst":"le fruits", "Gemüse":"les légumes", "Ananas":"l'ananas", "Apfel":"la pomme", "Banane":"la banane", "Birne":"la poire", "Brokkoli":"le brocoli", "Erbse":"le pois",
"Erdbeere":"la fraise", "Gurke":"le concombre", "Karotte":"la carotte", "Kartoffel":"la pomme de terre", "Kirsche":"la cerise", "Salat":"la laitue", "Kürbis":"la citrouille",
"Orange":"l'orange", "Paprika":"le poivron", "Pfirsich":"la pêche", "Spargel":"l'asperge", "Spinat":"les épinards", "Tomate":"la tomate", "Melone":"la pastèque",
"Weintraube":"le raisin", "Zitrone":"le citron", "Eis":"la glace", "Kaese":"le fromage", "der Käsekuchen":"le gâteau au fromage", "Keks":"le biscuit", "Kuchen":"le gâteau",
"Sahne":"la crème", "Schokolade":"le chocolat", "Waffel":"la gaufre", "Zucker":"le sucre", "Wein":"le vin",    

#Familie
"Großvater":"le grand-père", "Großmutter":"la grand-mère","Großeltern":"les grands-parents", "Mutter":"la mère", "Vater":"le père", "Eltern":"les parents", "Schwester":"la sœur", "Bruder":"le frère", "Tochter":"la fille",
"Kind":"l'enfant", "Sohn":"le fils", "Onkel":"l'oncle", "Tante":"la tante", "Neffe":"le neveu", "Nichte":"la nièce", "Cousin":"le cousin", "Cousine":"la cousine",

# Länder
"Deutschland":"Allemagne", "Frankreich":"France", "Spanien":"Espagne", "Großbritannien":"Royaume-Uni", "Italien":"Italie", "Österreich":"Autriche", "Portugal":"Portugal",
"Belgien":"Belgique", "Daenemark":"Danemark", "Finnland":"Finlande", "Schweden":"Suède", "Griechenland":"Grèce", "Ungarn":"Hongrie", "Niederlande":"Pays-Bas",
"Irland":"Irlande", "Polen":"Pologne", "USA":"États-Unis", "Japan":"Japon", "China":"Chine", "Tuerkei":"Turquie",          

# Zahlen
"0":"zéro", "1":"un", "2":"deux", "3":"trois", "4":"quatre", "5":"cinq", "6":"six", "7":"sept", "8":"huit", "9":"neuf", "10":"dix", "11":"onze", "12":"douze", "13":"treize", "14":"quatorze", "15":"quinze",
"16":"seize", "17":"dix-sept", "18":"dix-huit", "19":"dix-neuf", "20":"vingt", "21":"vingt et un", "22":"vingt-deux", "23":"vingt-trois", "24":"vingt-quatre",
"25":"vingt-cinq", "26":"vingt-six", "27":"vingt-sept", "28":"vingt-huit", "29":"vingt-neuf", "30":"trente", "31":"trente et un", "32":"trente-deux", "33":"trente-trois", 
"34":"trente-quatre", "35":"trente-cinq", "36":"trente-six", "37":"trente-sept", "38":"trente-huit", "39":"trente-neuf", "40":"quarante", "41":"quarante et un", "42":"quarante-deux", 
"43":"quarante-trois", "44":"quarante-quatre", "45":"quarante-cinq", "46":"quarante-six", "47":"quarante-sept", "48":"quarante-huit", "49":"quarante-neuf", "50":"cinquante",
"51":"cinquante et un", "52":"cinquante-deux", "53":"cinquante-trois", "54":"cinquante-quatre", "55":"cinquante-cinq", "56":"cinquante-six", "57":"cinquante-sept", "58":"cinquante-huit", 
"59":"cinquante-neuf", "60":"soixante", "61":"soixante et un", "62":"soixante-deux", "63":"soixante-trois", "64":"soixante-quatre", "65":"soixante-cinq", "66":"soixante-six", 
"67":"soixante-sept", "68":"soixante-huit", "69":"soixante-neuf", "70":"soixante-dix", "71":"soixante et onze", "72":"soixante-douze", "73":"soixante-treize", "74":"soixante-quatorze",
"75":"soixante-quinze", "76":"soixante-seize", "77":"soixante-dix-sept", "78":"soixante-dix-huit", "79":"soixante-dix-neuf", "80":"quatre-vingts", "81":"quatre-vingt-un",
"82":"quatre-vingt-deux", "83":"quatre-vingt-trois", "84":"quatre-vingt-quatre", "85":"quatre-vingt-cinq", "86":"quatre-vingt-six", "87":"quatre-vingt-sept", "88":"quatre-vingt-huit",
"89":"quatre-vingt-neuf", "90":"quatre-vingt-dix", "91":"quatre-vingt-onze","92":"quatre-vingt-douze", "93":"quatre-vingt-treize", "94":"quatre-vingt-quatorze", "95":"quatre-vingt-quinze", 
"96":"quatre-vingt-seize", "97":"quatre-vingt-dix-sept", "98":"quatre-vingt-dix-huit", "99":"quatre-vingt-dix-neuf", "100":"cent", "200":"deux cents","300":"trois cents",
"400":"quatre cents", "500":"cinq cents", "600":"six cents", "700":"sept cents", "800":"huit cents", "900":"neuf cents", "1000":"mille", "2000":"deux mille","3000":"trois mille",
"4000":"quatre mille", "5000":"cinq mille", "6000":"six mille", "7000":"sept mille", "8000":"huit mille", "9000":"neuf mille", "10000":"dix-mille", "20000":"vingt mille",
"30000":"trente mille", "40000":"quarante mille", "50000":"cinquante mille", "60000":"soixante mille", "70000":"soixante-dix mille", "80000":"quatre-vingts mille", 
"90000":"quatre-vingt-dix mille", "1000000":"un million", "1000000000":"un milliard",

# Adjektive
"reizend":"adorable", "angenehm":"agréable", "freundschaftlich":"amical", "alt":"ancien", "fleißig":"assidu", "schoen":"beau", "blond":"blond", "billig":"bon marché",
"gut":"bon", "ruhig":"calme", "charmant":"charmant", "heiss":"chaud", "teuer":"cher", "hell":"clair", "zufrieden":"content", "kurz":"court", "lecker":"délicieux",
"schwierig":"difficile", "einfach":"facile", "kalt":"froid", "nett":"gentil", "groß":"grand", "dick":"gros", "glücklich":"heureux", "wichtig":"important", 
"interessant":"intéressant", "huebsch":"joli", "haesslich":"laid", "frei":"libre", "lang":"long", "schlecht":"mauvais", "duenn":"mince", "modern":"moderne",
"neu":"nouveau", "faul":"paresseux", "klein":"petit", "hoeflich":"poli", "sauber":"propre", "rund":"rond", "weise":"sage", "schmutzig":"sale", "wild":"sauvage",
"traurig":"triste", "alt":"vieux", "wahr":"vrai", "veraergert":"fâché", "sportlich":"sportif", "langweilig":"ennuyeux", "mutig":"courageux", "ruhig":"tranquille",
"kalt":"froid", "selbstbewusst":"assuré", "freundlich":"amical", "lustig":"drôle", "schwer":"lourd", "heiss":"chaud", "ungeduldig":"impatient", "interessant":"intéressant",
"nett":"gentil", "faul":"paresseux", "allein":"solitaire", "nervoes":"nerveux", "geduldig":"patient", "schön":"belle", "traurig":"triste", "veraengstigt":"effrayé",
"klein":"petit", "schuechtern":"timide", "stark":"fort", "duenn":"mince", "muede":"fatigué", "unfreundlich":"froid", "schwach":"faible", "intelligent":"intelligent",

# Kleidung
"Kleidung":"Les vêtements", "Anorak":"l'anorak", "Anzug":"le complet", "Bademantel":"le peignoir", "Bluse":"la blouse", "Fliege":"le nœud papillon", "Handschuhe":"les gants",
"Handtasche":"le sac", "Hemd":"la chemis", "Hose":"le pantalon", "Hut":"le chapeau", "Jeans":"le jean", "Kleid":"la robe", "Krawatte":"la cravate", "Mantel":"le manteau",
"Muetze":"le bonnet", "Pullover":"le pull", "Schal":"l'écharpe", "Schuhe":"les chaussures", "Shorts":"le short", "Socken":"les chaussettes", "Stiefel":"les bottes",
"Strickjacke":"le gilet", "Strumpfhose":"le collant", "T-Shirt":"le tee-shirt", "Turnschuhe":"les baskets",

# Berufe
"Architekt":"l'architecte", "Arzt":"le médecin", "Baecker":"le boulanger", "Beamter":"le fonctionnaire", "Briefträger":"le facteur", "Buchhalter":"le comptable",
"Feuerwehrmann":"le pompier", "Fleischer":"le boucher", "Friseur":"le coiffeur", "Gaertner":"le jardinier", "Handwerker":"l'artisan", "Ingenieur":"l'ingénieur",
"Journalist":"le journaliste", "Koch":"le cuisinier", "Konditor":"le pâtissier", "Krankenschwester":"l'infirmière", "Kuenstler":"l'artiste", "Bauer Landewirt":"l'agriculteur",
"Lehrer":"le/la professeur", "Mechaniker":"le mécanicien", "Musiker":"le musicien", "Polizist":"l'agent de police", "Rechtsanwalt":"l'avocat", "Schauspieler":"l'acteur",
"Sekretärin":"la secrétaire", "Tierarzt":"le/la vétérinaire", "Verkäufer":"le vendeur", "Zahnarzt":"le dentiste",

# Ortsangaben
"Ort":"lieu","rechts":"à droite", "links":"à gauche", "gegenueber":"en face de", "weit":"loin", "nahe":"près", "geradeaus":"tout droit", "innen":"dedans", "draußen":"dehors",
"hier":"ici", "da":"là-bas", "oben":"en haut", "unten":"en bas", "vor":"devant", "hinter":"derrière",

# Jahreszeiten, Monate, Wochentage
"Jahreszeiten":"Les saisons", "Frühling":"le printemps", "Sommer":"l'été", "Herbst":"l'automne", "Winter":"l'hiver", "Januar":"janvier", "Februar":"février",
"Maerz":"mars", "April":"avril", "Mai":"mai", "Juni":"juin", "Juli":"juillet", "August":"août", "September":"septembre", "Oktober":"octobre", "November":"novembre",
"Dezember":"décembre", "Montag":"lundi", "Dienstag":"mardi", "Mittwoch":"mercredi", "Donnerstag":"jeudi", "Freitag":"vendredi", "Samstag":"samedi", "Sonntag":"dimanche",

# Im Büro
"Bewerbung":"la candidature", "Bleistift":"le crayon", "Buchführung":"la comptabilité", "Computer":"l'ordinateur", "Datei":"le fichier", "Drucker":"l'imprimante",
"Fueller":"le stylo-plume", "Kuli":"le stylo-bille", "Kugelschreiber":"le stylo-bille", "Lebenslauf":"le curriculum vitae", "Lineal":"la règle", "Locher":"la perforatrice",
"Ordner":"le classeur", "Rechnung":"la facture", "Schreibtisch":"le bureau", "Steuer":"l'impôt", "Tacker":"l'agrafeuse", "Taschenrechner":"la calculatrice de poche",

# Tiere
"Haustiere":"les animaux domestique", "Fisch":"le poisson", "Hamster":"le hamster", "Hund":"le chien", "Kaninchen":"le lapin", "Hase":"le lapin", "Katze":"le chat",
"Maus":"la souris", "Meerschweinchen":"la cochon d'Inde", "Pony":"le poney", "Ratte":"la rat", "Insekten":"les insectes", "Ameise":"la fourmi", "Biene":"l'abeille",
"Fliege":"la mouche", "Floh":"la puce", "Kakerlake":"la blatte", "Laus":"le pou", "Libelle":"la libellule", "Motte":"la mite", "Muecke":"le moustique", "Raupe":"la chenille",
"Regenwurm":"le ver de terre", "Schmetterling":"le papillon", "Schnecke":"l'escargot", "Spinne":"l'araignée", "Wespe":"la guêpe", "Zikade":"la cigale", "Meerestiere":"les animaux marin",
"Aal":"l'anguille", "Blauwal":"la baleine bleue", "Delfin":"le dauphin", "Fisch":"le poisson", "Hai":"le requin", "Koralle":"le corail", "Schildkroete":"la tortue",
"Oktopus":"le poulpe", "Qualle":"le méduse", "Sardine":"la sardine", "Seepferdchen":"l'hippocampe", "Seestern":"l'étoile de mer", "Thunfisch":"le thon", "Nutztiere":"les animaux de la ferme",
"Elefant":"l'éléphant", "Ente":"le canard", "Esel":"l'âne", "Gans":"l'oie", "Hahn":"le coq", "Huhn":"le poule", "Kamel":"le chameau", "Kuh":"la vache", "Pferd":"le cheval",
"Schaf":"le mouton", "Schwein":"le porc", "Taube":"la pigeon", "Ziege":"la chèvre", "Voegel":"les oiseaux", "Adler":"l'aigle", "Eule":"la chouette", "Falke":"le faucon",
"Kanarienvogel":"le canari", "Kraehe":"la corneille", "Papagei":"le perroquet", "Pinguin":"le manchot", "Schwan":"le cygne", "Spatz":"le moineau", "Strauß":"l'autruche",
"Wildtiere":"les animaux sauvages", "Baer":"l'ours", "Eichhörnchen":"l'écureuil", "Faultier":"le paresseuc", "Flusspferd":"l'hippopotame", "Fuchs":"le renard",
"Gepard":"le guépard", "Giraffe":"la girafe", "Guerteltier":"le tatou", "Hase":"le lièvre", "Jaguar":"le jaguar", "Kaenguru":"le kangourou", "Krokodil":"le crocodile",
"Leopard":"le léopard", "Loewe":"le lion", "Nashorn":"le rhinocéros", "Panther":"la panthère", "Tiger":"le tigre", "Reh":"le chevreuil", "Wildschwein":"le sanglier",
"Wolf":"le loup",

# Schulfâcher
"Englisch":"l'anglais", "Deutsch":"l'allemand", "Franzoesisch":"le français", "Mathematik":"les mathématiques", "Erdkunde":"la géographie", "Wirtschaft":"l'économie",
"Betriebswirtschaft":"la gestion", "Religion":"la religion", "Sport":"le sport", "Geschichte":"l'histoire", "Physik":"la physique", "Chemie":"la chimie", "Biologie":"la biologie",

# Freizeit
"Einkauf":"l'achat", "bezahlen":"payer", "billig":"bon marché", "einkaufen gehen":"faire les courses", "Einkaufswagen":"le caddie", "Garantie":"la garantie",
"gebraucht":"d'occasion", "Kasse":"la caisse", "Freizeit":" le temps libre", "kaufen":"acheter", "kosten":"coûter", "nehmen":"prendre", "Rabatt":"la remise",
"Sonderangebot":"l'offre spéciale", "stöbern":"fouiller", "teuer":"cher", "verkaufen":"vendre", "vorraetig":"disponible", "zurückgeben":"rendre", "essen gehen":"sortir manger",
"Beilage":"l'accompagnement", "bestellen":"commander", "empfehlen":"recommander", "Hauptgericht":"le plat principal", "Kellner":"le serveur", "Kellnerin":"la serveuse",
"koestlich":"délicieux", "Menue":"le menu", "Nachspeise":"le dessert", "Rechnung":"l'addition", "Restaurant":"le restaurant", "Service":"la service", "Serviette":"la serviette",
"Speisekarte":"la carta", "Spezialitaet":"la spécialité", "Tisch":"le table", "Trinkgeld":"le pourboire", "Vegetarier":"le végétarien", "Vegetarierin":"la végétarienne",
"Vorspeise":"l'entrée", "Kneipe":"bar", "Cafe":"café", "alkoholfrei":"sans alcool", "anstoßen":"trinquer", "Barhocker":"le tabouret de bar", "bedienen":"servir",
"betrunken":"saoul", "Bierdeckel":"le sous-bock", "bitte":"s'il vous plaît", "danke":"merci", "Erdnuss":"la cacahouète", "Fass":"pression", "herauswerfen":"jeter dehors",
"Imbiss":"l'en-cas", "koffeinfrei":"décaféiné", "koffein":"caféiné", "laut":"bruyant", "prost":"santé", "Runde":"la tournée", "Stammgast":"l'habitué", "Konzert":"concert",
"Club":"boîte de nuit", "anstehen":"faire la queue", "ausverkauft":"complet", "beschwipst":"pompette", "Buehne":"la scène", "Eintritt":"l'entrée", "Garderobe":"le vestiaire",
"Gaesteliste":"la liste des invités", "Karte":"le ticket", "nuechtern":"sobre", "Ohrstoepsel":"les bouchons d'oreilles", "Rauchverbot":"l'interdiction de fumer",
"Stempel":"le tampon", "tanzen":"danser", "Tuersteher":"le videur", "Veranstaltungsort":"le lieu", "Wasserflasche":"la bouteille d'eau", "Spiel":"le jeux",
"Brettspiel":"le jeu de société", "Dominosteine":"les dominos", "Flipper":"le flipper", "Geduldsspiel":"le casse-tête", "Joystick":"le joystick", "Karte":"la carte",
"Kreuzworträtsel":"les mots croisés", "Muenzschlitz":"la fente", "Puzzle":"le puzzle", "Regel":"la règle", "Rollenspiel":"le jeu de rôle", "Schach":"les échecs",
"Scharade":"la charade", "schummeln":"tricher", "Spaß":"le plaisir", "spielen":"jouer", "Tauziehen":"le tir à la corde", "Versteckspiel":"le cache-cache",
"Videospiel":"le jeu vidéo", "Wuerfel":"le dé",

# Sportarten
"Sportart":"discipline", "Fussball":"le football", "Volleyball":"le volley-ball", "Rugby":"le rugby", "Tennis":"tennis", "Eishockey":"hockey sur glace", 
"Basketball":"le basket-ball", "Mountainbiken":"le VTT", "Reiten":"l'équitation", "Kajakfahren":"le kayak", "Surfen":"la planche à voile", "Klettern":"l'escalade",
"Skifahren":"le ski", "Schwimmen":"la natation", "Radfahren":"le vélo", "Judo":"le judo", "Rollerskaten":"le roller", "Tanz":"la danse",

# Basics
"Hallo":"Bonjour", "Ich heiße":"Je m'appelle", "Wie heißt Du?":"Comment tu t'appelles?", "zufrieden":"content", "kennenlernen":"faire la connaissance de qqn",
"treffen":"faire la connaissance de qqn", "freuen":"être content(e)", "auch":"aussi", "woher":"d'où", "kommen":"venir", "geboren":"né(e)", "aufwachsen":"grandir",
"wie":"comment", "gut":"bien", "erkaeltet":"avoir un rhume", "danke":"merci", "eisig":"glacial(e)", "Temperatur":"température", "im Moment":"en ce moment",
"kalt":"froid(e)", "wirklich":"vraiment", "Plaene":"les projets", "Projekt":"le projet", "heute":"aujourd'hui", "spaeter":"plus tard", "Freunde":"les ami(e)s",
"grossartig":"génial(e)", "Spaß haben":"s'amuser", "begleiten":"accompagner", "Zeit":"le temps", "Abend":"le soir", "arbeiten":"travailler", "gehen":"aller",
"ankommen":"arriver", "Reise":"le voyage", "Gute Fahrt":"Bon voyage.", "hoffen":"espérer", "sehen":"voir", "demnächst":"bientôt", "Tschuess":"Salut", "Auf Wiedersehen":"Au revoir",

# Gefühle und Einstellungen
"Charakter":"le caractère", "aktiv":"actif", "egoistisch":"égoïste", "ehrlich":"honnête", "energiegeladen":"énergique", "ernst":"sérieux", "gemein":"méchant",
"gluecklos":"malchanceux", "großzuegig":"généreux", "hitziges Temperament":"le tempérament explosif", "lieb":"gentil", "nett":"sympathique", "offen":"ouvert",
"ruhig":"calme", "scheinen":"avoir l'air", "schlau":"intelligent", "selbstsicher":"sûr de soi", "suess":"mignon", "unsicher":"peu sûr de soi", "witzig":"drôle",
"Emotion":"l'émotion", "aufgebracht":"indigné", "begeistert":"enthousiaste", "darüber hinwegkommen":"laisser tomber", "deprimiert":"déprimé", "einsam":"seul",
"enttaeuscht":"éçu", "Freude":"la joie", "Gefuehl":"le sentiment", "gluecklich":"heureux", "Hass":"la haine", "Hoffnung":"l'espoir", "Laune":"l'humeur", "Liebe":"l'amour",
"Mitgefuehl":"la compassion", "sich fühlen":"se sentir", "stolz":"fier", "traurig":"triste", "wuetend":"en colère", "zufrieden":"satisfait", "Empfindung":"la sensation",
"Angst":"la peur", "Durst":"la soif", "Enttaeuschung":"la déception", "Erlebnis":"l'expérience", "Erleichterung":"le soulagement", "Gaensehaut":"la chair de poule",
"Hunger":"la faim", "irritieren":"irriter", "muede":"fatigué", "nervoes":"nerveux", "Neugier":"la curiosité", "Nostalgie":"la nostalgie", "schaudern":"frissonner",
"Schmerz":"la douleur", "Schock":"le choc", "langweilen":"s'ennuyer", "Ueberraschung":"la surprise", "Unbehagen":"la malaise", "Vergnuegen":"le paisir",
"Sexualitaet":"la sexualité", "attraktiv":"attirant", "bisexuell":"bisexuel", "erotisch":"érotique", "Geschlecht":"le sexe", "Hetero":"l'hétéro", "heterosexuell":"hétérosexuel",
"homosexuell":"homosexuel", "Jungfrau":"la vierge", "Kondom":"le préservatif", "lesbisch":"lesbienne", "Lust":"l'envie", "mit jemanden schlafen":"coucher avec quelqu'un",
"Pille":"la pilule", "Prostituierte":"la prostituée", "schwul":"homo", "sexy":"sexy", "enthalten":"s'abstenir", "verführen":"séduire", "Verhuetung":"la contraception",
"Verhalten":"le comportement", "begeistert":"enthousiaste", "boshaft":"méchant", "erroeten":"rougir", "faul":"paresseux", "freundlich":"amical", "geduldig":"patient",
"hoeflich":"poli", "lachen":"rire", "mutig":"courageux", "nachlaessig":"négligent", "schreien":"crier", "schuechtern":"timide", "sorgen":"se faire du souci",
"ungeduldig":"impatient","unhoeflich":"malpoli", "verrueckt":"fou", "vorsichtig":"prudent", "weinen":"pleurer", "zittern":"trembler", "Wahrnehmung":"la perception",
"diskriminieren":"discriminer", "Einstellung":"l'attitude", "falsch":"faux", "Fehler":"le défaut", "glauben":"croire", "gut":"bon", "Meinung":"l'opinion",
"Moral":"la morale", "negativ":"négatif", "Optimist":"l'optimiste", "Pessimist":"le pessimiste", "positiv":"positif", "rassistisch":"raciste", "Rechte":"les droits",
"richtig":"juste", "schlecht":"mauvais", "sexistisch":"sexiste", "Stereotyp":"le stéréotype", "Vorurteil":"le préjugé",
}


revdict = {v: k for k, v in dictionary.items()}



print(len(dictionary))

activation_bool_verbs = False, 
if chose == "c":
    activation_bool_verbs = True
elif chose != "c" and chose != "t":
    print("this is not an option.")

activation_bool_translation = False
if chose == "t":
    activation_bool_translation = True





while activation_bool_translation == True:
    my_word = input("Which word do you want to translate: ")
    if my_word in dictionary:
        print(dictionary[my_word])
    elif my_word in revdict:
        print(revdict[my_word])
    else:
        print("Jacob programmed this, and do you think JACOB is able to know a that difficult word in FRENCH???!!!")




etre = Verb("sein", "suis", "es", "est", "sommes", "êtes", "sont", "etre")
avoir = Verb("haben", "ai", "as", "a", "avons", "avez", "ont", "avoir")
regarder = Verb("anschauen", "regarde", "regardes", "regarde", "regardons", "regardez", "regardent", "regarder")
acheter = Verb("kaufen", "achète", "achétes", "achète", "achetons", "achetez", "achètent", "acheter")
appeler = Verb("anrufen/erfordern", "appelle", "appelles", "appelle", "appelons", "appelez", "appellent", "appeler")
#5
commencer = Verb("anfangen", "commence", "commences", "commence", "commençons", "commencez", "commencent", "commencer")
manger = Verb("essen", "mange", "manges", "mange", "mangeons", "mangez", "mangent", "manger")
preferer = Verb("bevorzugen", "préfère", "préfères", "préfère", "préférons", "préférez", "préfèrent", "preferer")
attendre = Verb("warten", "attends", "attends", "attend", "attendons", "attendez", "attendent", "attendre")
aller = Verb("gehen", "vais", "vas", "va", "allons", "allez", "vont", "aller")
#10
faire = Verb("machen", "fais", "fais", "fait", "faisons", "faites", "font", "faire")
pouvoir = Verb("können", "peux", "peux", "peut", "pouvons", "pouvez", "peuvent", "pouvoir")
prendre = Verb("nehmen", "prends", "prends", "prend", "prenons", "prenez", "prennent", "prendre")
vouloir = Verb("wollen", "veux", "veux", "veut", "voulons", "voulez", "veulent", "vouloir")
sortir = Verb("ausgehen", "sors", "sors", "sort", "sortons", "sortez", "sortent", "sortir")
#15
reagir = Verb("reagieren", "réagis", "réagis", "réagit", "réagissons", "réagissez", "réagissent", "reagir")
offrir = Verb("anbieten", "offre", "offres", "offre", "offrons", "offrez", "offrent", "offrir")
boire  = Verb("trinken", "bois", "bois", "boit", "bouvons", "bouvez", "boivent", "boire")
connaitre = Verb("wissen", "connais", "connais", "connaît", "connaissons", "connaissez", "connaissent", "connaitre")
construire = Verb("bauen", "construis", "construis", "construit", "construisons", "construisez", "construisent", "construire")
#20
parler = Verb("reden", "parle", "parles", "parle", "parlons", "parlez", "parlent", "parler")
savoir = Verb("wissen", "sais", "sais", "sait", "savons", "savez", "savent", "savoir")
venir = Verb("kommen", "viens", "viens", "vient", "venons", "venez", "viennent", "venir")
dire = Verb("sagen/erzählen", "dis", "dis", "dit", "disons", "dites", "disent", "dire")
donner = Verb("geben", "donne", "donnes", "donne", "donnons", "donnez", "donnent", "donner")
#25
penser = Verb("denken", "pense", "penses", "pense", "pensons", "pensez", "pensent", "penser")
aider = Verb("helfen", "aide", "aides", "aide", "aidons", "aidez", "aident", "aider")
aimer = Verb("mögen", "aime", "aimes", "aime", "aimons", "aimez", "aiment", "aimer")
devoir = Verb("müssen", "dois", "dois", "doit", "devons", "devez", "doivent", "devoir")
habiter = Verb("wohnen", "habite", "habites", "habite", "habitons", "habitez", "habitent", "habiter")
#30
utiliser = Verb("verwenden", "utilise", "utilises", "utilise", "utilisons", "utilisez", "utilisent", "utiliser")
essayer = Verb("probieren", "essaye", "essayes", "essaye", "essayons", "essayez", "essaient", "essayer")
arriver = Verb("ankommen", "arrive", "arrives", "arrive", "arrivons", "arrivez", "arrivent", "arriver")
envoyer = Verb("versenden", "envoie", "envoies", "envoie", "envoyons", "envoyez", "envoient", "envoyer")
dormir = Verb("schlafen", "dors", "dors", "dort", "dormons", "dormez", "dorment", "dormir")
#35
finir = Verb("enden", "finis", "finis", "finit", "finissons", "finissez", "finissent", "finir")
courir = Verb("laufen", "cours", "cours", "court", "courons", "courez", "courent", "courir")
croire = Verb("glauben", "crois", "crois", "croit", "croyons", "croyez", "croient", "croire")
écrire = Verb("schreiben", "écris", "écris", "écrit", "écrivons", "écrivez", "écrivent", "écrire")
lire = Verb("lesen", "lis", "lis", "lit", "lisons", "lisez", "lisent", "lire")
#40
mettre = Verb("stellen", "mets", "mets", "met", "mettons", "mettez", "mettent", "mettre")
plaire = Verb("gefallen", "plais", "plais", "plaît", "plaisons", "plaisez", "plaisent", "plaire")
recevoir = Verb("empfangen", "reçois", "reçois", "reçoit", "recevons", "recevez", "reçoivent", "recevoir")
rire = Verb("lachen", "ris", "ris", "rit", "rions", "riez", "rient", "rire")
vivre = Verb("leben", "vis", "vis", "vit", "vivons", "vivez", "vivent", "vivre")
#45
voir = Verb("sehen", "vois", "vois", "voit", "voyons", "voyez", "voient", "voir")
ouvrir = Verb("öffnen", "ouvre", "ouvres", "ouvre", "ouvrons", "ouvrez", "ouvrent", "ouvrir")
promettre = Verb("versprechen", "promets", "promets", "promet", "promettons", "promettez", "promettent", "promettre")
demander = Verb("fragen", "demande", "demandes", "demande", "demandons", "demandez", "demandent", "demander")
trouver = Verb("finden", "trouve", "trouves", "trouves", "trouvons", "trouvez", "trouvent", "trouver")
#50
comprendre = Verb("verstehen", "comprends", "comprends", "comprend", "comprenons", "comprenez", "comprennent", "comprendre")
tenir = Verb("halten", "tiens", "tiens", "tient", "tenons", "tenez", "tiennent", "tenir")
porter = Verb("tragen", "porte", "portes", "porte", "portons", "portez", "portent", "porter")
montrer = Verb("zeigen", "montre", "montres", "montre", "montrons", "montrez", "montrent", "montrer")
suivre = Verb ("folgen", "suis", "suis", "suit", "suivons", "suivez", "suivent", "suivre")
#55
compter = Verb("zählen", "compte", "comptes", "compte", "comptons", "comptez", "comptent", "compter")
entendre = Verb("hören", "entends", "entends", "entend", "entendons", "entendez", "entendent", "entendre")
permettre = Verb("erlauben", "permets", "permets", "permet", "permettons", "permettez", "permettent", "permettre")
partir = Verb("verlassen", "pars", "pars", "part", "partons", "partez", "partent", "partir")
decider = Verb("entscheiden", "décide", "décides", "décide", "décidons", "décidez", "décident", "decider")
#60



while activation_bool_verbs == True:
    v = input("Enter your verb: ")

    if v == "etre":
        print(etre)
    elif v == "sein":
        print("\nêtre")
        print(etre)
    
    elif v == "avoir":
        print(avoir)
    elif v == "haben":
        print("\navoir")
        print(avoir)
    
    elif v == "regarder":
        print(regarder)
    elif v == "anschauen" or v== "angucken" or v== "ansehen":
        print("\nregarder")
        print(regarder)
       
    elif v == "acheter":
        print(acheter)
    elif v == "kaufen":
        print("\nacheter")
        print(acheter)
    
    elif v == ("appeler"):
        print(appeler)
    elif v == "anrufen" or v== "rufen" or v== "erfordern":
        print("\nappeler")
        print(appeler)

    
    #5
    elif v == "commencer":
        print(commencer)
    elif v == "anfangen" or v== "beginnen":
        print("\ncommencer")
        print(commencer)

    elif v == "manger":
        print(manger)
    elif v == "essen":
        print("\nmanger")
        print(manger)
    
    elif v == "preferer":
        print(preferer)
    elif v == "bevorzugen":
        print("\npreferer")
        print(preferer)

    elif v == "attendre":
        print(attendre)
    elif v == "warten":
        print("\nattendre")
        print(attendre)

    elif v == "aller":
        print(aller)
    elif v == "gehen" or v == "fahren":
        print("\naller")
        print(aller)
    
    
    #10
    elif v == "faire":
        print(faire)
    elif v == "machen":
        print("\nfaire")
        print(faire)

    elif v == "pouvoir":
        print(pouvoir)
    elif v == "können":
        print("\npouvoir")
        print(pouvoir)
    
    elif v == "prendre":
        print(prendre)
    elif v == "nehmen":
        print("\nprendre")
        print(prendre)

    elif v == "vouloir":
        print(vouloir)
    elif v == "wollen":
        print("\nvouloir")
        print(vouloir)

    elif v == "sortir":
        print(sortir)
    elif v == "ausgehen":
        print("\nsortir")
        print(sortir)        
    #15
    elif v == "reagir":
        print(reagir)
    elif v == "reagieren":
        print("\nreagir")
        print(reagir)
    
    elif v == "offrir":
        print(offrir)
    elif v == "anbieten":
        print("\noffrir")
        print(offrir)
    
    elif v == "boire":
        print(boire)
    elif v == "trinken":
        print("\nboire")
        print(boire)

    elif v == "connaitre":
        print(connaitre)
    
    elif v == "construire":
        print(construire)
    elif v == "bauen" or v== "konstruieren":
        print("\nconstruire")
        print(construire)
    #20
    elif v == "parler":
        print(parler)
    elif v == "reden" or v== "sprechen":
        print("\nparler")
        print(parler)

    elif v == "savoir":
        print(savoir)
    elif v == "wissen":
        print("\nsavoir")
        print(savoir)
    
    elif v == "venir":
        print(venir)
    elif v == "kommen":
        print("\nvenir")
        print(venir)

    elif v == "dire":
        print(dire)
    elif v == "erzaehlen" or v== "sagen":
        print("\ndire")
        print(dire)

    elif v == "donner":
        print(donner)
    elif v == "geben" or v== "spenden":
        print("\ndonner")
        print(donner)
    
    
    #25
    elif v == "penser":
        print(penser)
    elif v == "denken" or v== "nachdenken":
        print("\npenser")
        print(penser)
    
    elif v == "aider":
        print(aider)
    elif v == "helfen" or v== "unterstuetzen":
        print("\naider")
        print(aider)
    
    elif v == "aimer":
        print(aimer)
    elif v == "moegen" or v== "lieben":
        print("\naimer")
        print(aimer)

    elif v == "devoir":
        print(devoir)
    elif v == "muessen":
        print("\ndevoir")
        print(devoir)
    
    elif v == "habiter":
        print(habiter)
    elif v == "wohnen":
        print("\nhabiter")
        print(habiter)

    #30
    elif v == "utiliser":
        print(utiliser)        
    elif v == "verwenden" or v== "benutzen":
        print("\nutiliser")
        print(utiliser)

    elif v == "essayer":
        print(essayer)
    elif v == "probieren" or v== "auspribieren" or v== "testen":
        print("\nessayer")
        print(essayer)

    elif v == "arriver":
        print(arriver)
    elif v == "ankommen":
        print("\narriver")
        print(arriver)

    elif v == "envoyer":
        print(envoyer)
    elif v == "versenden" or v== "versenden":
        print("\nenvoyer")
        print(envoyer)
        
    elif v == "dormir":
        print(dormir)
    elif v == "schlafen":
        print("\ndormir")
        print(dormir)
    #35
    elif v == "finir":
        print(finir)
    elif v == "enden":
        print("\nfinir")
        print(finir)

    elif v == "courir":
        print(courir)
    elif v == "laufen" or v== "rennen":
        print("\ncourir")
        print(courir)

    elif v == "croire":
        print(croire)
    elif v == "glauben":
        print("\ncroire")
        print(croire)

    elif v == "écrire":
        print(écrire)
    elif v == "schreiben":
        print("\nécrire")
        print(écrire)

    elif v == "lire":
        print(lire)
    elif v == "lesen":
        print("\nlire")
        print(lire)

    #40

    elif v == "mettre":
        print(mettre)
    elif v == "stellen":
        print("\nmettre")
        print(mettre)

    elif v == "plaire":
        print(plaire)
    elif v == "gefallen":
        print("\nplaire")
        print(plaire)

    elif v == "recevoir":
        print(recevoir)
    elif v == "empfangen" or v== "bekommen":
        print("\nrecevoir")
        print(recevoir)

    elif v == "rire":
        print(rire)
    elif v == "lachen":
        print("\nrire")
        print(rire)

    elif v == "vivre":
        print(vivre)
    elif v == "leben":
        print("\nvivre")
        print(vivre)

    #45
    elif v == "voir":
        print(voir)
    elif v == "sehen":
        print("\nvoir")
        print(voir)

    elif v == "ouvrir":
        print(ouvrir)
    elif v == "oeffnen":
        print("\nouvrir")
        print(dormir)

    elif v == "promettre":
        print(promettre)
    elif v == "versprechen":
        print("\npromettre")
        print(promettre)

    elif v == "demander":
        print(demander)
    elif v == "fragen":
        print("\ndemander")
        print(demander)

    elif v == "trouver":
        print(trouver)
    elif v == "finden":
        print("\ntrouver")
        print(trouver)

    #50

    elif v == "comprendre":
        print(comprendre)
    elif v == "verstehen":
        print("\ncomprendre")
        print(comprendre)

    elif v == "tenir":
        print(tenir)
    elif v == "halten":
        print("\ntenir")
        print(tenir)

    elif v == "porter":
        print(porter)
    elif v == "tragen":
        print("\nporter")
        print(porter)

    elif v == "montrer":
        print(montrer)
    elif v == "zeigen":
        print("\nmontrer")
        print(montrer)

    elif v == "suivre":
        print(suivre)
    elif v == "folgen" or v== "verfolgen":
        print("\nsuivre")
        print(suivre)

    #55
    elif v == "compter":
        print(compter)
    elif v == "zaehlen":
        print("\ncompter")
        print(compter)

    elif v == "entendre":
        print(entendre)
    elif v == "hoeren":
        print("\nentendre")
        print(entendre)

    elif v == "permettre":
        print(permettre)
    elif v == "erlauben":
        print("\npermettre")
        print(permettre)

    elif v == "partir":
        print(partir)
    elif v == "verlassen":
        print("\npartir")
        print(partir)

    elif v == "decider":
        print(decider)
    elif v == "entscheixden":
        print("\ndecider")
        print(decider)






    else:
        print("Jacob programmed this, and do you think JACOB is able to conjugate a that difficult word in FRENCH???!!!")







