function handleProjectClick() {
    document.querySelector(".project-card").classList.add("active");
    document.querySelector(".biocard").classList.remove("active");
    document.querySelector(".linkscard").classList.remove("active");
    document.querySelector(".buttons button:nth-child(1)").classList.add("active");
    document.querySelector(".buttons button:nth-child(2)").classList.remove("active");
    document.querySelector(".buttons button:nth-child(3)").classList.remove("active");
}

function handleBioClick() {
    document.querySelector(".project-card").classList.remove("active");
    document.querySelector(".biocard").classList.add("active");
    document.querySelector(".linkscard").classList.remove("active");
    document.querySelector(".buttons button:nth-child(1)").classList.remove("active");
    document.querySelector(".buttons button:nth-child(2)").classList.add("active");
    document.querySelector(".buttons button:nth-child(3)").classList.remove("active");
}

function handleLinksClick() {
    document.querySelector(".project-card").classList.remove("active");
    document.querySelector(".biocard").classList.remove("active");
    document.querySelector(".linkscard").classList.add("active");
    document.querySelector(".buttons button:nth-child(1)").classList.remove("active");
    document.querySelector(".buttons button:nth-child(2)").classList.remove("active");
    document.querySelector(".buttons button:nth-child(3)").classList.add("active");
}
document.addEventListener("DOMContentLoaded", function() {
    // Set the initial content to Projects
    handleProjectClick();
});