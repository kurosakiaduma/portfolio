from reactpy import component, html

@component
def Resources(resources: dict):
    resources_elements = []
    for name, details in resources.items():
        resources_elements.append(
            html.div(
                {"class": "resource-link"},
                [
                    html.a({"href": details["link"], "target": "_blank"}, html.i({"class": "fas fa-robot fa-1x","style": {"color": "black"}}),name),
                ],
            )
        )
    return html.div(
        {"class": "linkscard"},
        resources_elements
        )