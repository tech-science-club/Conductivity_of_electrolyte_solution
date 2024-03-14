<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Conductivity</title>
    <link rel="stylesheet" href="style.css"> <!-- Link to external CSS file -->
    <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
</head>

<body>
 		<h1>Conductivity</h1> <!-- Title "Conductivity" -->       
    
       
        <table class="summary-table"> <!-- Table for summary -->
            <tr>
                <th>Statistic</th>
                <th>Sec</th>
                <th>λ, 1/R</th>
            </tr>
            <tr>
                <td>Highest Value</td>
                <td id="highest-x-axis"></td>
                <td id="highest-value"></td>
            </tr>
            <tr>
                <td>Lowest Value</td>
                <td id="lowest-x-axis"></td>
                <td id="lowest-value"></td>
            </tr>
            <tr>
                <td>Time</td>
                <td id="duration"></td>
                <td id="lowest-value"></td>
            </tr>
        </table>
            
        
    
    <div class="chart-container"> <!-- Container for the chart -->
            <canvas id="myChart"></canvas>
    </div>
    <script src="script.js"></script> <!-- Link to external JavaScript file -->
    <button id="downloadBtn">Download Chart</button>
    
    
</body>
</html>
