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
});
