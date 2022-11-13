thumbsupClick=(icon)=>{
    icon.classList.toggle('fa bi bi-hand-thumbs-up-fill')
}
let noOfCharacter=20;
let contents = document.querySelectorAll(".article-content")
contents.forEach(content => {
    if(content.textContent.length < noOfCharacter){
        content.nextElementSibling.style.display="none"
    }
    else{
        let displayText = content.textContent.slice(0,noOfCharacter)
        let moreText = content.textContent.slice(noOfCharacter)
        content.innerHTML = `${displayText} <span class='dots'>...</span><span
        class="hide more">${moreText}</span>`
    }
});
function readMore(btn){
    let post = btn.parentElement;
    post.querySelector(".dots").classList.toggle("hide")
    post.querySelector(".more").classList.toggle("hide")
    btn.textContent == "Read More" ? btn.textContent= "Read Less"
    : btn.textContent="Read More"
}

