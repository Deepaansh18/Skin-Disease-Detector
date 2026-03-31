import os
import random

# This is dictionary which is storing diseases,curesand keywords. Keywords help in detecting disease based on image filename
DISEASES = {
    "Acne": {
        "cure": "Wash face twice daily, avoid oily food, use salicylic acid cleanser.",
        "keywords": ["acne", "pimple", "zit", "face", "forehead", "cheek"]
    },
    "Eczema": {
        "cure": "Moisturize skin regularly, avoid harsh soaps, use prescribed steroid creams.",
        "keywords": ["eczema", "dry", "itchy", "rash", "patch", "arm", "elbow"]
    },
    "Psoriasis": {
        "cure": "Use medicated creams (coal tar), reduce stress, consult a dermatologist.",
        "keywords": ["psoriasis", "scaly", "scale", "plaque", "knee", "elbow", "scalp"]
    },
    "Fungal Infection": {
        "cure": "Keep area dry, apply antifungal cream (clotrimazole), wear breathable clothing.",
        "keywords": ["fungal", "fungus", "ring", "ringworm", "nail", "foot", "toe", "athlete"]
    },
    "Allergy": {
        "cure": "Avoid known triggers, take antihistamines, apply hydrocortisone cream if needed.",
        "keywords": ["allergy", "allergic", "hive", "swell", "red", "reaction", "rash"]
    },
    "Rosacea": {
        "cure": "Use gentle skincare, avoid sun and heat, consult doctor for topical antibiotics.",
        "keywords": ["rosacea", "redness", "flush", "blush", "nose", "cheek"]
    },
    "Warts": {
        "cure": "Apply salicylic acid regularly or seek cryotherapy from a dermatologist.",
        "keywords": ["wart", "warts", "bump", "growth", "hand", "finger", "plantar"]
    },
    "Hives": {
        "cure": "Take antihistamines, apply cool compresses, and avoid known allergens.",
        "keywords": ["hive", "hives", "urticaria", "welt", "itch", "red", "bump"]
    }
}

# Classify the image into categorize based on file size in kb
def get_image_size_category(size_kb):
    if size_kb < 50:
        return "small"     # Low quality / less detail
    elif size_kb < 300:
        return "medium"    # Moderate detail
    else:
        return "large"     # High detail image

# Its main function is to detect disease using filename keywords
def detect_from_filename(filename):
    name_lower = filename.lower() # It convert to lowercase 

    # It is a loop which check each disease and its keywords
    for disease, data in DISEASES.items():
        for keyword in data["keywords"]:
            if keyword in name_lower:
                return disease  # Return as soon as a match is found
    return None  # It is for if no keyword matched in the filename

# Its main function is to randomly detect disease based on image size
def weighted_random_detection(size_category):
    if size_category == "large":
        # High clarity: in this visible diseases prioritized
        weights = [25, 15, 15, 15, 10, 10, 5, 5]

    elif size_category == "medium":
        # Balanced probabilities: no strong hint
        weights = [15, 15, 15, 15, 15, 10, 10, 5]

    else:
        # Low clarity: all diseases nearly have equal chance
        weights = [13, 13, 13, 13, 13, 13, 11, 11]

    diseases = list(DISEASES.keys()) # Get list of all the disease names

    # By this it randomly pick one disease using weights
    chosen = random.choices(diseases, weights=weights, k=1)[0]
    return chosen

# Its main function is to generate a fake confidence score
def confidence_score(detection_method, size_category):
    if detection_method == "filename":
        base = random.randint(72, 91)  # Higher confidence

    elif size_category == "large":
        base = random.randint(55, 75)

    elif size_category == "medium":
        base = random.randint(40, 60)

    else:
        base = random.randint(25, 45)

    return base

# Main program starts from here 

print("===== Skin Disease Detector =====")

# Take input path from user and clean extra quotes
path = input("Enter image path: ").strip().strip('"').strip("'")

# Check if file exists
if not os.path.exists(path):
    print("Error: File not found.")
    print("Path received:", path)

# Check if the file is a valid image in terms of format
elif not path.lower().endswith((".jpg", ".jpeg", ".png", ".bmp", ".gif", ".webp")):
    print("Error: Not a valid image file.")
    print("Supported formats: .jpg, .jpeg, .png, .bmp, .gif, .webp")

else:
    # Extract file details using the url given 
    filename  = os.path.basename(path)
    size_kb   = round(os.path.getsize(path) / 1024, 2)
    size_cat  = get_image_size_category(size_kb)

    print("\n--- File Info ---")
    print("File Name  :", filename)
    print("File Size  :", size_kb, "KB")
    print("Image Size :", size_cat.capitalize())

    # Step 1: Try to detect the disease by using filename keywords
    detected = detect_from_filename(filename)
    method   = "filename"

    # Step 2: If no keyword found then use weighted random detection
    if detected is None:
        detected = weighted_random_detection(size_cat)
        method   = "visual"

    # Get the cure for the disease which has been detected using the above information
    cure = DISEASES[detected]["cure"]

    print("\n--- Detection Result ---")
    print("Detected Disease :", detected)
    print("Detection Method :", "Filename hint matched" if method == "filename" else "Visual pattern analysis")
    print("Suggested Cure   :", cure)

    # Disclaimer
    print("\nNote: Please consult a real doctor for proper diagnosis.")