function createBurst(){
    const animContainer = document.querySelector('.animation-container');
    const burst = document.querySelector('.burst');
    const lines = document.querySelectorAll('.line');

    burst.style.top = Math.random() * innerHeight + 'px';
    burst.style.left = Math.random() * innerWidth + 'px';

    lines.forEach((line) => {
        const colors = ['#es4335', '#34a853', '#4285f4', '#fbbc05', '#dc18b9', '#fff5a00', '#8621f8', '#ffff1b'];
        const randomColor = colors[Math.floor(Math.random() * colors.length)];
        line.style.background = randomColor;
    });

    const burstClone = burst.cloneNode(true);
    animContainer.appendChild(burstClone);

    setTimeout(() => {
        burstClone.remove();
    }, 8000);
}
setInterval(createBurst, 500);