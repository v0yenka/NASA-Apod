import { useState, useEffect } from 'react';

function Planets() {
  const [planets, setPlanets] = useState([]);

  useEffect(() => {
    fetch('http://127.0.0.1:8000/planets')
      .then(response => response.json())
      .then(data => setPlanets(data))
      .catch(err => console.error(err));
  }, []);

  return (
    <div className="content-box">
      <h2>Encyklopedia Planet</h2>
      <div className="planets-grid">
        {planets.map((planet) => (
          <div key={planet.name} className="planet-card">
            <img src={planet.image} alt={planet.name} className="planet-img"/>
            <h3>{planet.name}</h3>
            <p>{planet.desc}</p>
          </div>
        ))}
      </div>
    </div>
  );
}
export default Planets;