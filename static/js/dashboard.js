const weightCtx = document.getElementById('weightChart');
if (weightCtx) {
    new Chart(weightCtx, {
        type: 'line',
        data: {
            labels: typeof weightLabels !== 'undefined' ? weightLabels : [],
            datasets: [{
                label: 'Weight (kg)',
                data: typeof weightData !== 'undefined' ? weightData : [],
                tension: 0.3,
                fill: false,
                pointRadius: 5,
                pointHoverRadius: 8,
                pointHitRadius: 12
            }]
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,
            interaction: {
                mode: 'nearest',
                intersect: true
            },
            plugins: {
                tooltip: {
                    enabled: true,
                    callbacks: {
                        label: function(context) {
                            return `Weight: ${context.raw} kg`;
                        }
                    }
                }
            }
        }
    });
}

const calorieCtx = document.getElementById('calorieChart');
if (calorieCtx) {
    new Chart(calorieCtx, {
        type: 'bar',
        data: {
            labels: ['Calories In', 'Calories Out', 'Net Calories'],
            datasets: [{
                label: 'Calories',
                data: [caloriesIn, caloriesOut, netCalories]
            }]
        },
        options: {
            responsive: true,
            maintainAspectRatio: false
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
                data: [protein, carbs, fat]
            }]
        },
        options: {
            responsive: true,
            maintainAspectRatio: true
        }
    });
}