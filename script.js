document.addEventListener('DOMContentLoaded', function () {
    // element-one: Dupla kattintásra hozzáad egy "animation" class-t kattintáskor
    const elementOne = document.getElementById('element-one');
    elementOne.addEventListener('dblclick', function() {
        elementOne.classList.add('animation');
    });

    // element-two: Ha rámegy az egér, hozzáad egy box-shadow-t
    const elementTwo = document.getElementById('element-two');
    elementTwo.addEventListener('mouseover', function() {
        elementTwo.style.boxShadow = '0 4px 8px rgba(0, 0, 0, 0.2)';
    });
    elementTwo.addEventListener('mouseout', function() {
        elementTwo.style.boxShadow = '';
    });

    // element-three: Kattintásra eltűnik
    const elementThree = document.getElementById('element-three');
    elementThree.addEventListener('click', function() {
        elementThree.style.display = 'none';
    });

    // element-four: Kattintásra a háttere zöld lesz
    const elementFour = document.getElementById('element-four');
    elementFour.addEventListener('click', function() {
        elementFour.style.backgroundColor = 'green';
    });
});