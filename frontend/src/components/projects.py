from reactpy import html, component

@component
def ProjectsList(projects: dict):
    project_elements = []
    for name, details in projects.items():
        if details["Deployment"]!="#":
            project_elements.append(
                html.div(
                    {"class": "project"},
                    [
                        html.h4(name),
                        html.p(details["Desc"]),
                        html.p(
                            {"class": "project-links"},
                            html.a({"href": details["Github"], "target": "_blank"}, html.i({"class": "fab fa-github fa-2x","style": {"color": "black"}}),"Github Repo"),
                            html.a({"href": details["Deployment"], "target": "_blank"}, html.i({"class": "fas fa-rocket fa-2x", "style": {"color":"#ff4500"}}),"Deployment"),
                        )
                    ],
                )
            )
        else:
            project_elements.append(
                html.div(
                    {"class": "project"},
                    [
                        html.h4(name),
                        html.p(details["Desc"]),
                        html.p(
                            {"class": "project-links"},
                            html.a({"href": details["Github"], "target": "_blank"}, html.i({"class": "fab fa-github fa-2x","style": {"color": "black"}}),"Github Repo"),
                        )
                    ],
                )
            )
            
    return html.div(
        {"class": "project-card"},
        project_elements
        )