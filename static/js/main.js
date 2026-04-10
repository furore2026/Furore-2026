document.querySelectorAll(".cluster-card").forEach((card) => {
    card.addEventListener("mousemove", (event) => {
        const rect = card.getBoundingClientRect();
        const x = event.clientX - rect.left;
        const y = event.clientY - rect.top;
        card.style.background = `radial-gradient(circle at ${x}px ${y}px, rgba(212,175,55,0.2), rgba(122,20,20,0.24) 35%, rgba(8,8,8,0.72) 70%)`;
    });

    card.addEventListener("mouseleave", () => {
        card.style.background = "linear-gradient(135deg, rgba(122, 20, 20, 0.2), rgba(8, 8, 8, 0.72))";
    });
});

const revealItems = document.querySelectorAll(".section, .cluster-card, .gallery-grid figure");
revealItems.forEach((item) => item.classList.add("reveal"));

const observer = new IntersectionObserver(
    (entries, obs) => {
        entries.forEach((entry) => {
            if (entry.isIntersecting) {
                entry.target.classList.add("is-visible");
                obs.unobserve(entry.target);
            }
        });
    },
    { threshold: 0.12, rootMargin: "0px 0px -20px 0px" }
);

revealItems.forEach((item) => observer.observe(item));
