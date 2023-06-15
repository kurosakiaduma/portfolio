function handleProjectClick() {
    document.querySelector(".project-card").classList.add("active");
    document.querySelector(".biocard").classList.remove("active");
    document.querySelector(".skillscard").classList.remove("active");
    document.querySelector(".linkscard").classList.remove("active");
    document.querySelector(".buttons button:nth-child(1)").classList.add("active");
    document.querySelector(".buttons button:nth-child(2)").classList.remove("active");
    document.querySelector(".buttons button:nth-child(3)").classList.remove("active");
    document.querySelector(".buttons button:nth-child(4)").classList.remove("active");
}

function handleBioClick() {
    document.querySelector(".project-card").classList.remove("active");
    document.querySelector(".biocard").classList.add("active");
    document.querySelector(".skillscard").classList.remove("active");
    document.querySelector(".linkscard").classList.remove("active");
    document.querySelector(".buttons button:nth-child(1)").classList.remove("active");
    document.querySelector(".buttons button:nth-child(2)").classList.add("active");
    document.querySelector(".buttons button:nth-child(3)").classList.remove("active");
    document.querySelector(".buttons button:nth-child(3)").classList.remove("active");
}

function handleSkillsClick() {
    //Stylize the level lines before displaying them to the user
    const skills = document.querySelectorAll('.skill-level-line');
    skills.forEach(skill => {
        const level = skill.previousSibling.innerText;
        // Reset the bgColor and width of the skill level line for all skills
        skill.style.width = '0%';
        skill.style.backgroundColor = "";
    
        // Modify the skill level line based on the skill's level
        if (level === 'Proficient') {
            skill.style.width = '100%';
            skill.style.backgroundColor = "#32cd32";
        } else if (level === 'Advanced') {
            skill.style.width = '75%';
            skill.style.backgroundColor = "#00ff7f";
        } else if (level === 'Intermediate') {
            skill.style.width = '60%';
            skill.style.backgroundColor = "#ffa500";
        } else {
            skill.style.width = '45%';
            skill.style.backgroundColor = "#ffd700";
        }
        skill.previousSibling.style.display = "none";
        skill.style.marginBottom = "10%";
        });
    document.querySelector(".project-card").classList.remove("active");
    document.querySelector(".biocard").classList.remove("active");
    document.querySelector(".skillscard").classList.add("active");
    document.querySelector(".linkscard").classList.remove("active");
    document.querySelector(".buttons button:nth-child(1)").classList.remove("active");
    document.querySelector(".buttons button:nth-child(2)").classList.remove("active");
    document.querySelector(".buttons button:nth-child(3)").classList.add("active");
    document.querySelector(".buttons button:nth-child(4)").classList.remove("active");
}

function handleLinksClick() {
    document.querySelector(".project-card").classList.remove("active");
    document.querySelector(".biocard").classList.remove("active");
    document.querySelector(".skillscard").classList.remove("active");
    document.querySelector(".linkscard").classList.add("active");
    document.querySelector(".buttons button:nth-child(1)").classList.remove("active");
    document.querySelector(".buttons button:nth-child(2)").classList.remove("active");
    document.querySelector(".buttons button:nth-child(3)").classList.remove("active");
    document.querySelector(".buttons button:nth-child(4)").classList.add("active");
}

document.addEventListener("DOMContentLoaded", function() {

    // Set the initial content to Projects
    handleProjectClick();

});
  