function contactUsButtonClick() {
    var contactUsButton = document.getElementById('contact-us-button');
    contactUsButton.classList.toggle("active");
    var content = contactUsButton.nextElementSibling;
    if (content.style.maxHeight) {
        content.style.maxHeight = null;
    } else {
        content.style.maxHeight = content.scrollHeight + "px";
    }
}