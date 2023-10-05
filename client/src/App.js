import React, {useState, useEffect} from 'react'
import {BrowserRouter as Router, Routes, Route, Link} from "react-router-dom";
import MainPage from './mainPage/main'
import RecipePage from "./recipeContent/recipePage";


function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<MainPage/>}/>
        <Route path="/recipePage" element={<RecipePage/>}/>
      </Routes>
    </Router> 
  );
}

export default App;
