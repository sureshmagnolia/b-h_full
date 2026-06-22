import json
import os

# Define syllabus families with their descriptions
SYLLABUS_FAMILIES = {
    "RANUNCULACEAE": "Herbs, opposite/alternate leaves. Flowers bisexual, actinomorphic, sepals and petals free, stamens numerous and spirally arranged.",
    "MAGNOLIACEAE": "Aromatic trees/shrubs. Alternate simple leaves with stipules. Flowers large, showy, perianth spirally arranged, stamens and carpels numerous.",
    "MENISPERMACEAE": "Dioecious climbing shrubs. Palmate leaves. Flowers small, unisexual, trimerous. Seed hooked or curved (drupe).",
    "NYMPHAEACEAE": "Aquatic perennial herbs. Large floating peltate leaves. Flowers large, showy, solitary on long peduncles, numerous petals and stamens.",
    "POLYGALAE": "Herbs or shrubs, exstipulate leaves. Flowers zygomorphic, papilionaceous-like, 5 sepals (2 large petaloid wings), 8 stamens fused in a split tube.",
    "CARYOPHYLLEAE": "Herbs with swollen nodes, opposite entire leaves. Flowers in cymes, 5 clawed petals, 10 stamens, free central placentation.",
    "GUTTIFERAE": "Trees or shrubs with resinous sap, opposite entire leaves. Flowers actinomorphic, stamens numerous and clustered in bundles (polyadelphous).",
    "STERCULIACEAE": "Herbs/trees with stellate hairs, alternate stipulate leaves. Flowers bisexual/unisexual, stamens fused in a monadelphous tube, anthers 2-loculed.",
    "MELIACEAE": "Woody plants, mostly trees, pinnate exstipulate leaves. Flowers in panicles, stamens fused into a characteristic staminal tube.",
    "SAPINDACEAE": "Trees/shrubs, compound leaves. Flowers small, unisexual, disc present. Fruit often lobed or winged, seeds with aril.",
    "ROSACEAE": "Herbs/shrubs/trees, stipulate leaves. Flowers actinomorphic, perigynous, hypanthium present, stamens numerous, apocarpous/syncarpous.",
    "RHIZOPHOREAE": "Mangrove trees with stilt roots and viviparous germination. Opposite stipulate leaves. Flowers bisexual, inferior ovary.",
    "MELASTOMACEAE": "Herbs/shrubs with opposite 3-9 palmately veined leaves. Stamens with characteristic curved connective and poricidal dehiscing anthers.",
    "FICIOIDEAE": "Succulent herbs/shrubs. Leaves opposite or alternate. Flowers regular, petals absent or represented by petaloid staminodes, parietal/axile placentation.",
    "RUBIACEAE": "Trees/shrubs/herbs, opposite entire leaves with interpetiolar stipules. Flowers actinomorphic, sympetalous, inferior ovary.",
    "SAPOTACEAE": "Trees or shrubs with milky latex. Leaves alternate, entire. Flowers actinomorphic, sympetalous, stamens in whorls, ovary superior.",
    "GENTIANEAE": "Herbs, opposite entire leaves. Flowers actinomorphic, sympetalous, ovary superior, unilocular with parietal placentation.",
    "BORAGINEAE": "Hispid herbs with scorpioid cymes. Flowers regular, sympetalous, ovary deeply 4-lobed, style gynobasic.",
    "CONVOLVULACEAE": "Twining herbs/shrubs, alternate leaves. Flowers funnel-shaped, sympetalous, ovary superior and bicarpellate.",
    "SCROPHULARINEAE": "Herbs/shrubs, flowers zygomorphic, bilabiate, stamens 4 (didynamous) or 2, ovary superior, axile placentation with numerous ovules.",
    "PEDALINEAE": "Sticky herbs with glandular hairs. Flowers zygomorphic, solitary. Fruit a capsule or nut with hooks or horns, axile placentation.",
    "VERBENACEAE": "Stems quadrangular, opposite leaves. Flowers zygomorphic, in spikes/cymes, style terminal, ovary 2-4 celled, drupe fruit.",
    "NYCTAGINEAE": "Herbs/shrubs with opposite leaves. Flowers small, often surrounded by brightly colored bracts, perianth tubular (tepals), 1-seeded anthocarp fruit.",
    "EUPHORBIACEAE": "Plants with milky latex, flowers unisexual, perianth reduced or absent. Tricarpellate syncarpous ovary, schizocarpic regma fruit.",
    "URTICACEAE": "Herbs/shrubs with stinging hairs or cystoliths. Flowers tiny, unisexual, green. Stamens infolded in bud, ovary unilocular.",
    "CASUARINEAE": "Jointed xerophytic trees with scale leaves. Flowers unisexual, males in spikes, females in heads forming a woody cone-like infructescence.",
    "ORCHIDEAE": "Epiphytic/terrestrial herbs. Flowers zygomorphic, resupinate, perianth 6 (lip/labellum present). Pollinia, column (gynostemium).",
    "SCITAMINEAE": "Aromatic rhizomatous herbs. Flowers zygomorphic, 1 fertile stamen (Zingiberaceae) or staminodes forming petaloid structures, inferior ovary.",
    "AMARYLLIDEAE": "Perennial bulbous herbs. Scapose inflorescence with spathe. Flowers regular, 6 tepals, 6 stamens, inferior ovary.",
    "LILIACEAE": "Bulbous/cormous herbs. Flowers regular, trimerous, 6 tepals (perianth), 6 stamens, ovary superior, axile placentation.",
    "COMMELINACEAE": "Herbs with succulent stems and closed leaf sheaths. Flowers trimerous, sepals and petals distinct, stamens often with hairy filaments.",
    "AROIDEAE": "Tuberous herbs, leaves broad. Inflorescence spadix enclosed by a large, often colored spathe. Flowers unisexual or bisexual.",
    "CYPERACEAE": "Sedges with 3-angled solid stems, 3-ranked leaves with closed sheaths. Flowers in spikelets, perianth reduced to bristles, fruit an achene.",
    "GRAMINEAE": "Grasses with round hollow stems (culms), 2-ranked leaves with open sheaths and ligules. Inflorescence spikelet, fruit caryopsis."
}

