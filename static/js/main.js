// البيانات تأتي الآن من Flask عبر /api/capitals
let capitals = [];

function createCapitalCard(capital) {
    return `
        <div class="capital-card">
            <img src="${capital.image}" alt="${capital.capital}" class="capital-image">
            <div class="capital-info">
                <h2 class="capital-name">${capital.capital}</h2>
                <p class="country-name">${capital.country}</p>
                <div class="temperature">${capital.temperature}°C</div>
            </div>
        </div>
    `;
}

function displayCapitals(capitalsArray) {
    const container = document.getElementById('capitalsContainer');
    container.innerHTML = capitalsArray
        .map(capital => createCapitalCard(capital))
        .join('');
}

function setupSearch() {
    const searchInput = document.getElementById('searchInput');
    searchInput.addEventListener('input', (e) => {
        const searchTerm = e.target.value.trim().toLowerCase();
        const filteredCapitals = capitals.filter(capital =>
            capital.capital.toLowerCase().includes(searchTerm) ||
            capital.country.toLowerCase().includes(searchTerm)
        );
        displayCapitals(filteredCapitals);
    });
}

async function loadCapitals() {
    try {
        const response = await fetch('/api/capitals');
        capitals = await response.json();
        displayCapitals(capitals);
    } catch (error) {
        console.error('Failed to load capitals:', error);
    }
}

document.addEventListener('DOMContentLoaded', () => {
    loadCapitals();
    setupSearch();
});
