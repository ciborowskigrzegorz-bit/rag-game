document.addEventListener("DOMContentLoaded", () => {
    const bgMusic = document.getElementById("bg-music");
    const volumeSlider = document.getElementById("volume");

    // Inicjalna głośność
    bgMusic.volume = volumeSlider.value;

    // Obsługa zmiany głośności
    volumeSlider.addEventListener("input", () => {
        bgMusic.volume = volumeSlider.value;
    });

    // Prosty efekt animacji co atak
    const enemyBox = document.querySelector(".enemy-box");
    if (enemyBox) {
        enemyBox.classList.add("shake");
        setTimeout(() => {
            enemyBox.classList.remove("shake");
        }, 500);
    }
    document.addEventListener("DOMContentLoaded", () => {
    const enemyBox = document.querySelector(".enemy-box");

    // Efekt drgania
    if (enemyBox) {
        enemyBox.classList.add("shake");

        setTimeout(() => {
            enemyBox.classList.remove("shake");
        }, 500);
    }

    // Odtwarzanie dźwięku
    const hitSound = new Audio("/static/hit.mp3");
    hitSound.play().catch((e) => {
        console.warn("Autoplay zablokowany przez przeglądarkę:", e);
    });
});

});
