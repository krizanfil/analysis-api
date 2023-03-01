import React, {useEffect, useRef, useState} from 'react';
import axios from 'axios';
import {Chart} from 'chart.js/auto';

const Graph: React.FC = () => {
  const [data, setData] = useState<{ [key: string]: number }>();
  const [inputValue, setInputValue] = useState<string>('');
  const chartRef = useRef<HTMLCanvasElement>(null);

  useEffect(() => {
    axios.get('http://127.0.0.1:5000/api/analyze/AAPL').then((result) => setData(result.data));
  }, []);

  const createChart = () => {
    if (data && chartRef.current) {
      return new Chart(chartRef.current, {
        type: 'bar',
        data: {
          labels: Object.keys(data),
          datasets: [
            {
              label: 'Numbers',
              data: Object.values(data),
              backgroundColor: ['rgba(255, 99, 132, 0.2)', 'rgba(54, 162, 235, 0.2)'],
              borderColor: ['rgba(255, 99, 132, 1)', 'rgba(54, 162, 235, 1)'],
              borderWidth: 1,
            },
          ],
        },
        options: {
          scales: {
            y: {
              beginAtZero: true,
            },
          },
        },
      });
    }
  };

  useEffect(() => {
    const currChart = createChart();
    return () => {
      if (currChart) {
        currChart.destroy();
      }
    };
  }, [data]);

  const handleInputChange = (event: React.ChangeEvent<HTMLInputElement>) => {
    setInputValue(event.target.value);
  };

  const handleButtonClick = () => {
  axios
    .get(`http://127.0.0.1:5000/api/analyze/${inputValue}`)
    .then((result) => setData(result.data));
};


  return (
    <div>
      <canvas ref={chartRef} id="myChart"></canvas>
      <div style={{ marginTop: '20px' }}>
        <input type="text" value={inputValue} onChange={handleInputChange} />
        <button onClick={handleButtonClick}>Analyze</button>
      </div>
    </div>
  );
};

export default Graph;
