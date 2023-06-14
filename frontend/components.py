from django.shortcuts import render
from reactpy import *

@component
def PersonalInfo():
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
        html.h2("Tevin Joel Aduma"),
        html.h4("Cloud Engineer| Software Engineer | Machine Learning Engineer"),
    )

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
    
@component
def Bio():
    return html.div(
        {"class": "biocard"},
        html.p("Hi👋🏾, I'm Tevin, a passionate Computer Science undergraduate with a deep love for technology and its potential to transform the world. I'm captivated by the enchanting melodies of lofi, jazz, and instrumental 🎶, which often accompany my coding adventures."),
        html.p("My curiosity extends beyond software development, as I am also fascinated by the realm of machine learning and its applications. I believe that through the power of data and intelligent algorithms, we can unlock innovative solutions to complex problems."),
        html.p("When I'm not immersed in the world of technology, you can find me on the football pitch ⚽, where I enjoy the camaraderie and competition 💪🏾. Cooking is another creative outlet I indulge in, experimenting with flavors and techniques to create delightful culinary experiences. Anime and gaming scenes also are also where I can unwind and explore virtual worlds, allowing me to embrace new perspectives and narratives."),
        html.p({"style": {"font-weight": "bold"}}, "One core belief that guides me is the importance of empathy. I truly believe that a more empathetic world can lead to positive change and foster understanding among individuals 🫱🏾‍🫲🏼"),
        html.p("Combining my technical expertise with a passion for business strategy, I am driven to explore the intersection of MLOps and web development. By leveraging data-driven insights and efficient operational practices, I aim to help businesses thrive and make a meaningful impact. Join me on this exciting journey as we harness the power of technology, empathy, and innovation to shape a brighter future 🌟"),
        )

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