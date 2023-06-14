from django.shortcuts import render
from reactpy import *

@component
def PersonalInfo():
    return html.div(
        {},
        html.div(
            html.a({"href": "https://www.linkedin.com/in/tevin_aduma", "target": "_blank"},html.i({"class": "fab fa-linkedin fa-2x"})),
            html.a({"href": "https://github.com/kurosakiaduma", "target": "_blank"},html.i({"class": "fab fa-github fa-2x"})),
            html.a({"href": "https://twitter.com/kurosakiaduma", "target": "_blank"},html.i({"class": "fab fa-twitter fa-2x"})),
            html.a({"href": "https://www.reddit.com/user/kurosakiaduma", "target": "_blank"},html.i({"class": "fab fa-reddit fa-2x"})),
            html.a({"href": "https://www.linkedin.com/", "target": "_blank"},html.i({"class": "fab fa-mail fa-2x fa-orange"})),
            ),
        html.h1("Tevin Joel Aduma"),
        html.p("Cloud Engineer| Software Engineer | Machine Learning Engineer"),
        html.p("Contact: kurosakiaduma@gmail.com"),
    )

@component
def ProjectsList(projects: dict):
    project_elements = []
    for name, details in projects.items():
        project_elements.append(
            html.div(
                {"class": "project"},
                [
                    html.h4(name),
                    html.p(details["Desc"]),
                    html.p(
                        {"class": "project-links"},
                        html.a({"href": details["Github"], "target": "_blank"}, "Github"),
                        html.a({"href": details["Deployment"], "target": "_blank"}, "Deployment"),
                    )
                ],
            )
        )
    return html.div(
        {"class": "project-card"},
        project_elements
        )
    
@component
def Bio():
    return html.div(
        {"class": "biocard"},
        html.p("I am a Computer Science undergraduate with a passion for technology and its potential to transform the world.\
            I love listening to lofi, jazz, and instrumental music while diving into coding adventures.\
                My interests also extend to machine learning, soccer, cooking, and gaming.\
                    I strongly believe that empathy can make the\
          world a better place. I'm dedicated to driving business strategy through MLOps and the web,\
          exploring innovative ways to make a positive impact."),
        )

@component
def Resources(resources: dict):
    resources_elements = []
    for name, details in resources.items():
        resources_elements.append(
            html.div(
                {"class": "link"},
                [
                    html.a({"href": details, "target": "_blank"}, name),
                ],
            )
        )
    return html.div(
        {"class": "linkscard"},
        resources_elements
        )