fetch('data.txt')
    .then(response => response.json())
    .then(data => {
        const ctx = document.getElementById('myChart').getContext('2d');

        const xAxesData = data.x_axes;
        const yAxesData = data.y_axes;
		
        let myChart = new Chart(ctx, {
            type: 'line',
            data: {
                labels: xAxesData,
                datasets: [{
                    label: 'Conductivity',
                    data: yAxesData,
                    borderColor: 'blue',
                    borderWidth: 5,
                    fill: false
                }]
            },
            options: {
              
                scales: {
                    xAxes: [{
                        scaleLabel: {
                            display: true,
                            labelString: 'X Axis'
                        }
                    }],
                    yAxes: [{
                        scaleLabel: {
                            display: true,
                            labelString: 'Y Axis'
                        }
                    }]
                }
            }
        });
    	
		
        // Update table with highest and lowest values
        const highestValue = Math.max(...yAxesData);
        const highestIndex = yAxesData.indexOf(highestValue);
        const highestXAxis = xAxesData[highestIndex];

        const lowestValue = Math.min(...yAxesData);
        const lowestIndex = yAxesData.indexOf(lowestValue);
        const lowestXAxis = xAxesData[lowestIndex];
        
        let xAxisLength =xAxesData[xAxesData.length-1];
		
        document.getElementById('downloadBtn').onclick = function(){downloadChart()};

        // Update table with highest and lowest values
       
        document.getElementById('highest-value').textContent = highestValue;
        document.getElementById('highest-x-axis').textContent = highestXAxis;
        document.getElementById('lowest-value').textContent = lowestValue;
        document.getElementById('lowest-x-axis').textContent = lowestXAxis;
        document.getElementById('duration').textContent = xAxisLength;
       
   
function downloadChart() {
    if(myChart) {
    	var url_base64 = myChart.toBase64Image();
    	var a = document.createElement('a');
    	a.href = myChart.toBase64Image();
    	a.download = 'myChart.png'; // Specify the download filename
    	a.click(); // Simulate click to download
           } else {
           alert("Chart is not ready yet.");
           }
        }

 });
