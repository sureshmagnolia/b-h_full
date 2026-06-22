import json
import os
import sys

# Import descriptions
sys.path.append(r"C:\Users\sures\.gemini\antigravity-ide\scratch\b-h")
try:
    from generate_descriptions import ALL_FAMILY_DESCRIPTIONS
except ImportError:
    ALL_FAMILY_DESCRIPTIONS = {}

# Syllabus families list
SYLLABUS_FAMILIES = [
    "RANUNCULACEAE", "MAGNOLIACEAE", "MENISPERMACEAE", "NYMPHAEACEAE", 
    "POLYGALAE", "CARYOPHYLLEAE", "GUTTIFERAE", "STERCULIACEAE", 
    "MELIACEAE", "SAPINDACEAE", "ROSACEAE", "RHIZOPHOREAE", 
    "MELASTOMACEAE", "FICIOIDEAE", "RUBIACEAE", "SAPOTACEAE", 
    "GENTIANEAE", "BORAGINEAE", "CONVOLVULACEAE", "SCROPHULARINEAE", 
    "PEDALINEAE", "VERBENACEAE", "NYCTAGINEAE", "EUPHORBIACEAE", 
    "URTICACEAE", "CASUARINEAE", "ORCHIDEAE", "SCITAMINEAE", 
    "AMARYLLIDEAE", "LILIACEAE", "COMMELINACEAE", "AROIDEAE", 
    "CYPERACEAE", "GRAMINEAE"
]

# Series descriptions (Characters)
SERIES_DESCRIPTIONS = {
    # Polypetalae
    "Thalamiflorae": "Sepals distinct/free. Petals and stamens hypogynous (inserted on thalamus, below superior ovary).",
    "Disciflorae": "Sepals & petals free. Stamens hypogynous, inserted on/around a prominent nectar disc at base of superior ovary.",
    "Calyciflorae": "Sepals fused (calyx cup-like). Stamens and petals perigynous/epigynous. Ovary often inferior.",
    
    # Gamopetalae
    "Inferae": "Calyx tube fused with ovary (epigynous). Ovary inferior. Stamens usually equal corolla lobes.",
    "Heteromerae": "Calyx tube free from ovary (hypogynous). Ovary superior. Carpels more than 2.",
    "Bicarpellatae": "Calyx tube free from ovary (hypogynous). Ovary superior, typically bicarpellate (2 fused carpels).",
    
    # Monochlamydeae
    "Curvembryae": "Usually single ovule, embryo coiled or curved around the endosperm.",
    "Multiovulatae Aquaticae": "Aquatic plants, ovary syncarpous with numerous ovules.",
    "Multiovulatae terrostris": "Terrestrial plants, ovary syncarpous with numerous ovules.",
    "Microembrae": "Embryo very small, embedded in copious endosperm.",
    "Daphnales": "Ovary typically with a single carpel and single ovule. Perianth sepaloid.",
    "Achlamydosporeae": "Ovary inferior, 1-loculed, 1-3 ovules, seeds without testa.",
    "Unisexuales": "Flowers unisexual, perianth simple or absent, ovary superior.",
    "Ordines Anomali": "Anomalous families with uncertain relationships, showing diverse characteristics.",
    
    # Monocotyledons
    "Microspermae": "Ovary inferior, seeds very small, numerous, without endosperm.",
    "Epigynae": "Ovary inferior, seeds large with abundant endosperm.",
    "Coronariae": "Perianth colorful and petaloid, ovary superior.",
    "Calycinae": "Perianth sepaloid or dry (green/brown), ovary superior.",
    "Nudiflorae": "Perianth absent or reduced to small scales/bristles, ovary superior.",
    "Apocarpae": "Ovary superior, composed of free carpels (apocarpous).",
    "Glumaceae": "Flowers in spikelets, enclosed by scale-like bracts (glumes), perianth reduced/chaffy."
}

