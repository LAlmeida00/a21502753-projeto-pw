document.addEventListener('DOMContentLoaded', function() {
    fetch('https://a21502753.pythonanywhere.com/meteo/api/weather/today/Lisboa/')
        .then(response => response.json())
        .then(data => {
            const weatherData = data.data;
            const weatherContainer = document.getElementById('weather-container');
            weatherContainer.innerHTML = `
                <div>
                    <strong>Tempo: </strong>${weatherData.city}<strong> - </strong><img src="${weatherData.icon_url}" style="width:4ch"><strong> - </strong>${weatherData.weather}
                </div>
            `;
        })
        .catch(error => {
            console.error('Error fetching weather data:', error);
        });
});

// Função para ativar/desativar o modo escuro
function toggleDarkMode() {
    // Alternar a classe 'dark-mode' no corpo do documento
    document.body.classList.toggle('dark-mode');
}

// Adiciona um ouvinte de eventos para o botão de alternância
document.getElementById('darkModeToggle').addEventListener('click', toggleDarkMode);

// Função para atualizar a data e hora
function updateDateTime() {
            var now = new Date();
            var datetimeElement = document.getElementById('datetime');
            datetimeElement.textContent = now.toLocaleString('pt', { weekday: 'long', year: 'numeric', month: 'long', day: 'numeric', hour: 'numeric', minute: 'numeric', second: 'numeric' });
        }

        // Chama a função updateDateTime a cada segundo
        setInterval(updateDateTime, 1000);