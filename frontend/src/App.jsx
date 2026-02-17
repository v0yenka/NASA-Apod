import { useState } from 'react';
import { BrowserRouter as Router, Routes, Route, NavLink } from 'react-router-dom';
import Apod from './Apod';
import Planets from './Planets';
import './App.css';

function App() {
  const [isSidebarOpen, setIsSidebarOpen] = useState(false);

  const toggleSidebar = () => {
    setIsSidebarOpen(!isSidebarOpen);
  };

  return (
    <Router>
      <div className="app-layout">
        
        {/* Hamburger Button showing only when sidebar is closed */}
        {!isSidebarOpen && (
          <button className="hamburger-btn" onClick={toggleSidebar}>
            ☰
          </button>
        )}

        {/* Menu */}
        <nav className={`sidebar ${isSidebarOpen ? 'open' : ''}`}>
          <div className="sidebar-header">
            <h2 className="brand-logo">NASA PROJECT</h2>
            
            <button className="close-btn" onClick={toggleSidebar}>×</button>
          </div>
          
          <ul className="sidebar-links">
            <li>
              <NavLink to="/" onClick={toggleSidebar}>📸 Zdjęcie Dnia</NavLink>
            </li>
            <li>
              <NavLink to="/planets" onClick={toggleSidebar}>🪐 Planety</NavLink>
            </li>
          </ul>
        </nav>

        {/* Treść strony */}
        <main className="main-content">
          <Routes>
            <Route path="/" element={<Apod />} />
            <Route path="/planets" element={<Planets />} />
          </Routes>
        </main>

        {/* Ciemne tło */}
        {isSidebarOpen && <div className="overlay" onClick={toggleSidebar}></div>}
      </div>
    </Router>
  );
}

export default App;