# Gymnosperm families descriptions (to keep consistent)
GYMNO_DESCRIPTIONS = {
    "GNETACEAE": "Vessels present in xylem. Leaves opposite, broad or scale-like. Cones compound with outer envelope.",
    "CONIFERAE": "Wood without vessels, resin ducts present. Needles/scale leaves. Unisexual cones, seeds winged or fleshy.",
    "CYCADACEAE": "Wood without vessels. Palm-like unbranched trunk, pinnate compound leaves. Large terminal cones."
}

def generate_chart():
    data_path = r"C:\Users\sures\.gemini\antigravity-ide\scratch\b-h\bentham_hooker_data.json"
    if not os.path.exists(data_path):
        print("Data file not found!")
        return

    with open(data_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    # Let's group data hierarchically
    # Structure: Class -> Subclass -> Series -> Order -> Families
    tree = {}
    family_counter = 0

    for item in data:
        cls = item["Class"]
        subcls = item["Subclass"]
        ser = item["Series"]
        order = item["Order"]
        fam = item["Family"]

        if cls not in tree:
            tree[cls] = {}
        if subcls not in tree[cls]:
            tree[cls][subcls] = {}
        if ser not in tree[cls][subcls]:
            tree[cls][subcls][ser] = {}
        if order not in tree[cls][subcls][ser]:
            tree[cls][subcls][ser][order] = []
        
        tree[cls][subcls][ser][order].append(fam)

    # HTML code generation
    html = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Bentham & Hooker's Complete Classification System (201 Families)</title>
<link href="https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;600;700;800&family=Merriweather:ital,wght@0,400;0,700;1,400&display=swap" rel="stylesheet">
<style>
    :root {
        --color-dicot: #8b0000;
        --color-gymno: #0f3d59;
        --color-mono: #d35400;
        
        --color-poly: #2980b9;
        --color-gamo: #27ae60;
        --color-monochlamy: #8e44ad;
        
        --color-thala-bg: #ebf5fb;
        --color-disci-bg: #fef9e7;
        --color-calyci-bg: #e8f8f5;
        
        --color-inferae-bg: #e9f7ef;
        --color-hetero-bg: #ebdef0;
        --color-bicar-bg: #f5eef8;

        --color-curve-bg: #f4ecf7;
        
        --color-mono-bg1: #fbeee6;
        --color-mono-bg2: #fdf2e9;
    }

    body {
        font-family: 'Outfit', sans-serif;
        margin: 0;
        padding: 0;
        background-color: #f1f2f6;
        color: #2c3e50;
        font-size: 11px;
    }

    @media print {
        @page { size: A3 landscape; margin: 6mm; }
        body { background-color: #fff; -webkit-print-color-adjust: exact; print-color-adjust: exact; }
        .main-container { box-shadow: none; max-width: 100%; margin: 0; border: none; }
        .no-print { display: none; }
        .grid-container { background: #fff !important; padding: 0 !important; gap: 6px !important; }
    }

    .main-container {
        display: flex;
        flex-direction: column;
        width: 100%;
        max-width: 1720px;
        margin: 10px auto;
        background: #fff;
        box-shadow: 0 10px 40px rgba(0,0,0,0.06);
        border-radius: 8px;
        overflow: hidden;
    }

    .header-main {
        background: linear-gradient(135deg, #1e272e 0%, #2f3640 100%);
        color: white;
        text-align: center;
        padding: 10px;
        font-family: 'Merriweather', serif;
        border-bottom: 2px solid #2f3542;
        position: relative;
    }

    .header-main h1 {
        margin: 0;
        font-size: 20px;
        font-weight: 700;
        letter-spacing: 1.5px;
        text-transform: uppercase;
        color: #f1c40f;
    }
    
    .super-class-header {
        background-color: #2f3542;
        color: #ffffff;
        text-align: center;
        padding: 5px;
        font-weight: 700;
        font-size: 14px;
        text-transform: uppercase;
        letter-spacing: 3px;
        border-bottom: 2px solid #747d8c;
    }

    .grid-container {
        display: grid;
        grid-template-columns: 3.3fr 0.8fr 1.1fr;
        background: #f1f2f6;
        padding: 6px;
        gap: 6px;
        align-items: start;
    }

    /* --- LEVEL 1: Top Level Cards --- */
    .top-level-card {
        background-color: #ffffff;
        border-radius: 6px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.04);
        display: flex;
        flex-direction: column;
        height: 100%;
    }
    .top-level-header {
        color: white;
        text-align: center;
        padding: 8px 4px;
        font-weight: 700;
        font-size: 13px;
        text-transform: uppercase;
        border-top-left-radius: 6px;
        border-top-right-radius: 6px;
    }
    .top-level-desc {
        font-size: 9px;
        font-weight: 400;
        margin-top: 2px;
        text-transform: none;
        opacity: 0.95;
    }

    /* --- LEVEL 2: Subclass Cards --- */
    .dicot-content {
        display: grid;
        grid-template-columns: 1.1fr 1fr 0.9fr;
        background: #f1f2f6;
        padding: 4px;
        gap: 4px;
        flex: 1;
    }
    .subclass-card {
        background-color: #ffffff;
        border-radius: 4px;
        box-shadow: 0 2px 8px rgba(0,0,0,0.02);
        display: flex;
        flex-direction: column;
        border: 1px solid #e1b12c;
    }
    .subclass-header {
        color: white;
        text-align: center;
        padding: 6px;
        font-weight: 600;
        font-size: 11px;
    }
    .subclass-body {
        padding: 4px;
        display: flex;
        flex-direction: column;
        background: #f8f9fa;
        flex: 1;
        gap: 4px;
    }

    /* --- LEVEL 3: Series Card --- */
    .series-block {
        display: flex;
        flex-direction: row;
        background-color: #ffffff;
        border-radius: 4px;
        box-shadow: 0 1px 4px rgba(0,0,0,0.02);
        border: 1px solid #ced6e0;
    }
    .series-left {
        flex: 0 0 22px;
        background-color: rgba(0,0,0,0.03);
        border-right: 1px solid #dfe4ea;
        display: flex;
        align-items: center;
        justify-content: center;
        padding: 4px 1px;
        border-top-left-radius: 3px;
        border-bottom-left-radius: 3px;
    }
    .series-title-vertical {
        writing-mode: vertical-rl;
        transform: rotate(180deg);
        font-weight: 700;
        font-size: 9px;
        color: #2f3542;
        letter-spacing: 1px;
        text-align: center;
    }
    .series-content {
        flex: 1;
        display: flex;
        flex-direction: column;
        padding: 3px;
        background-color: #ffffff;
        gap: 3px;
    }

    /* --- LEVEL 4: Order Card --- */
    .order-row {
        display: flex;
        flex-direction: column;
        background-color: #fcfcfc;
        border-radius: 3px;
        border: 1px solid #f1f2f6;
        padding: 3px;
    }
    
    .order-header-row {
        display: flex;
        align-items: center;
        justify-content: space-between;
        margin-bottom: 3px;
        padding-bottom: 2px;
        border-bottom: 1px dashed #dfe4ea;
    }
    
    .order-title {
        font-weight: 700;
        color: white;
        font-size: 9px;
        text-transform: uppercase;
        padding: 1.5px 4px;
        border-radius: 3px;
        display: inline-block;
    }

    .order-desc {
        font-size: 8px;
        color: #747d8c;
        font-style: italic;
        line-height: 1;
        margin-left: 5px;
    }

    /* --- LEVEL 5 & 6: Family Badges --- */
    .families-flex-container {
        display: flex;
        flex-wrap: wrap;
        gap: 3px;
        align-items: center;
    }

    .family-badge {
        font-size: 8.5px;
        font-weight: 600;
        background-color: #f1f2f6;
        color: #2c3e50;
        padding: 2.5px 5px;
        border-radius: 12px;
        border: 1px solid #ced6e0;
        display: inline-flex;
        align-items: center;
        transition: all 0.2s;
    }

    /* Highlighted Syllabus Families */
    .family-badge.syllabus-highlight {
        background-color: #fff9db;
        border: 1.5px solid #f1c40f;
        color: #b7791f;
        box-shadow: 0 1px 3px rgba(241, 196, 15, 0.2);
    }
    
    .family-badge.syllabus-highlight::before {
        content: "★ ";
        color: #f1c40f;
        margin-right: 2px;
        font-size: 8px;
    }

    /* Detail block for syllabus families */
    details.syllabus-details-box {
        margin-top: 4px;
        background-color: #fffaf0;
        border-left: 2.5px solid #f1c40f;
        border-radius: 2px;
        font-size: 8.2px;
        line-height: 1.1;
        color: #5d4037;
    }
    
    details.syllabus-details-box summary {
        padding: 3px 5px;
        cursor: pointer;
        outline: none;
        user-select: none;
    }
    
    details.syllabus-details-box strong {
        color: #795548;
        text-transform: uppercase;
        font-size: 8px;
    }

    /* Series Specific Tints */
    .bg-thala .series-left { background-color: var(--color-thala-bg); }
    .bg-disci .series-left { background-color: var(--color-disci-bg); }
    .bg-calyci .series-left { background-color: var(--color-calyci-bg); }
    .bg-inferae .series-left { background-color: var(--color-inferae-bg); }
    .bg-hetero .series-left { background-color: var(--color-hetero-bg); }
    .bg-bicar .series-left { background-color: var(--color-bicar-bg); }
    .bg-curve .series-left { background-color: var(--color-curve-bg); }

    /* Gymnosperm & Monocot styling */
    .gymno-content { 
        padding: 4px; 
        display: flex; 
        flex-direction: column; 
        gap: 4px; 
        background: #f1f2f6;
        flex: 1;
    }
    .gymno-card {
        background: #ffffff;
        padding: 4px;
        border-radius: 4px;
        box-shadow: 0 1px 3px rgba(0,0,0,0.03);
        border: 1px solid #ced6e0;
    }
    .gymno-title { font-weight: 700; font-size: 9px; color: white; padding: 2px 5px; border-radius: 3px; display: inline-block; text-transform: uppercase;}
    
    .mono-content { 
        display: flex; 
        flex-direction: column; 
        background: #f1f2f6; 
        padding: 4px;
        gap: 4px;
        flex: 1;
    }
    
    .mono-series-card {
        display: flex;
        flex-direction: column;
        background-color: #ffffff;
        border-radius: 4px;
        box-shadow: 0 1px 4px rgba(0,0,0,0.02);
        border: 1px solid #ced6e0;
        padding: 4px;
    }
    .mono-series-header {
        display: flex;
        justify-content: space-between;
        align-items: center;
        margin-bottom: 4px;
        border-bottom: 1.5px solid #dfe4ea;
        padding-bottom: 2px;
    }
    .mono-left-title {
        font-weight: 700; 
        color: white; 
        font-size: 9px;
        padding: 2px 5px;
        border-radius: 3px;
        display: inline-block;
    }
    .mono-series-desc {
        font-size: 8px;
        color: #747d8c;
        font-style: italic;
        margin-left: 5px;
    }

</style>
</head>
<body>

<div class="no-print" style="text-align: center; padding: 6px; background-color: #2f3542;">
    <button onclick="window.print()" style="padding: 6px 14px; font-size: 12px; cursor: pointer; background: #e1b12c; color: #2f3542; border: none; border-radius: 4px; font-weight: 800; box-shadow: 0 2px 4px rgba(0,0,0,0.2); transition: all 0.2s;">🖨️ Print Complete Chart (A3 Landscape)</button>
</div>

<div class="main-container">
    <div class="header-main">
        <h1>Bentham and Hooker's Classification System</h1>
        <div style="font-size: 11px; font-weight: 600; color: #dfe4ea; letter-spacing: 0.5px; margin-top: 2px;">
            Complete Tree of 201 Families | Highlighted Syllabus Families (★) with Diagnostic Descriptions (Collapsible)
        </div>
    </div>
    
    <div class="super-class-header">
        PHANEROGAMS (SEED-BEARING PLANTS)
    </div>
    
    <div class="grid-container">
"""

    # We will generate families sequentially with numbers
    # Class colors mapping
    class_headers = {
        "Dicotyledonae": ("DICOTYLEDONS", "var(--color-dicot)", "Two cotyledons, reticulate venation, pentamerous flowers, ringed vascular bundles"),
        "GYMNOSPERMEAE": ("GYMNOSPERMS", "var(--color-gymno)", "Naked seeded plants, vessels absent in xylem, cones present"),
        "Monocotyledonae": ("MONOCOTYLEDONS", "var(--color-mono)", "One cotyledon, parallel venation, trimerous flowers, scattered vascular bundles")
    }

    subclass_headers = {
        "Polypetalae": ("POLYPETALAE", "var(--color-poly)", "Corolla of free distinct petals"),
        "Gamopetalae": ("GAMOPETALAE", "var(--color-gamo)", "Corolla of fused sympetalous petals"),
        "Monochlamydeae": ("MONOCHLAMYDEAE", "var(--color-monochlamy)", "Perianth simple (single whorl) or absent")
    }

    # Series tints for Dicot subclasses
    series_classes = {
        "Thalamiflorae": "bg-thala",
        "Disciflorae": "bg-disci",
        "Calyciflorae": "bg-calyci",
        "Inferae": "bg-inferae",
        "Heteromerae": "bg-hetero",
        "Bicarpellatae": "bg-bicar",
        "Curvembryae": "bg-curve"
    }

    # Colors for orders in Polypetalae
    poly_order_colors = {
        "Ranales": "#3498db",
        "Parietales": "#16a085",
        "Polygalyneae": "#8e44ad",
        "Caryophylliniae": "#2980b9",
        "Guttiferales": "#e67e22",
        "Malvales": "#f1c40f",
        "Geraniales": "#2ecc71",
        "Olacales": "#1abc9c",
        "Celestrales": "#34495e",
        "Sapindales": "#f39c12",
        "POTIUS GENERA ANOMALA": "#7f8c8d",
        "Rosales": "#e74c3c",
        "Myrtales": "#c0392b",
        "Passiflorales": "#8e44ad",
        "Ficoidales": "#9b59b6",
        "Umbellales": "#2980b9"
    }

    # Colors for orders in Gamopetalae
    gamo_order_colors = {
        "Rubiales": "#27ae60",
        "Asterales": "#16a085",
        "Companales": "#f39c12",
        "Ericales": "#8e44ad",
        "Primulales": "#2980b9",
        "Ebenales": "#c0392b",
        "Gentianales": "#f39c12",
        "Polemoneales": "#e67e22",
        "Personales": "#d35400",
        "Lamiales": "#8e44ad",
        "Incertae sedis": "#7f8c8d"
    }

    # Colors for Monochlamydeae series
    monochlamy_colors = {
        "Curvembryae": "#9b59b6",
        "Multiovulatae Aquaticae": "#3498db",
        "Multiovulatae terrostris": "#e74c3c",
        "Microembrae": "#2ecc71",
        "Daphnales": "#9b59b6",
        "Achlamydosporeae": "#e67e22",
        "Unisexuales": "#f1c40f",
        "Ordines Anomali": "#34495e"
    }

    # Colors for Monocot series
    mono_series_colors = {
        "Microspermae": "#d35400",
        "Epigynae": "#e67e22",
        "Coronariae": "#f39c12",
        "Calycinae": "#8e44ad",
        "Nudiflorae": "#c0392b",
        "Apocarpae": "#2980b9",
        "Glumaceae": "#f1c40f"
    }

    # Custom short descriptors for some orders
    order_descriptors = {
        "Ranales": "Many stamens, apocarpous carpels",
        "Parietales": "Parietal placentation",
        "Polygalyneae": "Irregular flowers, bilocular ovary",
        "Caryophylliniae": "Opposite leaves, free-central placentation",
        "Guttiferales": "Opposite leaves, numerous stamens",
        "Malvales": "Stellate hairs, monadelphous stamens",
        "Geraniales": "Ovary multi-locular, nectary disc present",
        "Olacales": "Disc cushion-like, superior ovary",
        "Celestrales": "Disc prominent, stamens alternate with petals",
        "Sapindales": "Compound leaves, disc prominent, variable stamens",
        "Rosales": "Perigynous/epigynous, stipulate leaves",
        "Myrtales": "Syncarpous, epigynous, aromatic",
        "Passiflorales": "Climbers, parietal placentation, tendrils",
        "Ficoidales": "Carpels fused, succulent habit",
        "Umbellales": "Flowers in umbels, inferior ovary",
        "Rubiales": "Opposite leaves, interpetiolar stipules",
        "Asterales": "Syngenesious anthers, head inflorescence",
        "Companales": "Anthers free or connate, inferior ovary",
        "Ericales": "Anthers open by pores, superior ovary",
        "Primulales": "Stamens opposite petals, free-central placentation",
        "Ebenales": "Woody plants, superior ovary, stamens in whorls",
        "Gentianales": "Opposite leaves, superior bicarpellate ovary",
        "Polemoneales": "Alternate leaves, regular flowers",
        "Personales": "Zygomorphic, didynamous stamens, axile placentation",
        "Lamiales": "Zygomorphic, drupe/schizocarp, style terminal/gynobasic",
        "Microspermae": "Inferior ovary, tiny seeds",
        "Epigynae": "Inferior ovary, large endospermic seeds",
        "Coronariae": "Petaloid perianth, superior ovary",
        "Calycinae": "Sepaloid perianth, superior ovary",
        "Nudiflorae": "Apetalous, spadix common",
        "Apocarpae": "Superior apocarpous ovary",
        "Glumaceae": "Flowers enclosed in glumes (scaly bracts)"
    }

    # 1. DICOTS COLUMN
    dicot_tree = tree.get("Dicotyledonae", {})
    html += f"""        <!-- DICOTYLEDONS CARD -->
        <div class="top-level-card" style="border-top: 4px solid var(--color-dicot);">
            <div class="top-level-header" style="background-color: var(--color-dicot);">
                {class_headers["Dicotyledonae"][0]}
                <div class="top-level-desc">{class_headers["Dicotyledonae"][2]}</div>
            </div>
            
            <div class="dicot-content">
"""

    # We iterate subclasses of Dicotyledons
    for subcls in ["Polypetalae", "Gamopetalae", "Monochlamydeae"]:
        subcls_tree = dicot_tree.get(subcls, {})
        subcls_name, subcls_col, subcls_desc = subclass_headers[subcls]
        
        html += f"""                <!-- {subcls_name} CARD -->
                <div class="subclass-card" style="border-color: {subcls_col};">
                    <div class="subclass-header" style="background-color: {subcls_col};">
                        {subcls_name}
                        <div class="top-level-desc" style="font-size: 8px;">{subcls_desc}</div>
                    </div>
                    
                    <div class="subclass-body">
"""
        # Iterate Series
        for ser, orders in subcls_tree.items():
            tint_class = series_classes.get(ser, "")
            
            # If Series is '-', we don't draw a series block header wrapper, but let's draw it cleanly
            if ser != "-":
                html += f"""                        <!-- SERIES {ser.upper()} -->
                        <div class="series-block {tint_class}">
                            <div class="series-left"><div class="series-title-vertical">{ser.upper()}</div></div>
                            <div class="series-content">
"""
            
            # Iterate Orders in Series
            for order, families in orders.items():
                # Pick order color
                order_col = "#2c3e50"
                if subcls == "Polypetalae":
                    order_col = poly_order_colors.get(order, "#2c3e50")
                elif subcls == "Gamopetalae":
                    order_col = gamo_order_colors.get(order, "#2c3e50")
                elif subcls == "Monochlamydeae":
                    # Monochlamydeae has Series as top groups instead of Orders, the JSON has Order as '-'
                    order_col = monochlamy_colors.get(ser, "#2c3e50")

                # Get description
                order_desc_text = order_descriptors.get(order if order != "-" else ser, "")
                
                html += f"""                                <div class="order-row" style="border-left: 3px solid {order_col};">
                                    <div class="order-header-row">
                                        <div class="order-title" style="background-color: {order_col};">
                                            {order.upper() if order != "-" else ser.upper()}
                                        </div>
                                        {f'<div class="order-desc">{order_desc_text}</div>' if order_desc_text else ''}
                                    </div>
                                    <div class="families-flex-container">
"""
                # Render Families
                syllabus_details = []
                for fam in families:
                    family_counter += 1
                    # Clean family name for lookup
                    lookup_name = fam.replace(" [sic]", "").upper()
                    
                    is_syllabus = lookup_name in SYLLABUS_FAMILIES
                    badge_class = "family-badge syllabus-highlight" if is_syllabus else "family-badge"
                    
                    html += f"""                                        <span class="{badge_class}">
                                            {family_counter}. {fam}
                                        </span>
"""
                    if is_syllabus:
                        desc = SYLLABUS_FAMILIES[lookup_name]
                        syllabus_details.append((family_counter, fam, desc))

                html += """                                    </div>
"""
                # Render syllabus detailed boxes below the pills
                for num, fam_name, desc in syllabus_details:
                    html += f"""                                    <details class="syllabus-details-box">
                                        <summary><strong>{num}. {fam_name}</strong></summary>
                                        <div style="padding: 2px 4px 4px 4px; border-top: 1px dashed #f5deb3; margin-top: 2px;">{desc}</div>
                                    </details>
"""
                
                html += """                                </div>
"""
            
            if ser != "-":
                html += """                            </div>
                        </div>
"""

        html += """                    </div>
                </div>
"""

    html += """            </div>
        </div>
"""

    # 2. GYMNOSPERMS COLUMN
    gymno_tree = tree.get("GYMNOSPERMEAE", {})
    html += f"""        <!-- GYMNOSPERMS CARD -->
        <div class="top-level-card" style="border-top: 4px solid var(--color-gymno);">
            <div class="top-level-header" style="background-color: var(--color-gymno);">
                {class_headers["GYMNOSPERMEAE"][0]}
                <div class="top-level-desc">{class_headers["GYMNOSPERMEAE"][2]}</div>
            </div>
            
            <div class="gymno-content">
"""
    # Gymnosperms has Subclass '-', Series '-', Order '-'
    # We display them directly as cards
    gymno_families = gymno_tree.get("-", {}).get("-", {}).get("-", [])
    gymno_colors = ["#3498db", "#2ecc71", "#e74c3c"]
    
    for idx, fam in enumerate(gymno_families):
        family_counter += 1
        col = gymno_colors[idx % len(gymno_colors)]
        desc = GYMNO_DESCRIPTIONS.get(fam.upper(), "")
        html += f"""                <div class="gymno-card" style="border-left: 3px solid {col};">
                    <div class="gymno-title" style="background-color: {col};">
                        {family_counter}. {fam}
                    </div>
                    {f'<details class="syllabus-details-box" style="border-left-color: {col}; margin-top:3px; background-color:#fcfcfc;"><summary><strong>DIAGNOSTIC CHARACTERS</strong></summary><div style="padding: 2px 4px 4px 4px; border-top: 1px dashed #f5deb3; margin-top: 2px;">{desc}</div></details>' if desc else ''}
                </div>
"""

    html += """            </div>
        </div>
"""

    # 3. MONOCOTS COLUMN
    mono_tree = tree.get("Monocotyledonae", {})
    html += f"""        <!-- MONOCOTYLEDONS CARD -->
        <div class="top-level-card" style="border-top: 4px solid var(--color-mono);">
            <div class="top-level-header" style="background-color: var(--color-mono);">
                {class_headers["Monocotyledonae"][0]}
                <div class="top-level-desc">{class_headers["Monocotyledonae"][2]}</div>
            </div>
            
            <div class="mono-content">
"""
    # Monocots has Subclass '-', Series, Order '-'
    mono_subclasses = mono_tree.get("-", {})
    for ser, orders in mono_subclasses.items():
        ser_col = mono_series_colors.get(ser, "#2c3e50")
        ser_desc = order_descriptors.get(ser, "")
        
        html += f"""                <!-- SERIES {ser.upper()} -->
                <div class="mono-series-card" style="border-left: 3px solid {ser_col};">
                    <div class="mono-series-header">
                        <div class="mono-left-title" style="background-color: {ser_col};">
                            {ser.upper()}
                        </div>
                        {f'<div class="mono-series-desc">{ser_desc}</div>' if ser_desc else ''}
                    </div>
                    <div class="families-flex-container">
"""
        
        syllabus_details = []
        # Monocots has Order '-'
        families = orders.get("-", [])
        for fam in families:
            family_counter += 1
            lookup_name = fam.replace(" [sic]", "").upper()
            
            is_syllabus = lookup_name in SYLLABUS_FAMILIES
            badge_class = "family-badge syllabus-highlight" if is_syllabus else "family-badge"
            
            html += f"""                        <span class="{badge_class}">
                            {family_counter}. {fam}
                        </span>
"""
            if is_syllabus:
                desc = SYLLABUS_FAMILIES[lookup_name]
                syllabus_details.append((family_counter, fam, desc))

        html += """                    </div>
"""
        for num, fam_name, desc in syllabus_details:
            html += f"""                    <div class="syllabus-details-box" style="border-left-color: {ser_col};">
                        <strong>{num}. {fam_name}</strong> &mdash; {desc}
                    </div>
"""
        html += """                </div>
"""

    html += f"""            </div>
        </div>
    </div>
    
    <div style="display: flex; justify-content: space-between; align-items: center; padding: 10px 20px; background: #2f3542; color: white; border-top: 2px solid #747d8c;">
        <div style="font-size: 10px; opacity: 0.8;">
            Total Families: {family_counter} (Complete Bentham &amp; Hooker System)
        </div>
        <div style="text-align: right; font-size: 11px; font-weight: bold; color: #f1c40f;">
            Prepared by: Dr. Suresh V, Department of Botany, Government Victoria College, Palakkad, Kerala
        </div>
    </div>
</div>

</body>
</html>"""

    output_path = r"C:\Users\sures\.gemini\antigravity-ide\scratch\b-h\index.html"
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(html)
    
    print(f"Success! Generated {family_counter} families.")

if __name__ == "__main__":
    generate_chart()
