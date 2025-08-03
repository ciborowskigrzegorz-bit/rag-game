document.addEventListener("DOMContentLoaded", () => {
    const bgMusic = document.getElementById("bg-music");
    const volumeSlider = document.getElementById("volume");
    const enemyBox = document.querySelector(".enemy-box");

    // Inicjalna głośność tła
    if (bgMusic && volumeSlider) {
        bgMusic.volume = volumeSlider.value;

        volumeSlider.addEventListener("input", () => {
            bgMusic.volume = volumeSlider.value;
        });
    }

    // Efekt drgania przeciwnika
    if (enemyBox) {
        enemyBox.classList.add("shake");
        setTimeout(() => {
            enemyBox.classList.remove("shake");
        }, 500);
    }

    // Odtwarzanie dźwięku trafienia
    const hitSound = new Audio("/static/hit.mp3");
    hitSound.play().catch((e) => {
        console.warn("Autoplay zablokowany przez przeglądarkę:", e);
    });
});

