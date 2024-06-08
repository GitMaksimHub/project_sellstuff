import React, { useState, useEffect } from "react";
import axios from "axios";
// checked
// izmeneniya
// branch frontend
// another commit
function App() {
  const [details, setDetails] = useState([]);

  useEffect(() => {
    axios
      .get("http://localhost:8000/test_api")
      .then((res) => {
        setDetails(res.data);
      })
      .catch((err) => {
        console.error("Ошибка при получении данных:", err);
      });
  }, []);

  return (
    <div>
      <header>Данные из Django</header>
      <hr></hr>
      <ul>
        {details.map((item, index) => (
          <li key={index}>
            <h2>{item.title}</h2>
            <p>{item.description}</p>
          </li>
        ))}
      </ul>
    </div>
  );
}

export default App;
