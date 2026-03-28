AOS.init();

// Typing animation
new Typed("#typing", {
    strings: ["AI Developer 🤖", "Data Analyst 📊", "Flask Developer 💻"],
    typeSpeed: 50,
    loop: true
});

// ML Form
document.getElementById("mlForm").addEventListener("submit", function(e) {
    e.preventDefault();

    let input = document.getElementById("inputData").value;

    fetch('/predict', {
        method: 'POST',
        body: new URLSearchParams({input: input})
    })
    .then(res => res.text())
    .then(data => {
        let result = document.getElementById("result");

        result.innerHTML = "Prediction: " + data;

        result.style.opacity = 0;
        setTimeout(() => {
            result.style.opacity = 1;
            result.style.transition = "1s";
        }, 100);
    });
});

// Particle animation (AI-controlled)
let theme = document.body.className;

particlesJS("particles-js", {
  particles: {
    number: {
      value: theme === "neon" ? 120 : 60
    },
    color: {
      value: theme === "dark" ? "#ffffff" : "#00f7ff"
    },
    move: {
      speed: theme === "neon" ? 4 : 1
    }
  }
});