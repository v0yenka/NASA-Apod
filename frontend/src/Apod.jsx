import { useState, useEffect } from 'react';

function Apod() {
  const [data, setData] = useState(null);
  const [date, setDate] = useState('');

  const fetchData = async (selectedDate) => {
    try {
      let url = 'http://127.0.0.1:8000/apod';
      if (selectedDate) url += `?date=${selectedDate}`;
      const response = await fetch(url);
      const result = await response.json();
      setData(result);
    } catch (error) { console.error(error); }
  };

  useEffect(() => { fetchData(); }, []);

  return (
    <div className="apod-container">
      <h1>Zdjęcie Dnia NASA</h1>
      
      {/* MAIN LAYOUT: Two columns - Date Picker on the left, Photo/Video + Description on the right */}
      <div className="apod-layout">
        
        {/* LEFT COLUMN: Date Picker */}
        <div className="apod-sidebar">
          <h3>Wybierz datę:</h3>
          <input 
            type="date" 
            className="date-picker"
            onChange={(e) => { setDate(e.target.value); fetchData(e.target.value); }} 
            max={new Date().toISOString().split("T")[0]}
          />
        </div>

        {/* RIGHT COLUMN: Photo/Video + Description */}
        <div className="apod-content">
          {data ? (
            data.code && data.code !== 200 ? (
               <p className="error-msg">Błąd NASA: {data.msg}</p>
            ) : (
              // Flexbox (Photo next to Description)
              <div className="content-flex">
                
                {/* Photo/Video */}
                <div className="media-container">
                  <h2>{data.title}</h2>
                  {data.media_type === "image" ? (
                    <img src={data.url} alt={data.title} className="main-img" />
                  ) : (
                    <iframe src={data.url} className="main-video"></iframe>
                  )}
                </div>
                
                {/* Description */}
                <div className="text-container">
                  <h3>Opis:</h3>
                  <p className="explanation-text">{data.explanation}</p>
                  <p className="date-info">Data: {data.date}</p>
                </div>

              </div>
            )
          ) : (
            <p>Ładowanie kosmosu...</p>
          )}
        </div>
      </div>
    </div>
  );
}
export default Apod;