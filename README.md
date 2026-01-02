<div align="center">
  <img src="img/cvgue_logo_rounded.webp">
</div>


### Why the name CVGue?
CVGue is a portmanteau of "Curriculum Vitae" and "me" in Indonesian slang.


### Installation

```bash
pip install cvgue
```

### Available Templates

```python
| Template | Description |
| --- | --- |
| ATS | ATS-friendly CV template (optimized for applicant tracking systems) |
| Creative | Creative CV template (modern & visually expressive) |
```

### Usage

```python
from cvgue import create_cv


# Your Data
data = {
    "name": "your_name",
    "title": "your_title",
    "email": "your_email",
    "phone": "your_phone",
    "location": "your_location",
    "website": "your_website",
    "linkedin": "your_linkedin",
    "photo": "path_to_your_photo",
    
    "summary": "your_summary",
    
    "education": [
        {
            "degree": "your_degree",
            "institution": "your_institution",
            "period": "your_period",
            "location": "your_location",
            "gpa": "your_gpa"
        },
        {
            "degree": "your_degree",
            "institution": "your_institution",
            "period": "your_period",
            "location": "your_location",
            "gpa": "your_gpa"
        }
    ],
    
    "experience": [
        {
            "role": "your_role",
            "company": "your_company",
            "location": "your_location",
            "period": "your_period",
            "points": [
                "your_points",
                "your_points",
                "your_points",
                "your_points"
            ]
        },
        {
            "role": "your_role",
            "company": "your_company",
            "location": "your_location",
            "period": "your_period",
            "points": [
                "your_points",
                "your_points"
            ]
        },
        {
            "role": "your_role",
            "company": "your_company",
            "location": "your_location",
            "period": "your_period",
            "points": [
                "your_points"
            ]
        }
    ],
    
    "skills": {
        "hard": [
            "your_skills",
            "your_skills",
            "your_skills"
        ],
        "soft": [
            "your_skills",
            "your_skills",
            "your_skills"
        ]
    },
    
    "certifications": [
        "your_certifications",
        "your_certifications",
        "your_certifications"
    ],
    
    "languages": [
        "your_languages",
        "your_languages"
    ],
    
    "references": [
        {
            "name": "reference_name",
            "company": "reference_company",
            "position": "reference_position",
            "phone": "reference_phone",
            "email": "reference_email"
        },
        {
            "name": "reference_name",
            "company": "reference_company",
            "position": "reference_position",
            "phone": "reference_phone",
            "email": "reference_email"
        }
    ]
}

# Generate creative CV
create_cv(data, template_type="creative", output_path="cv_yourname_creative.pdf")
```


