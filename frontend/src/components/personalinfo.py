from reactpy import html, component

@component
def avatar():
    return html.div(
        {},
        html.div(
            {"class": "contact-icons"},
            html.a({"href": "https://www.linkedin.com/in/tevin_aduma", "target": "_blank"},html.i({"class": "fab fa-linkedin fa-2x","style": {"color": "#0077B5"}})),
            html.a({"href": "https://github.com/kurosakiaduma", "target": "_blank"},html.i({"class": "fab fa-github fa-2x","style": {"color": "#000000"}})),
            html.a({"href": "https://twitter.com/kurosakiaduma", "target": "_blank"},html.i({"class": "fab fa-twitter fa-2x","style": {"color": "#1da1f2"}})),
            html.a({"href": "https://www.reddit.com/user/kurosakiaduma", "target": "_blank"},html.i({"class": "fab fa-reddit fa-2x","style": {"color": "#ff4500"}})),
            html.a({"href": "mailto:tevin74@live.com", "target": "_blank"},html.i({"class": "far fa-envelope fa-2x", "style": {"color": "#0072c6"}})),
            html.a({"href": "https://www.linkedin.com/", "target": "_blank"},html.i({"class": "fab fa-discord fa-2x", "style": {"color": "#7289da"}})),
            ),
        html.hr({"style":{"color":"#d3c5c5"}}),
        html.h3("Hi 🙂, my name is"),
        html.h3("Tevin Joel Aduma 🧑🏾‍💻"),
        html.hr({"style":{"color":"#d3c5c5"}}),
        html.h4("Cloud Engineer ☁️| Software Engineer 💻"),
        html.h4("Machine Learning Engineer 🤖")
    )