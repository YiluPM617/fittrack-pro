const weightCtx = document.getElementById('weightChart');
if (weightCtx) {
    new Chart(weightCtx, {
        type: 'line',
        data: {
            labels: typeof weightLabels !== 'undefined' ? weightLabels : [],
            datasets: [{
                label: 'Weight (kg)',
                data: typeof weightData !== 'undefined' ? weightData : [],
                tension: 0.3
            }]
        },
        options: {
            responsive: true,
            maintainAspectRatio: true
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
        },
        options: {
            responsive: true,
            maintainAspectRatio: true
        }
    });
}