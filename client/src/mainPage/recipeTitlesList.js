import React from "react";
import { Link } from "react-router-dom";
import axios from "axios";


function RecipeTitlesList({data}) {
    const recipes = Object.values(data);

    

    return (
        <ul>
            {recipes.map((value, index) => (
                <li key={index}>
                    <Link to="/recipePage" onClick={
                        () => {
                            axios.post('/retrieveRecipe', {
                                "recipeTitle": value
                            })
                        }
                    }>{value}</Link>
                </li>
            ))}
        </ul>    
    );
}

export default RecipeTitlesList;