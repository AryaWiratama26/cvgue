import pytest
import os
import sys


sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from cvgue.engine import create_cv, TEMPLATE_DIR

# Sample Data Creative
DATA_CREATIVE = {
    "name": "Budi Santoso",
    "title": "Software Engineer",
    "email": "budi.santoso@email.com",
    "phone": "+62 812-3456-7890",
    "location": "Jakarta Selatan",
    "website": "budisantoso.dev",
    "linkedin": "linkedin.com/in/budisantoso",
    "photo": "/home/codemax/Documents/Project/cvgue/dummy-image.jpeg",
    "summary": "Software Engineer dengan 3+ tahun pengalaman dalam pengembangan web aplikasi menggunakan Python dan JavaScript. Passionate dalam clean code dan scalable architecture.",
    "education": [
        {
            "degree": "S1 Teknik Informatika",
            "institution": "Universitas Indonesia",
            "period": "2017 - 2021",
            "location": "Depok",
            "gpa": "3.65",
        }
    ],
    "experience": [
        {
            "role": "Backend Developer",
            "company": "PT Startup Tech",
            "location": "Jakarta",
            "period": "Jan 2022 - Sekarang",
            "points": [
                "Mengembangkan RESTful API menggunakan Django dan FastAPI",
                "Meningkatkan performa aplikasi hingga 40% melalui optimasi database",
                "Implementasi CI/CD pipeline dengan GitLab",
            ],
        },
        {
            "role": "Junior Developer",
            "company": "PT Software House",
            "location": "Jakarta",
            "period": "Jul 2021 - Dec 2021",
            "points": [
                "Membuat fitur e-commerce dengan Django",
                "Kolaborasi dengan tim frontend untuk integrasi API",
            ],
        },
    ],
    "skills": {
        "hard": [
            "Python (Django, FastAPI)",
            "JavaScript (Node.js, React)",
            "PostgreSQL & MySQL",
            "Git & Docker",
            "REST API Design",
        ],
        "soft": ["Problem Solving", "Team Collaboration", "Time Management"],
    },
    "certifications": [
        "AWS Certified Developer Associate",
        "Python Professional Certificate",
    ],
    "languages": ["Bahasa Indonesia (Native)", "English (Professional)"],
    "references": [
        {
            "name": "John Doe",
            "company": "PT Startup Tech",
            "position": "Tech Lead",
            "phone": "+62 811-1111-2222",
            "email": "john.doe@startup.com",
        }
    ],
}


# Samplee Data ATS
SAMPLE_CV_DATA = {
    "name": "Abdul Rozak",
    "email": "abdur.rozak@gmail.com",
    "phone": "+62 812 3456 7890",
    "location": "Jakarta, Indonesia",
    "linkedin": "linkedin.com/in/abdurrozak",
    "website": "abdurrozak.com",
    "summary": "Software developer with 5 years of experience in web and mobile application development.",
    "education": [
        {
            "degree": "S1 Teknik Informatika",
            "institution": "Universitas Indonesia",
            "location": "Depok",
            "period": "2015 - 2019",
            "gpa": "3.75",
        }
    ],
    "experience": [
        {
            "role": "Senior Developer",
            "company": "PT. Rawiw",
            "location": "Jakarta",
            "period": "2020 - Present",
            "points": [
                "Developing web and mobile applications.",
                "Leading a team of 5 developers.",
            ],
        }
    ],
    "organizations": [
        {
            "role": "Ketua",
            "organization": "Universitas Indonesia",
            "location": "Depok",
            "period": "2015 - 2019",
            "points": ["Managing 100+ active members."],
        }
    ],
    "projects": [
        {
            "title": "E-Commerce Platform",
            "stack": "Python, Django, PostgreSQL",
            "date": "2023",
            "points": ["Building e-commerce platform with 10K+ users."],
        }
    ],
    "skills": {
        "hard": ["Python", "JavaScript", "SQL", "Django", "React"],
        "soft": ["Leadership", "Communication", "Problem Solving"],
    },
    "certifications": ["AWS Certified Developer", "Google Cloud Professional"],
    "languages": ["Indonesian (Native)", "English (Fluent)"],
}


class TestTemplateDirectory:

    # Test template directory
    def test_template_dir_exists(self):
        assert os.path.exists(
            TEMPLATE_DIR
        ), f"Template directory not found: {TEMPLATE_DIR}"

    def test_ats_template_exists(self):

        # Test template ATS
        ats_path = os.path.join(TEMPLATE_DIR, "ats")
        assert os.path.exists(ats_path), "Template ATS not found"

        # Test template HTMLL
        template_html = os.path.join(ats_path, "template.html")
        styles_css = os.path.join(ats_path, "styles.css")

        # Test templates.html and styles.css
        assert os.path.exists(template_html), "template.html not found in ATS"
        assert os.path.exists(styles_css), "styles.css not found in ATS"


class TestCreateCV:

    def test_create_cv_default_template(self, tmp_path):
        output_file = tmp_path / "test_cv_cvgue.pdf"

        create_cv(data=SAMPLE_CV_DATA, output_path=str(output_file))

        assert output_file.exists(), "File PDF not created"
        assert output_file.stat().st_size > 0, "File PDF is empty"

    def test_create_cv_ats_template(self, tmp_path):
        output_file = tmp_path / "cv_ats_cvgue.pdf"

        create_cv(
            data=SAMPLE_CV_DATA, template_type="ats", output_path=str(output_file)
        )

        assert output_file.exists(), "File PDF ATS not created"

    def test_create_cv_creative_template(self, tmp_path):
        output_file = tmp_path / "cv_creative_cvgue.pdf"

        create_cv(
            data=DATA_CREATIVE, template_type="creative", output_path=str(output_file)
        )

        assert output_file.exists(), "File PDF Creative not created"

    def test_create_cv_with_minimal_data(self, tmp_path):
        output_file = tmp_path / "cv_minimal_cvgue.pdf"

        minimal_data = {
            "name": "Test User",
            "email": "",
            "phone": "",
            "location": "",
            "linkedin": "",
            "website": "",
            "summary": "",
            "education": [],
            "experience": [],
            "organizations": [],
            "projects": [],
            "skills": {"hard": [], "soft": []},
            "certifications": [],
            "languages": [],
        }

        create_cv(data=minimal_data, output_path=str(output_file))

        assert output_file.exists(), "File PDF not created with minimal data"

    def test_create_cv_invalid_template_raises_error(self, tmp_path):
        output_file = tmp_path / "cv_invalid_cvgue.pdf"

        with pytest.raises(Exception):
            create_cv(
                data=SAMPLE_CV_DATA,
                template_type="invalid_template",
                output_path=str(output_file),
            )


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
