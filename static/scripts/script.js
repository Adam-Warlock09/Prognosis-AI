let imgContainer = document.getElementById("img")
let mainContainer = document.getElementsByClassName("main-container")[0]
let headText = document.getElementsByClassName("head-text")[0]
let bodyContainer = document.getElementsByClassName("body-container")[0]
let textContainer = document.getElementsByClassName("text-container")[0]
let startBtn = document.getElementById("start-btn")
let formBackground = document.getElementsByClassName("form-background")[0]

imgContainer.addEventListener("click", () => {

    imgContainer.classList.add("fade-out")

    const imgTimeout = setTimeout(() => {

        imgContainer.classList.add("no-display")
        mainContainer.classList.toggle("no-display")

        headText.style.animation = "movement 1s";

        bodyContainer.style.animation = "fade-in 2s";

        clearTimeout(imgTimeout)

    }, 1000)

})

startBtn.addEventListener("click", ()=> {

    textContainer.classList.add("fade-out")

    const startTimeout = setTimeout(() => {

        textContainer.classList.add("no-display")

        formBackground.classList.toggle("no-display")

        formBackground.style.animation = "fade-in 2s";

        const alertTimeout = setTimeout(() => {
            alert("This is an unvalidated form. None Of your inputs are being checked. All numerical inputs are required. Form Validation feature will soon be added.")
            clearTimeout(alertTimeout)
        }, 1800);

        clearTimeout(startTimeout)

    }, 1000)

})