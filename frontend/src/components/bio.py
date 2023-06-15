from reactpy import html, component

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

