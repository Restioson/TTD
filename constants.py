BUDGET = 5000
TREATMENT_COST = 500
PATIENTS_PER_DAY = 15
HOSPITAL_BONUS = 25

# Tuple list of name, chance (1 in x), and survival impact
SYMPTOMS = (

    ("coughing", 0.2, 1),
    ("vomiting blood", 0.05, 15),
    ("amnesia", 0.05, 15),
    ("loss of apetite", 0.2, 3),
    ("sneezing", 0.2, 1),
    ("infection", 0.2, 10),
    ("kidney failure", 0.05, 40),
    ("liver failure", 0.05, 40)

)

SYMPTOMS_INDEXES = {
    "coughing": 0,
    "vomiting blood": 1,
    "amnesia": 2,
    "loss of apetite": 3,
    "sneezing": 4,
    "infection": 5,
    "kidney failure": 6,
    "liver failure": 7
}
