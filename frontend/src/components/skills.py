from reactpy import html, component

@component
def Skills():
    skills = [
        {"name": "Python", "id": "py", "level": "Proficient"},
        {"name": "Machine Learning", "id": "ml","level": "Advanced"},
        {"name": "Web (HTML5/CSS3/ReactJS)", "id": "web", "level": "Advanced"},
        {"name": "GCP/Azure", "id": "cloud", "level": "Advanced"},
        {"name": "Linux", "id": "linux", "level": "Advanced"},
        {"name": "SQL", "id": "sql", "level": "Intermediate"},
        {"name": "Critical Thinking", "id": "critical", "level": "Advanced"},
        {"name": "Communication", "id": "communication", "level": "Intermediate"},
    ]

    slider = html.div(
        {"class": "skills-slider"},
        html.div(
            {"class": "slider"},
            *[html.div(
                {"class": "skill"},
                html.div(
                    {"class": "skill-name"},
                    skill["name"]
                ),
                html.div(
                    {"class": "skill-level"},
                    skill["level"]
                ),
                html.div(
                    {"class": "skill-level-line", "id": skill["id"]},
                ),
            ) for skill in skills]
        )
    )
    
    return html.div(
        {"class": "skillscard"},
        slider,
    )
