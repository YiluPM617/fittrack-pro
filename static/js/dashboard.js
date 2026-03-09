const weightCtx = document.getElementById('weightChart');
if (weightCtx) {
    new Chart(weightCtx, {
        type: 'line',
        data: {
            labels: ['Mon', 'Tue', 'Wed', 'Thu', 'Fri'],
            datasets: [{
                label: 'Weight (kg)',
                data: [73.2, 73.0, 72.9, 72.7, 72.5]
            }]
        }
    });
}

const macroCtx = document.getElementById('macroChart');
if (macroCtx) {
    new Chart(macroCtx, {
        type: 'pie',
        data: {
            labels: ['Protein', 'Carbs', 'Fat'],
            datasets: [{
                data: [120, 180, 50]
            }]
        }
    });
}