def generate_chart():
    data_path = r"C:\Users\sures\.gemini\antigravity-ide\scratch\b-h\bentham_hooker_data.json"
    if not os.path.exists(data_path):
        print("Data file not found!")
        return

    with open(data_path, "r", encoding="utf-8") as f:
        data = json.load(f)

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
<title>Bentham & Hooker's Complete Classification System (202 Families)</title>
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
        
        /* Force open details to print content */
        details {
            display: block !important;
        }
        details summary::before {
            content: "" !important;
        }
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

    /* --- LEVEL 2: Subclass Collapsible Cards --- */
    .dicot-content {
        display: grid;
        grid-template-columns: 1.1fr 1fr 0.9fr;
        background: #f1f2f6;
        padding: 4px;
        gap: 4px;
        flex: 1;
    }
    details.subclass-card {
        background-color: #ffffff;
        border-radius: 4px;
        box-shadow: 0 2px 8px rgba(0,0,0,0.02);
        display: flex;
        flex-direction: column;
        border: 1px solid #ced6e0;
        margin-bottom: 4px;
    }
    details.subclass-card summary.subclass-header {
        color: white;
        text-align: center;
        padding: 6px;
        font-weight: 600;
        font-size: 11px;
        cursor: pointer;
        outline: none;
        user-select: none;
        list-style: none;
    }
    details.subclass-card summary.subclass-header::-webkit-details-marker {
        display: none;
    }
    details.subclass-card summary.subclass-header::before {
        content: "▼ ";
        font-size: 8px;
        margin-right: 4px;
    }
    details.subclass-card:not([open]) summary.subclass-header::before {
        content: "▶ ";
    }
    .subclass-body {
        padding: 4px;
        display: flex;
        flex-direction: column;
        background: #f8f9fa;
        gap: 4px;
        border-top: 1px solid #ced6e0;
    }

    /* --- LEVEL 3: Series Collapsible Card --- */
    details.series-block {
        background-color: #ffffff;
        border-radius: 4px;
        box-shadow: 0 1px 4px rgba(0,0,0,0.02);
        border: 1px solid #ced6e0;
        margin-bottom: 4px;
    }
    details.series-block summary.series-summary-header {
        padding: 5px 6px;
        font-weight: 700;
        font-size: 9.5px;
        cursor: pointer;
        outline: none;
        user-select: none;
        color: #2f3542;
        background-color: rgba(0,0,0,0.02);
        list-style: none;
        display: flex;
        align-items: center;
        justify-content: space-between;
    }
    details.series-block summary.series-summary-header::-webkit-details-marker {
        display: none;
    }
    details.series-block summary.series-summary-header::before {
        content: "▼ ";
        font-size: 8px;
        color: #747d8c;
        margin-right: 4px;
    }
    details.series-block:not([open]) summary.series-summary-header::before {
        content: "▶ ";
    }
    .series-title-text {
        text-transform: uppercase;
        margin-right: 6px;
    }
    .series-desc-text {
        font-size: 8px;
        color: #747d8c;
        font-weight: 400;
        font-style: italic;
        text-align: right;
    }
    .series-content {
        padding: 4px;
        background-color: #ffffff;
        display: flex;
        flex-direction: column;
        gap: 4px;
        border-top: 1px solid #dfe4ea;
    }

    /* --- LEVEL 4: Order Collapsible Card --- */
    details.order-row {
        display: flex;
        flex-direction: column;
        background-color: #fcfcfc;
        border-radius: 3px;
        border: 1px solid #f1f2f6;
        margin-bottom: 2px;
    }
    
    details.order-row summary.order-header-row {
        display: flex;
        align-items: center;
        justify-content: flex-start;
        padding: 3px;
        cursor: pointer;
        outline: none;
        user-select: none;
        list-style: none;
    }
    details.order-row summary.order-header-row::-webkit-details-marker {
        display: none;
    }
    
    details.order-row summary.order-header-row::before {
        content: "▼ ";
        font-size: 8px;
        color: #747d8c;
        margin-right: 4px;
        margin-left: 2px;
    }
    details.order-row:not([open]) summary.order-header-row::before {
        content: "▶ ";
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
        margin-left: 8px;
    }

    /* --- LEVEL 5 & 6: Family Collapsible Cards --- */
    .families-flex-container {
        display: flex;
        flex-wrap: wrap;
        gap: 3px;
        align-items: flex-start;
        padding: 4px;
        background-color: #ffffff;
    }
    .order-row .families-flex-container {
        border-top: 1px dashed #dfe4ea;
    }

    details.family-card-collapsible {
        background-color: #f1f2f6;
        border: 1px solid #ced6e0;
        border-radius: 4px;
        font-size: 8.5px;
        color: #2c3e50;
        transition: all 0.2s;
        box-sizing: border-box;
    }
    
    details.family-card-collapsible[open] {
        background-color: #ffffff;
        border-color: #a4b0be;
        box-shadow: 0 2px 6px rgba(0,0,0,0.05);
        flex: 1 1 100%;
    }

    /* Highlighted Syllabus Families (Readily Visible) */
    details.family-card-collapsible.syllabus-highlight {
        background-color: #fffde7;
        border: 1.2px solid #f1c40f;
    }

    details.family-card-collapsible.syllabus-highlight[open] {
        background-color: #fff9db;
        border: 1.5px solid #f1c40f;
        box-shadow: 0 2px 8px rgba(241, 196, 15, 0.15);
    }

    details.family-card-collapsible summary {
        padding: 3px 6px;
        font-weight: 600;
        cursor: pointer;
        outline: none;
        user-select: none;
        list-style: none;
    }

    details.family-card-collapsible summary::-webkit-details-marker {
        display: none;
    }

    details.family-card-collapsible summary::before {
        content: "▸ ";
        color: #747d8c;
        margin-right: 2px;
        font-size: 8px;
    }

    details.family-card-collapsible[open] summary::before {
        content: "▾ ";
        color: #2f3542;
    }

    details.family-card-collapsible.syllabus-highlight summary::before {
        content: "★ ▸ ";
        color: #f1c40f;
    }

    details.family-card-collapsible.syllabus-highlight[open] summary::before {
        content: "★ ▾ ";
        color: #f1c40f;
    }

    .family-desc-content {
        padding: 3px 6px 5px 6px;
        border-top: 1px dashed #dfe4ea;
        color: #57606f;
        line-height: 1.15;
        font-size: 8.2px;
    }

    details.family-card-collapsible.syllabus-highlight .family-desc-content {
        border-top-color: #f1c40f;
        color: #7f5f00;
        font-weight: 500;
    }

    /* Series Specific Tints */
    .bg-thala .series-summary-header { background-color: var(--color-thala-bg) !important; }
    .bg-disci .series-summary-header { background-color: var(--color-disci-bg) !important; }
    .bg-calyci .series-summary-header { background-color: var(--color-calyci-bg) !important; }
    .bg-inferae .series-summary-header { background-color: var(--color-inferae-bg) !important; }
    .bg-hetero .series-summary-header { background-color: var(--color-hetero-bg) !important; }
    .bg-bicar .series-summary-header { background-color: var(--color-bicar-bg) !important; }
    .bg-curve .series-summary-header { background-color: var(--color-curve-bg) !important; }

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
    
    .mono-content { 
        display: flex; 
        flex-direction: column; 
        background: #f1f2f6; 
        padding: 4px;
        gap: 4px;
        flex: 1;
    }
    
    details.mono-series-card {
        display: flex;
        flex-direction: column;
        background-color: #ffffff;
        border-radius: 4px;
        box-shadow: 0 1px 4px rgba(0,0,0,0.02);
        border: 1px solid #ced6e0;
        margin-bottom: 4px;
    }
    details.mono-series-card summary.mono-series-header {
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding: 5px;
        cursor: pointer;
        outline: none;
        user-select: none;
        list-style: none;
    }
    details.mono-series-card summary.mono-series-header::-webkit-details-marker {
        display: none;
    }
    details.mono-series-card summary.mono-series-header::before {
        content: "▼ ";
        font-size: 8px;
        color: #747d8c;
        margin-right: 4px;
    }
    details.mono-series-card:not([open]) summary.mono-series-header::before {
        content: "▶ ";
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
        margin-left: 8px;
        text-align: right;
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
            Complete Tree of 202 Families | Interactive Collapsible Badges &amp; Groups | Syllabus Families (★) Open by Default
        </div>
    </div>
    
    <div class="super-class-header">
        PHANEROGAMS (SEED-BEARING PLANTS)
    </div>
    
    <div class="grid-container">
"""

    # Class headers
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

    series_classes = {
        "Thalamiflorae": "bg-thala",
        "Disciflorae": "bg-disci",
        "Calyciflorae": "bg-calyci",
        "Inferae": "bg-inferae",
        "Heteromerae": "bg-hetero",
        "Bicarpellatae": "bg-bicar",
        "Curvembryae": "bg-curve"
    }

    poly_order_colors = {
        "Ranales": "#3498db", "Parietales": "#16a085", "Polygalyneae": "#8e44ad", "Caryophylliniae": "#2980b9",
        "Guttiferales": "#e67e22", "Malvales": "#f1c40f", "Geraniales": "#2ecc71", "Olacales": "#1abc9c",
        "Celestrales": "#34495e", "Sapindales": "#f39c12", "POTIUS GENERA ANOMALA": "#7f8c8d", "Rosales": "#e74c3c",
        "Myrtales": "#c0392b", "Passiflorales": "#8e44ad", "Ficoidales": "#9b59b6", "Umbellales": "#2980b9"
    }

    gamo_order_colors = {
        "Rubiales": "#27ae60", "Asterales": "#16a085", "Companales": "#f39c12", "Ericales": "#8e44ad",
        "Primulales": "#2980b9", "Ebenales": "#c0392b", "Gentianales": "#f39c12", "Polemoneales": "#e67e22",
        "Personales": "#d35400", "Lamiales": "#8e44ad", "Incertae sedis": "#7f8c8d"
    }

    monochlamy_colors = {
        "Curvembryae": "#9b59b6", "Multiovulatae Aquaticae": "#3498db", "Multiovulatae terrostris": "#e74c3c",
        "Microembrae": "#2ecc71", "Daphnales": "#9b59b6", "Achlamydosporeae": "#e67e22", "Unisexuales": "#f1c40f",
        "Ordines Anomali": "#34495e"
    }

    mono_series_colors = {
        "Microspermae": "#d35400", "Epigynae": "#e67e22", "Coronariae": "#f39c12", "Calycinae": "#8e44ad",
        "Nudiflorae": "#c0392b", "Apocarpae": "#2980b9", "Glumaceae": "#f1c40f"
    }

    order_descriptors = {
        "Ranales": "Many stamens, apocarpous carpels", "Parietales": "Parietal placentation",
        "Polygalyneae": "Irregular flowers, bilocular ovary", "Caryophylliniae": "Opposite leaves, free-central placentation",
        "Guttiferales": "Opposite leaves, numerous stamens", "Malvales": "Stellate hairs, monadelphous stamens",
        "Geraniales": "Ovary multi-locular, nectary disc present", "Olacales": "Disc cushion-like, superior ovary",
        "Celestrales": "Disc prominent, stamens alternate with petals", "Sapindales": "Compound leaves, disc prominent",
        "Rosales": "Perigynous/epigynous, stipulate leaves", "Myrtales": "Syncarpous, epigynous, aromatic",
        "Passiflorales": "Climbers, parietal placentation, tendrils", "Ficoidales": "Carpels fused, succulent habit",
        "Umbellales": "Flowers in umbels, inferior ovary", "Rubiales": "Opposite leaves, interpetiolar stipules",
        "Asterales": "Syngenesious anthers, head inflorescence", "Companales": "Anthers free or connate, inferior ovary",
        "Ericales": "Anthers open by pores, superior ovary", "Primulales": "Stamens opposite petals, free-central",
        "Ebenales": "Woody plants, superior ovary, stamens in whorls", "Gentianales": "Opposite leaves, superior bicarpellate ovary",
        "Polemoneales": "Alternate leaves, regular flowers", "Personales": "Zygomorphic, didynamous stamens",
        "Lamiales": "Zygomorphic, drupe/schizocarp, style terminal/gynobasic"
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

    for subcls in ["Polypetalae", "Gamopetalae", "Monochlamydeae"]:
        subcls_tree = dicot_tree.get(subcls, {})
        subcls_name, subcls_col, subcls_desc = subclass_headers[subcls]
        
        html += f"""                <!-- {subcls_name} CARD -->
                <details class="subclass-card" open style="border-color: {subcls_col};">
                    <summary class="subclass-header" style="background-color: {subcls_col};">
                        {subcls_name}
                        <div class="top-level-desc" style="font-size: 8px;">{subcls_desc}</div>
                    </summary>
                    
                    <div class="subclass-body">
"""
        for ser, orders in subcls_tree.items():
            tint_class = series_classes.get(ser, "")
            ser_desc_text = SERIES_DESCRIPTIONS.get(ser, "")
            
            if ser != "-":
                html += f"""                        <!-- SERIES {ser.upper()} -->
                        <details class="series-block {tint_class}" open>
                            <summary class="series-summary-header">
                                <span class="series-title-text">{ser.upper()}</span>
                                {f'<span class="series-desc-text">&mdash; {ser_desc_text}</span>' if ser_desc_text else ''}
                            </summary>
                            <div class="series-content">
"""
            # Monochlamydeae has only series, no orders. The Order key is '-'
            is_monochlamydeae = (subcls == "Monochlamydeae")
            
            if is_monochlamydeae:
                # Monochlamydeae: list families directly in the Series container
                html += """                                <div class="families-flex-container">
"""
                # Loop through all families in this series (which are under the Order '-' in tree)
                families = orders.get("-", [])
                for fam in families:
                    family_counter += 1
                    lookup_name = fam.replace(" [sic]", "").upper()
                    
                    is_syllabus = lookup_name in SYLLABUS_FAMILIES
                    desc = ALL_FAMILY_DESCRIPTIONS.get(lookup_name, "Bentham & Hooker plant family.")
                    
                    badge_class = "family-card-collapsible syllabus-highlight" if is_syllabus else "family-card-collapsible"
                    open_attr = " open" if is_syllabus else ""
                    
                    html += f"""                                        <details class="{badge_class}"{open_attr}>
                                            <summary>{family_counter}. {fam}</summary>
                                            <div class="family-desc-content">{desc}</div>
                                        </details>
"""
                html += """                                </div>
"""
            else:
                # Polypetalae & Gamopetalae: loop through Orders as normal
                for order, families in orders.items():
                    order_col = "#2c3e50"
                    if subcls == "Polypetalae":
                        order_col = poly_order_colors.get(order, "#2c3e50")
                    elif subcls == "Gamopetalae":
                        order_col = gamo_order_colors.get(order, "#2c3e50")

                    order_desc_text = order_descriptors.get(order, "")
                    
                    html += f"""                                <details class="order-row" open style="border-left: 3px solid {order_col};">
                                    <summary class="order-header-row">
                                        <div class="order-title" style="background-color: {order_col};">
                                            {order.upper()}
                                        </div>
                                        {f'<div class="order-desc">{order_desc_text}</div>' if order_desc_text else ''}
                                    </summary>
                                    <div class="families-flex-container">
"""
                    for fam in families:
                        family_counter += 1
                        lookup_name = fam.replace(" [sic]", "").upper()
                        
                        is_syllabus = lookup_name in SYLLABUS_FAMILIES
                        desc = ALL_FAMILY_DESCRIPTIONS.get(lookup_name, "Bentham & Hooker plant family.")
                        
                        badge_class = "family-card-collapsible syllabus-highlight" if is_syllabus else "family-card-collapsible"
                        open_attr = " open" if is_syllabus else ""
                        
                        html += f"""                                        <details class="{badge_class}"{open_attr}>
                                                <summary>{family_counter}. {fam}</summary>
                                                <div class="family-desc-content">{desc}</div>
                                            </details>
"""
                    html += """                                    </div>
                                </details>
"""
            if ser != "-":
                html += """                            </div>
                        </details>
"""
        html += """                    </div>
                </details>
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
    gymno_families = gymno_tree.get("-", {}).get("-", {}).get("-", [])
    gymno_colors = ["#3498db", "#2ecc71", "#e74c3c"]
    
    for idx, fam in enumerate(gymno_families):
        family_counter += 1
        col = gymno_colors[idx % len(gymno_colors)]
        lookup_name = fam.replace(" [sic]", "").upper()
        desc = ALL_FAMILY_DESCRIPTIONS.get(lookup_name, "Gymnosperm family.")
        
        html += f"""                <div class="gymno-card" style="border-left: 3px solid {col};">
                                    <details class="family-card-collapsible syllabus-highlight" open style="border-color: {col};">
                                        <summary style="color: {col}; font-weight:700;">{family_counter}. {fam}</summary>
                                        <div class="family-desc-content" style="border-top-color: {col}; color: #34495e;">{desc}</div>
                                    </details>
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
    mono_subclasses = mono_tree.get("-", {})
    for ser, orders in mono_subclasses.items():
        ser_col = mono_series_colors.get(ser, "#2c3e50")
        ser_desc = SERIES_DESCRIPTIONS.get(ser, "")
        
        html += f"""                <!-- SERIES {ser.upper()} -->
                <details class="mono-series-card" open style="border-left: 3px solid {ser_col};">
                    <summary class="mono-series-header">
                        <div class="mono-left-title" style="background-color: {ser_col};">
                            {ser.upper()}
                        </div>
                        {f'<div class="mono-series-desc">{ser_desc}</div>' if ser_desc else ''}
                    </summary>
                    <div class="families-flex-container">
"""
        families = orders.get("-", [])
        for fam in families:
            family_counter += 1
            lookup_name = fam.replace(" [sic]", "").upper()
            
            is_syllabus = lookup_name in SYLLABUS_FAMILIES
            desc = ALL_FAMILY_DESCRIPTIONS.get(lookup_name, "Monocot family.")
            
            badge_class = "family-card-collapsible syllabus-highlight" if is_syllabus else "family-card-collapsible"
            open_attr = " open" if is_syllabus else ""
            
            html += f"""                        <details class="{badge_class}"{open_attr}>
                                            <summary>{family_counter}. {fam}</summary>
                                            <div class="family-desc-content">{desc}</div>
                                        </details>
"""
        html += """                    </div>
                </details>
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
    
    print(f"Success! Generated {family_counter} families with collapsible groups, characters, and series descriptions.")

if __name__ == "__main__":
    generate_chart()
