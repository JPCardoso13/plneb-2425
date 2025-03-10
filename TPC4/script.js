document.addEventListener("DOMContentLoaded", () => {
    handleSiuCounter();
    handleResetBtn();
});

// Event Listener para incrementação do contador
function handleSiuCounter() {
    const audio = document.getElementById("audio-siu");
    const playText = document.getElementById("play-audio-siu");
    const counter = document.getElementById("siu-counter");

    playText.style.cursor = "pointer";

    playText.addEventListener("click", () => {
        audio.play();
        counter.textContent = parseInt(counter.textContent) + 1;
    });
}

// Event Listener para reinício do contador
function handleResetBtn() {
    const resetBtn = document.getElementById("siu-reset-btn");
    const counter = document.getElementById("siu-counter");

    resetBtn.addEventListener("click", () => {
        counter.textContent = 0;
    });
}
