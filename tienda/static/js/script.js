document.addEventListener("DOMContentLoaded", function() {
    const btn = document.getElementById("theme-toggle-btn");
    const icon = document.getElementById("theme-icon");
    const html = document.documentElement;

    // --- LÓGICA DE TEMA (DARK/LIGHT) ---
    function updateUI(theme) {
        html.setAttribute("data-bs-theme", theme);
        if (theme === "dark") {
            icon.className = "bi bi-sun-fill fs-5";
            btn.classList.replace("btn-outline-primary", "btn-warning");
        } else {
            icon.className = "bi bi-moon-stars-fill fs-5";
            btn.classList.replace("btn-warning", "btn-outline-primary");
        }
    }

    const savedTheme = localStorage.getItem("theme") || "light";
    updateUI(savedTheme);

    btn.addEventListener("click", function() {
        const newTheme = html.getAttribute("data-bs-theme") === "light" ? "dark" : "light";
        localStorage.setItem("theme", newTheme);
        updateUI(newTheme);
    });

    // --- LÓGICA DE SCROLL (MOSTRAR/OCULTAR) ---
    let lastScrollY = window.scrollY;
    let timer = null;

    window.addEventListener("scroll", function() {
        const currentScrollY = window.scrollY;

        if (currentScrollY > lastScrollY) {
            // Bajando: Ocultar inmediatamente
            ocultarBoton();
        } else {
            // Subiendo: Mostrar y resetear temporizador
            mostrarBoton();
            
            // Limpiar temporizador anterior
            if (timer) clearTimeout(timer);
            
            // Iniciar nuevo temporizador de 2 segundos
            timer = setTimeout(() => {
                ocultarBoton();
            }, 2000);
        }
        
        lastScrollY = currentScrollY;
    });

    function mostrarBoton() {
        btn.style.opacity = "1";
        btn.style.visibility = "visible";
        btn.style.transform = "translateY(0)";
    }

    function ocultarBoton() {
        btn.style.opacity = "0";
        btn.style.visibility = "hidden";
        btn.style.transform = "translateY(-20px)"; // Efecto de desplazamiento hacia arriba al desaparecer
    }
});