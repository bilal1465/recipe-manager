import { Button } from "bootstrap";
import React, { useState } from "react";
import axios from "axios";

function AddRecipe() {
    const [recipeURL, setURL] = useState("");

    function editURL(event) {
        setURL(event.target.value)
    }

    function submitURL() {
        axios.post('/submitURL', {
            "recipeURL": recipeURL
        })
    }

    return (
        <div>
        <input 
            type="text"
            placeholder="Enter recipe URL here"
            onChange={editURL}
            value={recipeURL}
        />
        <button onClick={submitURL}>Add</button>
        </div>
    );
}

export default AddRecipe;